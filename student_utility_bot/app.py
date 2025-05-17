import streamlit as st
from graph import build_graph

st.set_page_config(page_title="Student Utility Bot", page_icon="🎓")
st.title("🎓 Student Utility Bot")

user_query = st.text_area("Enter your request (email, math, explanation, or learning plan):")

if st.button("Submit"):
    if not user_query.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Thinking..."):
            app = build_graph()
            result = app.invoke({"user_input": user_query})
            st.success("Result:")
            st.write(result["result"])
