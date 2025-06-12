from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#streamlit app
st.set_page_config(page_title="QnA Demo")

st.header("Generative LLM App")

input=st.text_input("Input:",key="input")
submit=st.button("Submit")

#when submit button is clicked


if submit:
    response=get_gemini_response(input)
    st.write("The response is : " , response)