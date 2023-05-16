import streamlit as st

st.title("Contact Us")
with st.form(key="my_form"):
    user_email=st.text_input("Enter Your Email Address",placeholder="email")
    message=st.text_area("Your Message")
    button= st.form_submit_button("Submit")

#if button:


