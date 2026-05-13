from google import genai
import streamlit as st
import os

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"

st.header(":bird: AI Tweet Generator")

st.subheader(":heart: Made with Build Fast with AI")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    client = genai.Client(api_key=st.secrets['GOOGLE_API_KEY'])
    prompt = tweet_template.format(number=number, topic=topic)
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=prompt
    )
    
    # Extract only the text parts manually to avoid the "non-text parts" warning
    final_text = ""
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'text') and part.text:
                final_text += part.text
                
    st.write(final_text)
