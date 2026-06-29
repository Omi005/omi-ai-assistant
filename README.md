



# 🤖 Omi AI Assistant

A modern AI chatbot built with **Python, Flask, Groq API, SQLite, HTML, CSS, and JavaScript**.

Omi AI Assistant provides a clean ChatGPT-like interface where users can create multiple conversations, save chat history, switch between dark and light mode, display beautifully formatted code blocks, and receive intelligent AI responses powered by Groq's Llama 3.3 model.

---

# 📸 Project Preview

> Add screenshots of your chatbot here.

Example:

- Home Screen
- Dark Mode
- Mobile View
- Code Generation Example

---

# ✨ Features

## 💬 AI Chat

- Chat with an AI assistant powered by the Groq API.
- Uses the Llama 3.3 70B Versatile model.
- Maintains conversation context within each chat.

---

## 🗂 Multiple Chat Management

- Create unlimited chat sessions.
- Automatically save every conversation.
- Load previous chats anytime.
- Delete chats permanently.

---

## 🧠 Automatic Chat Titles

The first user message automatically becomes the chat title, making conversations easy to identify.

Example:

User message:

> Explain Python Lists

Sidebar title:

> Explain Python Lists

---

## 💻 Beautiful Code Blocks

When the AI generates code:

- Syntax highlighting
- Programming language detection
- Copy button
- Clean formatting

---

## 📋 Copy Code Button

Every code block includes a **Copy** button.

One click copies the generated code directly to the clipboard.

---

## 📝 Markdown Rendering

The chatbot supports Markdown formatting including:

- Headings
- Bold text
- Italics
- Lists
- Tables
- Inline code
- Code blocks

---

## 🌙 Dark Mode

Switch instantly between:

- ☀️ Light Mode
- 🌙 Dark Mode

---

## 📱 Responsive Design

Works smoothly on:

- Desktop
- Laptop
- Tablet
- Mobile Devices

Includes:

- Responsive sidebar
- Mobile navigation menu
- Sidebar overlay
- Auto-adjusting layout

---

## ⌨️ Smart Input Box

The input box automatically expands as you type longer messages.

Supports:

- Enter → Send message
- Shift + Enter → New line

---

## ⏳ Typing Indicator

Shows:

Omi is typing...

while waiting for the AI response.

---

## 💾 Persistent Chat History

Chat history is stored locally using SQLite.

Even after restarting the application, previous chats remain available.

---

## 🎨 Modern User Interface

Features include:

- Rounded chat bubbles
- User & AI avatars
- Smooth animations
- Custom scrollbars
- Clean layout
- Professional design

---

# 🛠 Technologies Used

## Backend

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- python-dotenv
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

```
Omi AI Assistant/
│
├── Static/
│   └── style.css
│
├── Templates/
│   └── index.html
│
├── instance/
│   └── chat_history.db
│
├── .env
├── .gitignore
├── main.py
└── README.md
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/omi-ai-assistant.git
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
pip install flask
pip install flask_sqlalchemy
pip install python-dotenv
pip install groq
```

Or install them using a requirements file if available.

---

## 5. Create a .env File

Create a file named:

```
.env
```

Add your Groq API key:

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

Visit:

```
http://127.0.0.1:5000
```

---

# ⚙️ How It Works

1. User sends a message.
2. Flask receives the request.
3. Previous chat history is loaded from SQLite.
4. Conversation is sent to the Groq API.
5. AI generates a response.
6. Response is stored in SQLite.
7. Response is displayed with Markdown formatting and syntax highlighting.

---

# 📚 Database

SQLite is used for storing:

- Chat titles
- User messages
- AI responses

Database tables:

- Chat
- Message

---

# 🔒 Environment Variables

This project uses:

```
.env
```

to securely store the Groq API key.

The `.env` file is excluded from Git using `.gitignore`.

---

# 🚧 Future Improvements

Planned features include:

- 🌐 Web Search
- 🖼 Image Generation
- 📎 File Upload Support
- 🎤 Voice Input
- 🔊 Text-to-Speech
- Streaming AI Responses
- User Authentication
- Chat Export
- Better Markdown Rendering

---

# 👨‍💻 Author

**Omkar**

Built as a personal AI assistant project to learn:

- Flask
- Python
- Frontend Development
- AI Integration
- API Development
- Database Management

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ If You Like This Project

If you found this project helpful, consider giving it a ⭐ on GitHub.