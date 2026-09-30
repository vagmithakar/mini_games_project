import streamlit as st

st.set_page_config(layout="wide")
# 1. Define your page objects
home_page = st.Page("views/homepage.py", title="Mini Games! 🎮 ", default = True)
game_1_page = st.Page("views/game_1.py", title="Game 1: Tic-tac-toe ❌⭕")  # <-- This is your page object
game_2_page = st.Page("views/game_2.py", title="Game 2: Rock, paper, scissors 🪨 ✂️")
game_3_page = st.Page("views/game_3.py", title="Game 3: Memory game 🧩")

# 2. Initialize navigation
pg = st.navigation([home_page, game_1_page, game_2_page, game_3_page])
pg.run()

# 3. Trigger the switch using the object variable name
