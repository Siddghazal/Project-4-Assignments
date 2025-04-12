import streamlit as st
import random
import string

# Title
st.title("🔐 Password Generator")

# User inputs
length = st.slider("Select password length:", min_value=4, max_value=50, value=12)
include_upper = st.checkbox("Include Uppercase Letters (A-Z)", value=True)
include_lower = st.checkbox("Include Lowercase Letters (a-z)", value=True)
include_digits = st.checkbox("Include Numbers (0-9)", value=True)
include_symbols = st.checkbox("Include Symbols (!@#$%^&*)", value=True)

# Generate password button
if st.button("Generate Password"):
    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
        st.success("Your Generated Password:")
        st.code(password)
    else:
        st.warning("Please select at least one character set!")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")
