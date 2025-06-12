# 🤖 LLM Applications using Gemini model

This repository contains two powerful LLM-based applications built using Google's **Gemini 1.5 Flash** model via `google.generativeai`. These apps demonstrate both text-based and image-based interaction capabilities.

---

## 🔧 Prerequisites

- Python 3.9+
- API key from [Google AI Studio](https://makersuite.google.com/)
- Required libraries (install via `requirements.txt`)

### Installation

```bash
git clone https://github.com/DARSHAN9029/Gemini_LLMs.git
python -m venv myvenv
source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
pip install -r requirements.txt
```
---
Api key:
```
GOOGLE_API_KEY=your_google_api_key_here
```
---
📄 1. app.py — Text QnA Chatbot
A basic chatbot using Gemini 1.5 Flash that allows users to ask questions and get conversational responses.

🔹 How to Run
```bash
streamlit run app.py
```
🔹 Features
Text-only input and response

Powered by Gemini's generative capabilities

Lightweight and responsive
---
🖼️ 2. vision.py — Image-to-Text + Chat Bot
This app lets users upload an image and chat about its content using Gemini's multimodal features.

🔹 How to Run
```bash
streamlit run vision.py
```
🔹 Features
Upload images (PNG, JPG, etc.)

Ask questions related to the image

Conversational and context-aware image understanding
---
🧪 Requirements
Create a requirements.txt:
```
streamlit
python-dotenv
google-generativeai
Pillow
```
