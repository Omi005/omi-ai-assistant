# 🤖 Omi AI Assistant

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Groq](https://img.shields.io/badge/AI-Groq-green)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7)

</p>

A modern AI chatbot built with **Python, Flask, Groq API, SQLite, HTML, CSS, Tavily and JavaScript**.

Omi AI Assistant provides a clean ChatGPT-like interface where users can create multiple conversations, save chat history, switch between dark and light mode, display beautifully formatted code blocks, and receive intelligent AI responses powered by **Llama 3.3 70B Versatile**.

---

# 🚀 Live Demo

**Try Omi AI Assistant here**

👉 https://omi-ai-assistant.onrender.com/ 

---

# 📂 GitHub Repository

https://github.com/Omi005/omi-ai-assistant

---

# 📸 Project Preview

## 🏠 Home Screen

<p align="center">
<img src="images/Home Screen.png" width="900">
</p>

---

## 🌙 Dark Mode

<p align="center">
<img src="images/Dark Mode.png" width="900">
</p>

---

## 💻 Code Generation

<p align="center">
<img src="images/Code Generation.png" width="900">
</p>

---

## 📱 Mobile View

<p align="center">
<img src="images/Mobile View.png" width="350">
</p>

---

## 🕒 Chat History

<p align="center">
<img src="images/Chat History.png" width="350">
</p>

---

# ✨ Features

## 💬 AI Chat

- AI-powered conversations using the Groq API
- Powered by **Llama 3.3 70B Versatile**
- Maintains conversation context within each chat

---

## 🗂 Multiple Chat Management

- Create unlimited chat sessions
- Automatically save conversations
- Load previous chats
- Delete chats permanently

---

## 🧠 Automatic Chat Titles

The first user message automatically becomes the chat title, making conversations easy to identify.

---

## 💻 Beautiful Code Blocks

- Syntax Highlighting
- Language Detection
- Copy Button
- Clean Formatting

---

## 📋 Copy Code

Copy any generated code with a single click.

---

## 📝 Markdown Rendering

Supports:

- Headings
- Bold
- Italics
- Lists
- Tables
- Inline Code
- Code Blocks

---

## 🌙 Dark Mode

- Light Mode
- Dark Mode

Theme preference is saved in the browser.

---

## 📱 Responsive Design

Optimized for:

- Desktop
- Laptop
- Tablet
- Mobile

Includes:

- Responsive Sidebar
- Mobile Navigation
- Sidebar Overlay
- Adaptive Layout

---

## ⌨️ Smart Input Box

- Auto-expanding textarea
- Enter → Send Message
- Shift + Enter → New Line

---

## ⏳ Typing Indicator

Displays:

```
Omi is typing...
```

while waiting for the AI response.

---

## 💾 Chat History

Chat history is stored using SQLite.

- When running locally, chats persist between application restarts.
- On the Render free tier, chat history may reset after a redeploy or service restart because the filesystem is ephemeral.

---

## 🎨 Modern UI

- Rounded Chat Bubbles
- User & AI Avatars
- Smooth Animations
- Custom Scrollbars
- Professional Layout

---

# 🛠 Technologies Used

## Backend

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Python-dotenv
- Groq API
- Tavily API

---

## Frontend

- HTML5
- CSS3
- JavaScript (ES6)

---

## Libraries

## Backend

- Flask
- Flask-SQLAlchemy
- Groq Python SDK
- Tavily Python SDK
- Python-dotenv

---

## Frontend

- Marked.js (Markdown Rendering)
- Highlight.js (Syntax Highlighting)

---

# 📂 Project Structure

```text
Omi AI Assistant/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── instance/
│   └── chat_history.db
│
├── .env
├── .gitignore
├── requirements.txt
├── Procfile
├── main.py
└── README.md
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Omi005/omi-ai-assistant.git
```

---

## 2. Navigate to the Project Directory

```bash
cd omi-ai-assistant
```

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Create a `.env` File

Create a `.env` file in the project root and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## 6. Get Your API Keys

### Groq API

1. Visit https://console.groq.com/keys
2. Sign in or create an account.
3. Generate a new API key.
4. Copy the key into your `.env` file.

### Tavily API

1. Visit https://app.tavily.com/
2. Sign in or create an account.
3. Generate a new API key.
4. Copy the key into your `.env` file.

---

## 7. Run the Application

```bash
python main.py
```

or

```bash
python3 main.py
```

---

## 8. Open Your Browser

Visit:

```
http://127.0.0.1:5000
```

Your Omi AI Assistant should now be running locally.

# ☁️ Deployment

Omi AI Assistant is deployed on **Render**.

The deployment uses:

- Flask
- Gunicorn
- Render Web Service
- GitHub Integration
- Environment Variables

Every push to the GitHub repository can automatically trigger a new deployment on Render.

---

## Environment Variables

Configure the following environment variables in your Render dashboard:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Build Command

```bash
pip install -r requirements.txt
```

---

## Start Command

```bash
gunicorn main:app
```

---

## Notes

- SQLite is used for storing chat history.
- On the Render Free plan, the filesystem is **ephemeral**, meaning the SQLite database may reset after a service restart or redeployment.
- For permanent chat history in production, consider using PostgreSQL or another managed database.

# ⚙️ How It Works

1. The user enters a message in the chat interface.
2. Flask receives the request from the frontend.
3. The user's message is saved to the SQLite database.
4. The previous conversation history for that chat is loaded.
5. A lightweight AI classifier determines whether the question requires current or real-time information.
6. If a web search is needed, the Tavily Search API retrieves relevant and up-to-date information.
7. The search results are added to the conversation as additional context.
8. The complete conversation is sent to Groq's **Llama 3.3 70B Versatile** model.
9. The AI generates a response using the conversation history and, when available, the web search results.
10. The AI response is saved to the SQLite database.
11. Markdown is rendered, code blocks are syntax highlighted, and copy buttons are added.
12. The formatted response is displayed in the chat interface.

---

# 📚 Database

SQLite stores:

- Chat Titles
- User Messages
- AI Responses

Tables:

- Chat
- Message

---

# 🔒 Environment Variables

The project securely stores API keys using:

```
.env
```

The `.env` file is excluded from Git using `.gitignore`.

---

# 🚧 Future Improvements

- 🎤 Voice Input
- 🔊 Text-to-Speech
- 🖼 AI Image Generation
- 📎 File Upload Support
- 📄 PDF & Document Analysis
- 🌍 Multi-language Support
- 💬 Streaming AI Responses
- 👤 User Authentication
- ☁️ Cloud Database (PostgreSQL/MySQL)
- 📤 Chat Export (PDF/Markdown)
- ⭐ Pin & Favorite Chats
- 🔍 Chat Search
- 🧠 Support for Multiple AI Models
- ⚙️ Custom AI Settings (Temperature, Model Selection)
- 📱 Progressive Web App (PWA) Support

---

# 👨‍💻 Author

**Omkar**

Omi AI Assistant was developed as a personal project to explore modern AI application development using Python and Flask.

Through this project, I gained hands-on experience with:

- Python
- Flask
- SQLAlchemy
- SQLite
- Groq API
- Tavily Search API
- REST APIs
- HTML, CSS & JavaScript
- Markdown Rendering
- Responsive Web Design
- AI Prompt Engineering
- Deployment with Render

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.