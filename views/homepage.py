import streamlit as st 
import random
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

st.set_page_config(layout="wide")
st.set_page_config(page_title="Mini Games! 🎮 ", page_icon=" 🧩 ", layout="wide")
st.title("Welcome to Mini-Games!! 🎮 🧩 🎲")

tab1, tab2, tab3 = st.tabs(["🎮 Game Dashboard", "📊 Analytics", "⚙️ Settings"])

# 2. Add elements inside each view using context managers
with tab1:
    st.header("Play Area")
    st.subheader("Welcome to the gaming room!")
    
    st.subheader("Choose your game: ")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("❌ Tic-tac-toe ⭕")
        st.write("A game of wit, chance and luck.")
        
        if st.button("Play Tic-tac-toe"):
            st.switch_page("views/game_1.py")
            
        # st.switch_page(r"C:\vagmi\Learn-Gen-AI\Test-jupyter\New_project\game_1.py") 

    with col2:
        st.header("🪨Rock, Paper, Scissors ✂️")
        if st.button("Play Rock, Paper, Scissors"):
            st.switch_page("views/game_2.py")
            
    with col3:
        st.header("🪨Rock, Paper, Scissors ✂️")
        if st.button("   "):
            st.title("🧩 Memory Match")

            # Initialize board assets
            icons = ["🍎", "🍌", "🍇", "🍒", "🥝", "🍉", "🍓", "🍍"] * 2

            if "cards" not in st.session_state:
                random.shuffle(icons)
                st.session_state.cards = icons
                st.session_state.revealed = [False] * 16
                st.session_state.selected = []
                st.session_state.matches = 0

            def handle_card_click(idx):
                sel = st.session_state.selected
                # Block clicks if already matched or already temporary picked
                if st.session_state.revealed[idx] or idx in sel:
                    return
                    
                if len(sel) < 2:
                    sel.append(idx)
                    
                if len(sel) == 2:
                    # Check matching indices
                    if st.session_state.cards[sel[0]] == st.session_state.cards[sel[1]]:
                        st.session_state.revealed[sel[0]] = True
                        st.session_state.revealed[sel[1]] = True
                        st.session_state.matches += 1
                        st.session_state.selected = []
                    else:
                        # Keep selected array populated so user can see their choice before resetting next click
                        pass

            # Process clearing unmatched clicks
            if len(st.session_state.selected) == 2 and st.sidebar.button("Clear Unmatched Cards"):
                st.session_state.selected = []
                st.rerun()

            # Build 4x4 Grid layout
            for row in range(4):
                cols = st.columns(4)
                for col in range(4):
                    idx = row * 4 + col
                    
                    # Decide item layout visibility
                    is_visible = st.session_state.revealed[idx] or (idx in st.session_state.selected)
                    label = st.session_state.cards[idx] if is_visible else "❓"
                    
                    if cols[col].button(label, key=f"card_{idx}", use_container_width=True):
                        if len(st.session_state.selected) == 2:
                            st.session_state.selected = [] # Auto-flush choices on next click
                        handle_card_click(idx)
                        st.rerun()

            if len(st.session_state.selected) == 2:
                st.warning("Mismatch! Click any card to hide them again.")

            if st.session_state.matches == 8:
                st.success("Congratulations! You found all pairs! 🏆")

            if st.button("Reset Board"):
                del st.session_state.cards
                st.rerun()
        
with tab2:
    st.header("High Scores & Metrics")
    # Charts or scoreboards go here

with tab3:
    st.header("Preferences")
    # Configurations go here
    st.toggle("Sound")
    st.toggle("Vibrations")


