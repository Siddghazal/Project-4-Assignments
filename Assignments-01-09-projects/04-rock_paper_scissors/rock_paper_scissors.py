import streamlit as st
import random

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def play(user_choice):
    computer = random.choice(['r', 'p', 's'])
    
    choices_map = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    result = ""

    if user_choice == computer:
        result = "It's a tie!"
    elif is_win(user_choice, computer):
        result = "You won!"
    else:
        result = "You lost!"
    
    return result, choices_map[user_choice], choices_map[computer]

# --- Streamlit UI ---
st.title("✊ Rock ✋ Paper ✌️ Scissors Game")

user_choice = st.radio("Choose your option:", ['Rock', 'Paper', 'Scissors'])

choice_map = {'Rock': 'r', 'Paper': 'p', 'Scissors': 's'}

if st.button("Play"):
    result, user, computer = play(choice_map[user_choice])
    st.write(f"**You chose:** {user}")
    st.write(f"**Computer chose:** {computer}")
    st.subheader(result)
