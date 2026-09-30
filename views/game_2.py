import streamlit as st

st.title("🪨 Rock, Paper, Scissors ✂️")

# Initialize scores
if "scores" not in st.session_state:
    st.session_state.scores = {"Player": 0, "Computer": 0}

choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

# Action buttons side-by-side
cols = st.columns(3)
player_choice = None

for i, choice in enumerate(choices):
    if cols[i].button(f"{emojis[choice]} {choice}", use_container_width=True):
        player_choice = choice

if player_choice:
    computer_choice = random.choice(choices)
    
    st.write(f"You chose: **{emojis[player_choice]} {player_choice}**")
    st.write(f"Computer chose: **{emojis[computer_choice]} {computer_choice}**")
    
    # Logic matrix
    if player_choice == computer_choice:
        st.info("It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
        (player_choice == "Paper" and computer_choice == "Rock") or \
        (player_choice == "Scissors" and computer_choice == "Paper"):
        st.success("You win this round! 🎉")
        st.session_state.scores["Player"] += 1
    else:
        st.error("Computer wins this round! 🤖")
        st.session_state.scores["Computer"] += 1

# Scoreboard layout
st.divider()
sc1, sc2 = st.columns(2)
sc1.metric("Your Score", st.session_state.scores["Player"])
sc2.metric("Computer Score", st.session_state.scores["Computer"])

if st.button("Reset Scores"):
    st.session_state.scores = {"Player": 0, "Computer": 0}
    st.rerun()
    
if st.button("← Back to Lobby"):
    st.switch_page("views/homepage.py")