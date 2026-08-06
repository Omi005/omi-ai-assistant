from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from groq import Groq
from tavily import TavilyClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# SQLite Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chat_history.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

# ==========================
# DATABASE MODELS
# ==========================

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer)
    role = db.Column(db.String(20))
    content = db.Column(db.Text)


# ==========================
# SYSTEM PROMPT
# ==========================

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are Omi, an intelligent AI assistant created by Omkar. "
        "You are friendly, helpful, professional, and knowledgeable."
    )
}


# ==========================
# WEB SEARCH
# ==========================

def search_web(query):

    try:

        response = tavily.search(
            query=query,
            search_depth="basic",
            max_results=5
        )

        return response.get("results", [])

    except Exception as e:

        print("Tavily Error:", e)

        return []


def ai_should_search(query):

    decision = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a classifier. "
                    "Reply ONLY with YES or NO.\n\n"
                    "Reply YES if answering the user's question requires current, live, or recent information from the internet.\n"
                    "Reply NO if the question can be answered from general knowledge."
                )
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=0
    )

    answer = decision.choices[0].message.content.strip().upper()

    return answer.startswith("YES")


# ==========================
# TEST WEB SEARCH
# ==========================

@app.route("/test_search")
def test_search():

    results = search_web("Latest AI news")

    return jsonify(results)


# ==========================
# HOME
# ==========================

@app.route("/")
def home():

    chats = Chat.query.order_by(
        Chat.id.desc()
    ).all()

    return render_template(
        "index.html",
        chats=chats
    )


# ==========================
# CREATE NEW CHAT
# ==========================

@app.route("/new_chat", methods=["POST"])
def new_chat():

    chat = Chat(
        title="New Chat"
    )

    db.session.add(chat)
    db.session.commit()

    return jsonify({
        "chat_id": chat.id
    })


# ==========================
# LOAD CHAT
# ==========================

@app.route("/load_chat/<int:chat_id>")
def load_chat(chat_id):

    messages = Message.query.filter_by(
    chat_id=chat_id
    ).order_by(Message.id).all()

    data = []

    for msg in messages:

        data.append({
            "role": msg.role,
            "content": msg.content
        })

    return jsonify(data)

# ==========================
# DELETE CHAT
# ==========================

@app.route("/delete_chat/<int:chat_id>", methods=["POST"])
def delete_chat(chat_id):

    # Delete all messages in the chat
    Message.query.filter_by(
        chat_id=chat_id
    ).delete()

    # Delete the chat itself
    Chat.query.filter_by(
        id=chat_id
    ).delete()

    db.session.commit()

    return jsonify({
        "success": True
    })


# ==========================
# CHAT
# ==========================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    chat_id = data["chat_id"]
    user_message = data["message"]

    chat_obj = db.session.get(Chat, chat_id)

    # Update title from first user message
    if chat_obj and chat_obj.title == "New Chat":
        chat_obj.title = user_message[:30]
        db.session.commit()

    # Save user message
    db.session.add(
        Message(
            chat_id=chat_id,
            role="user",
            content=user_message
        )
    )
    db.session.commit()

# ==========================
# BUILD CONVERSATION
# ==========================

    conversation = [SYSTEM_PROMPT]

    # Decide whether a web search is needed
    decision = ai_should_search(user_message)
    print("AI SEARCH DECISION:", decision)

    if decision:

        search_results = search_web(user_message)

        print("\n===== TAVILY RESULTS =====")
        print(search_results)
        print("==========================\n")

        if search_results:

            web_context = "Web Search Results:\n\n"

            for result in search_results:

                title = (result.get("title") or "").strip()

                content = (result.get("content") or "").strip()

                url = (result.get("url") or "").strip()

                if not content:
                    content = "No summary was provided by the search result."

                web_context += (
                    f"Title: {title}\n"
                    f"Content: {content[:400]}\n"
                    f"Source: {url}\n\n"
                )

            conversation.append({
                "role": "system",
                "content": f"""
You have been provided with recent web search results.

Instructions:
- Use the web search results as your primary source whenever they answer the user's question.
- Write naturally, as if you already know the information.
- Do NOT say "According to the web search results."
- Do NOT mention that you searched the web.
- Do NOT say your knowledge is limited or that you cannot browse the internet.
- If multiple sources disagree, mention the disagreement.
- If the search results are incomplete or unclear, say you couldn't find enough reliable information instead of guessing.
- Keep your answer concise unless the user asks for more detail.

Web Search Results:

{web_context}
"""
            })

        else:

            conversation.append({
                "role": "system",
                "content": (
                    "A web search was attempted but no reliable results were found. "
                    "If the question requires current information, explain that you "
                    "couldn't find enough reliable information instead of guessing."
                )
            })

    # Load previous conversation
    previous_messages = Message.query.filter_by(
    chat_id=chat_id
    ).order_by(Message.id).all()

    for msg in previous_messages:

        conversation.append({
            "role": msg.role,
            "content": msg.content
        })

# ==========================
# DEBUG: PRINT CONVERSATION
# ==========================

    print("\n===== CONVERSATION SENT TO GROQ =====\n")

    for message in conversation:
        print(message["role"])
        print(message["content"][:500])   # Print first 500 characters
        print("-" * 60)

    # AI Response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation,
        temperature=0.7
    )

    assistant_reply = response.choices[0].message.content

    # Save AI response
    db.session.add(
        Message(
            chat_id=chat_id,
            role="assistant",
            content=assistant_reply
        )
    )

    db.session.commit()

    return jsonify({
        "reply": assistant_reply
    })


# ==========================
# RUN APP
# ==========================

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)