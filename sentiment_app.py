
import streamlit as st
from transformers import pipeline

# Load the model
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# Streamlit UI
st.set_page_config(page_title="Text Sentiment Analyzer", page_icon="🧠")
st.title("🔍 Text Sentiment Analyzer")
st.write("Enter a sentence, and I'll tell you whether it's **Positive**, **Negative**, or **Neutral**!")

# Input text
user_input = st.text_area("✏️ Your sentence:")

if st.button("Analyze Sentiment"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a sentence.")
    else:
        with st.spinner("Analyzing..."):
            result = model(user_input)[0]
            label = result["label"]
            confidence = round(result["score"] * 100, 2)

            if label == "POSITIVE":
                st.success(f"🙂 Positive — {confidence}% confident")
            elif label == "NEGATIVE":
                st.error(f"🙁 Negative — {confidence}% confident")
            else:
                st.info(f"😐 Neutral — {confidence}% confident")

            st.caption(f"Model Output: `{result}`")
