from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from groq import Groq
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
    ).all()

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

    chat_obj = Chat.query.get(chat_id)

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

    # Build conversation
    conversation = [SYSTEM_PROMPT]

    previous_messages = Message.query.filter_by(
        chat_id=chat_id
    ).all()

    for msg in previous_messages:

        conversation.append({
            "role": msg.role,
            "content": msg.content
        })

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

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)