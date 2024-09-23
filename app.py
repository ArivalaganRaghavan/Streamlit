import streamlit as st

st.header("learning is fun")


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

st.subheader("_Streamlit_ is :blue[cool] : sunglass:")
