# 🧠 Text Sentiment Analyzer

A lightweight Streamlit web app that uses a Hugging Face transformer model to detect sentiment in English sentences.  
🔍 It classifies text as **Positive**, **Negative**, or **Neutral** (inferred by confidence threshold).

### 🌐 Live Demo

👉 [Click here to try it out](https://text-sentimentanalyzer.streamlit.app/)

---

## 🚀 Features

- ✅ Simple, clean UI (built with Streamlit)
- 🤖 Powered by Hugging Face's `distilbert-base-uncased-finetuned-sst-2-english`
- ⚡ Instant analysis of sentence-level sentiment
- 📊 Shows confidence scores with emojis and colors

---


## 🛠️ How It Works

- Input: A sentence from the user
- Model: `distilbert-base-uncased-finetuned-sst-2-english`
- Output: Sentiment label (`POSITIVE`, `NEGATIVE`) and confidence
- Logic: If model confidence is below a threshold, label is treated as `Neutral`

---

## 📦 Installation (Local)

```bash
git clone https://github.com/your-username/text-sentiment-analyzer.git
cd text-sentiment-analyzer
pip install -r requirements.txt
streamlit run sentiment_app.py
```
## 🧪 Example
  - Input: I love using AI to make life easier.
  - Output: 🙂 Positive — 99.2% confident
