# 🤖 Local AI Chatbot

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Framework](https://img.shields.io/badge/Framework-Streamlit-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

A conversational AI chatbot built with **Python**, **Streamlit**, and the **OpenAI API**.

The application provides a ChatGPT-style interface that runs locally in your browser while securely communicating with OpenAI's language models.

---

# 📋 Features

- 💬 ChatGPT-style conversational interface
- 💾 Saved conversations
- 📁 Sidebar chat navigation
- 🔒 Secure API key management
- 🌐 Streamlit web interface
- 🤖 OpenAI API integration
- 📄 Local JSON chat storage
- 🐍 Python virtual environment support

---

# 🛠 Technologies

- Python 3.14
- Streamlit
- OpenAI Python SDK
- JSON
- Git
- GitHub
- Visual Studio Code

---

# 📁 Project Structure

```text
local-ai-chatbot/
│
├── assets/
│   ├── chatbot-home.png
│   ├── saved-chats.png
│   └── architecture.png
│
├── chatbot.py
├── chats.json
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/dreevesjr1/local-ai-chatbot.git

cd local-ai-chatbot
```

## 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

Activate it

```powershell
.venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Your OpenAI API Key

```powershell
$env:OPENAI_API_KEY="YOUR_API_KEY"
```

Never place your API key inside your source code.

---

# ▶️ Run the Application

```bash
python -m streamlit run chatbot.py
```

Open your browser:

```
http://localhost:8501
```

---

# 📸 Screenshots

## Home Screen

![Home Screen](assets/chatbot-home.png)

---

## Saved Chats

![Saved Chats](assets/saved-chats.png)

---

## Architecture

![Architecture](assets/architecture.png)

---

# 💡 Skills Demonstrated

- Python Programming
- Object-Oriented Programming
- REST API Integration
- Streamlit Development
- Prompt Engineering
- Environment Variables
- Virtual Environments
- JSON Data Storage
- Git Version Control
- Debugging

---

# 🔮 Future Improvements

- SQLite database
- User authentication
- Chat search
- Chat renaming
- Conversation export
- PDF upload
- Image generation
- Voice input
- Docker support
- Cloud deployment

---

# 📚 Lessons Learned

This project demonstrates how to:

- Build AI applications with Python
- Integrate the OpenAI API
- Create web applications using Streamlit
- Secure API credentials
- Persist conversation history
- Manage project dependencies using virtual environments
- Organize code with Git and GitHub

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository, create a feature branch, and submit a pull request.

---

# 👨‍💻 Author

**Daniel Reeves**

Technical Information Systems Student

GitHub: https://github.com/dreevesjr1

---

# 📄 License

This project is licensed under the MIT License.
