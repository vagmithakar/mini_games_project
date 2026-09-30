import streamlit as st
import random 

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
    
if st.button("← Back to Lobby"):
    st.switch_page("views/homepage.py")