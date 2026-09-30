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
        st.header("Memory Game 🧩")
        if st.button("Play Memory game "):
            st.switch_page("views/game_3.py")
        
with tab2:
    st.header("High Scores & Metrics")
    # Charts or scoreboards go here

with tab3:
    st.header("Preferences")
    # Configurations go here

    ##backround music playing continuously, only turning off when user does so.
    if st.toggle("Sound", value=True):
        lofi_url = "https://soundhelix.com" 
        st.audio(lofi_url, format="audio/mp3", loop=True, autoplay=True)
    else:
        st.write("🔇 Music muted.")
    
    st.toggle("Vibrations")


