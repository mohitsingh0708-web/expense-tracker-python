🤖 SmartAssist AI Chatbot

A clean, modern, beginner-friendly AI chatbot built using Python, NLTK, and Streamlit.
SmartAssist responds to user messages using rule-based NLP logic and features a polished, chat-app style UI.

⸻

✨ Features
	•	🔍 NLP-powered chatbot using NLTK
	•	💬 Modern chat interface with Streamlit
	•	🎨 Beautiful chat bubbles (user + bot)
	•	⚡ Real-time auto-refresh using st.rerun()
	•	🧩 Simple rule-based architecture (easy to customize)
	•	🪶 Lightweight: only Python + Streamlit + NLTK

⸻

📸 Demo

Example chat interface:

(Optional: Add an actual screenshot of your chatbot UI here.)

⸻

🧰 Tech Stack

Technology	Purpose
Python	Core programming language
Streamlit	Web UI & front-end interface
NLTK	Natural language processing + Chat logic
Regex	Pattern matching for chatbot rules


⸻

📂 Project Structure

SmartAssist-Chatbot/
│── app.py            # Main Streamlit application
│── requirements.txt  # Dependencies
└── README.md         # Project documentation


⸻

🚀 How to Run Locally

Follow these steps:

1. Clone the repository

git clone https://github.com/<sahilsingh1021y>/SmartAssist-Chatbot.git
cd SmartAssist-Chatbot

2. Install dependencies

pip install -r requirements.txt

3. Run the app

streamlit run app.py

Once launched, Streamlit will open the chatbot in your browser.

⸻

🧠 How It Works
	1.	User sends a message ➝ input captured by Streamlit
	2.	Message passed to NLTK Chat class
	3.	Regex patterns match the user’s intent
	4.	Chatbot generates a matching response
	5.	Streamlit displays both messages in styled chat bubbles
	6.	UI refreshes automatically with st.rerun()

⸻

📌 Future Improvements
	•	Add conversational memory
	•	Integrate LLM (GPT-based) responses
	•	Add voice input/output
	•	Deploy to Streamlit Cloud or HuggingFace Spaces
	•	Add custom themes & animations

⸻

📝 License

This project is free and open-source. Feel free to modify and build upon it.

⸻

🌐 Connect

If you like this project, consider giving it a ⭐ on GitHub!

Made with ❤️ by Sahil.