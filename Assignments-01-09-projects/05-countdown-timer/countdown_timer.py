import streamlit as st
import time

st.set_page_config(page_title="Countdown Timer", layout="centered")

st.title("⏳ Countdown Timer")

# Input from user
seconds = st.number_input("Enter time in seconds:", min_value=1, step=1)

# Start button
if st.button("Start Countdown"):
    placeholder = st.empty()
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        placeholder.markdown(f"### ⏱ Time Left: `{timer_format}`")
        time.sleep(1)

    placeholder.markdown("## ✅ Time's up!")
