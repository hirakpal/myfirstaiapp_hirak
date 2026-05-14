import streamlit as st
import anthropic

# Prompt template
inventor_template = (
    "Who invented the programming language {language}? "
    "Give a brief, factual answer including the inventor's name, "
    "the year it was created, and one interesting fact about its origin."
)

st.header("💻 Programming Language Inventor Finder")
st.subheader("❤️ Made by Hirak")

language = st.text_input(
    "Enter a Programming Language",
    placeholder="e.g. Python, Java, Rust..."
)

if st.button("Find Inventor"):
    if language.strip() == "":
        st.warning("Please enter a programming language name.")
    else:
        client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
        prompt = inventor_template.format(language=language.strip())

        response = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=300,
            temperature=0.2,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        # response.content is a list of content blocks; join text blocks safely
        final_text = ""
        for block in response.content:
            if getattr(block, "type", None) == "text":
                final_text += block.text

        st.write(final_text)
        
