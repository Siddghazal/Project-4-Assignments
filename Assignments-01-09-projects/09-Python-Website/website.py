import streamlit as st

# Title
st.title("Welcome to Ghazala's Website")

# Introduction
st.write("Hello! I'm **Ghazala**, a front-end developer currently learning Python.")

# Projects Section
st.header("My Projects")
st.write("- E-commerce Website using HTML, CSS, JavaScript")
st.write("- Growth Mindset App using Streamlit")
st.write("- Dynamic Web Pages using Next.js and Sanity")

# About Me Section
st.header("About Me")
st.write("I'm passionate about web development and love creating clean, user-friendly websites.")

# Contact Section
st.header("Contact Me")
name = st.text_input("Your Name")
message = st.text_area("Your Message")

if st.button("Send"):
    st.success(f"Thank you {name}, your message has been sent!")

# Footer
st.write("Made with ❤️ by Ghazala")
