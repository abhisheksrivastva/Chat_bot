# 🤖 Real-Time Emotion-Based Chatbot

This is a real-time rule-based chatbot built using **Python + Flask**, styled with **HTML/CSS**, and powered by a simple **JSON decision flow**. It can understand basic emotional cues (like “I feel low”) and respond accordingly. Perfect for beginners in AI, students, or anyone building a basic conversational interface.

---

## 📌 Features

- ✅ Real-time chat with no page refresh
- 🤗 Emotion-aware responses for “I feel low”, “What should I do?”, etc.
- 🧠 Lightweight logic using a JSON-based dialog tree
- 🎨 Clean UI with CSS
- 🛠 Easy to customize and extend
- 💬 Maintains basic state for conversation flow

---

## 🗂 Project Structure


chatbot_project/
└── realtime_chat/
├── app.py # Flask backend with routing and logic
├── dialog_flow.json # JSON decision tree for chatbot behavior
├── static/
│ └── style.css # Styling for the chat interface
└── templates/
└── index.html # Main chat UI (frontend)


---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.7 or higher
- pip package manager installed

### 📥 Clone the Repository

```bash
git clone https://github.com/yourusername/chatbot_project.git
cd chatbot_project/realtime_chat
