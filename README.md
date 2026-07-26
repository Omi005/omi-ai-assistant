# 🤖 Omi AI Assistant

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Groq](https://img.shields.io/badge/AI-Groq-green)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7)

</p>

A modern AI chatbot built with **Python, Flask, Groq API, SQLite, HTML, CSS, and JavaScript**.

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

---

## Frontend

- HTML5
- CSS3
- JavaScript (ES6)

---

## Libraries

- Highlight.js
- Marked.js

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

## 2. Open the Project

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

```env
GROQ_API_KEY=your_api_key_here
```

---

## 6. Run the Application

```bash
python main.py
```

or

```bash
python3 main.py
```

---

## 7. Open in Browser

```
http://127.0.0.1:5000
```

---

# ☁️ Deployment

This project is deployed on **Render** using:

- Flask
- Gunicorn
- GitHub Integration
- Environment Variables

Every push to GitHub can automatically trigger a new deployment on Render.

---

# ⚙️ How It Works

1. User sends a message.
2. Flask receives the request.
3. Previous chat history is loaded from SQLite.
4. Conversation is sent to the Groq API.
5. AI generates a response.
6. Response is stored in SQLite.
7. Markdown is rendered.
8. Code blocks are syntax highlighted.
9. The response is displayed in the chat interface.

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

- 🌐 Web Search
- 🖼 Image Generation
- 📎 File Upload
- 🎤 Voice Input
- 🔊 Text-to-Speech
- Streaming Responses
- User Authentication
- Chat Export
- Better Markdown Rendering

---

# 👨‍💻 Author

**Omkar**

Built to learn and practice:

- Python
- Flask
- AI Integration
- REST APIs
- SQLAlchemy
- Frontend Development
- Responsive UI Design
- Deployment with Render

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.