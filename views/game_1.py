import streamlit as st
    
st.title("❌ Tic-Tac-Toe ⭕")

if st.toggle("Music 🎵 ", value=True):
    lofi_path = r"C:\vagmi\Learn-Gen-AI\Test-jupyter\alex-morgan-lofi-beat-homework-focus-concentration-587404.mp3" 
    st.audio(lofi_path, format="audio/mp3", loop=True, autoplay=True)
else:
    st.write("🔇 Music muted.")
    
## Main Code:
print("\n\n")
# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

def check_winner():
    b = st.session_state.board
    win_lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for x, y, z in win_lines:
        if b[x] and b[x] == b[y] == b[z]:
            return b[x]
    if "" not in b:
        return "Tie"
    return None

def make_move(idx):
    if not st.session_state.board[idx] and not st.session_state.winner:
        st.session_state.board[idx] = st.session_state.turn
        st.session_state.winner = check_winner()
        st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

# Render board using 3x3 columns
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        cell_text = st.session_state.board[idx] or " "
        if cols[col].button(cell_text, key=f"ttt_{idx}", use_container_width=True):
            make_move(idx)
            st.rerun()

# Display results or turn
if st.session_state.winner:
    if st.session_state.winner == "Tie":
        st.info("It's a tie game!")
    else:
        st.success(f"Player {st.session_state.winner} wins! 🎉")
else:
    st.write(f"Current Turn: **{st.session_state.turn}**")

if st.button("Reset Game", key="reset_ttt"):
    del st.session_state.board
    st.rerun()
    
if st.button("← Back to Lobby"):
    st.switch_page("views/homepage.py")


