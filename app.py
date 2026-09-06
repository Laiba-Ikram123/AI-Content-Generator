
import os
import streamlit as st
from groq import Groq
from prompt import create_content_prompt

st.set_page_config(
    page_title="AI Content Generator",
    page_icon="🤖",
    layout="centered"
)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("API key not found.")
    st.stop()

client = Groq(api_key=api_key)


def generate_content(topic, content_type, tone, length):

    prompt = create_content_prompt(
        topic,
        content_type,
        tone,
        length
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI content generator."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


st.title("🤖 AI Content Generator")

st.write("Generate high-quality content using AI.")

topic = st.text_area(
    "Enter your topic",
    placeholder="Example: Benefits of Artificial Intelligence"
)

content_type = st.selectbox(
    "Content Type",
    [
        "LinkedIn Post",
        "Email",
        "Blog Introduction",
        "Instagram Caption",
        "Product Description"
    ]
)

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Friendly",
        "Creative",
        "Persuasive",
        "Simple"
    ]
)

length = st.selectbox(
    "Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

if st.button("✨ Generate Content"):

    if not topic.strip():
        st.warning("Please enter a topic.")

    else:

        with st.spinner("Generating content..."):

            try:

                result = generate_content(
                    topic,
                    content_type,
                    tone,
                    length
                )

                st.subheader("Generated Content")
                st.write(result)

            except Exception as e:
                st.error(f"Error: {e}")
