from google import genai
import streamlit as st

# Prompt template
inventor_template = "Who invented the programming language {language}? Give a brief, factual answer including the inventor's name, the year it was created, and one interesting fact about its origin."

st.header("💻 Programming Language Inventor Finder")
st.subheader("❤️ Made by Hirak")

language = st.text_input("Enter a Programming Language", placeholder="e.g. Python, Java, Rust...")

if st.button("Find Inventor"):
    if language.strip() == "":
        st.warning("Please enter a programming language name.")
    else:
        client = genai.Client(api_key=st.secrets['GOOGLE_API_KEY'])
        prompt = inventor_template.format(language=language)
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=prompt
        )

        final_text = ""
        if response.candidates and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if hasattr(part, 'text') and part.text:
                    final_text += part.text

        st.write(final_text)