import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Merry Christmas!",
    page_icon="🎄",
    layout="centered"
)

# --- NEW FUNCTION TO PLAY SOUND ---
def play_sound(audio_url):
    """
    Injects a hidden HTML audio player that works on the next re-run.
    Browsers usually allow this because the user has just clicked a button.
    """
    st.markdown(f"""
        <audio autoplay style="display:none;">
            <source src="{audio_url}" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

# 2. Custom CSS
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-image: url("https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSEsP7JBMsA_kB-OcsvQuIL6mg6h0Cuu0IaCbJu4o9szCvEE9LfnDpiOzPf9MLG-VkluhnlSqmAFDVIuy8");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* Fix the top header strip */
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0); 
    }
    
    /* Card Container */
    .block-container {
        background-color: rgba(255, 255, 255, 0.90);
        padding: 3rem !important;
        border-radius: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        max-width: 700px;
        margin-top: 50px;
    }
    
    /* Text Styling */
    h1 { color: #D42426; text-align: center; font-family: 'Helvetica Neue', sans-serif; }
    p { color: #2F4F4F; font-size: 1.2rem; text-align: center; }
    
    /* Standard Button Styling (for the reset button later) */
    .stButton > button {
        background-color: #D42426;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State Management
if 'gift_opened' not in st.session_state:
    st.session_state.gift_opened = False

# --- NEW: Initialize the Belly Wash Counter ---
if 'wash_count' not in st.session_state:
    st.session_state.wash_count = 0

# New state to track if we need to play a sound on this specific run
if 'sound_to_play' not in st.session_state:
    st.session_state.sound_to_play = None

# 4. Sound Logic Handler
# This checks if a sound was queued from the PREVIOUS click and plays it now
if st.session_state.sound_to_play:
    play_sound(st.session_state.sound_to_play)
    st.session_state.sound_to_play = None # Reset so it doesn't loop

# 4. The Card Content
st.title("🎄 Merry Christmas! 🎄")
st.write("To Aimee and also Patrick,")
st.write("Your days are numbered.")

st.markdown("---")

# 5. The Interaction
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Only show the "Game" if gift hasn't been opened
    if not st.session_state.gift_opened:
        
        # Define your messages based on clicks
        msgs = [
            "Rub his belly to open!", 
            "Ohhhh Yeah again!", 
            "One more Time!!", 
        ]
        
        # Pick the message based on current count (safeguard index with min)
        current_msg = msgs[min(st.session_state.wash_count, len(msgs)-1)]
        
        # Display the dynamic text
        st.markdown(f"<h3 style='text-align: center; color: #D42426;'>{current_msg}</h3>", unsafe_allow_html=True)

        # --- CSS FOR THE BELLY BUTTON ---
        st.markdown("""
            <style>
            /* Specific targeting for the belly button */
            div.stButton > button:first-child {
                background-image: url("https://i.pinimg.com/236x/c8/a6/b4/c8a6b40052b20e30b63dafd6a904b8da.jpg");
                background-size: cover;
                background-position: center;
                background-color: transparent;
                border: none;
                
                /* FORCE DIMENSIONS */
                height: 250px !important;
                min-height: 250px !important; 
                width: 100% !important;
                border-radius: 20px;
                
                /* Remove default padding so the image fills the space */
                padding: 0 !important;
                transition: transform 0.1s;
            }

            /* HIDE TEXT (But keep structure so it doesn't collapse) */
            div.stButton > button:first-child p { 
                color: transparent !important;
            }
            
            /* Make it pulse on hover */
            div.stButton > button:hover {
                background-color: transparent;
                transform: scale(1.05);
                box-shadow: 0px 0px 20px rgba(255,255,255,0.8);
            }
            
            /* Make it shrink slightly on click */
            div.stButton > button:active {
                transform: scale(0.95);
            }
            </style>
        """, unsafe_allow_html=True)
        # THE LOGIC
        if st.button("BELLY_BUTTON"):
            # Increment the counter in session state
            st.session_state.wash_count += 1
            
            
            # If they have clicked 3 times, open the gift
            if st.session_state.wash_count >= 3:
                st.session_state.gift_opened = True
            
            st.rerun() # Refresh to show new text or open gift

# 6. The Reveal Logic
if st.session_state.gift_opened:
    with st.spinner("Washing..."):
        time.sleep(1.5)
    
    st.snow()
    
    st.markdown("""
    <div style="display: flex; justify-content: center;">
        <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW9iMGVibmVpanZrb3I3c3M1OHhuY2JkeGxjMjU4OWk5d2hhZ2pzMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/m8fyrgnXwXV5EHw6Lm/giphy.gif" width="300" style="border-radius: 15px; box-shadow: 0px 0px 15px white;">
    </div>
    <br>
    """, unsafe_allow_html=True)
    
    st.success("You've received €50 to spend on whatever the fuck!")

    # Reset Button
    if st.button("Wash his belly again!"):
        st.session_state.gift_opened = False
        st.session_state.wash_count = 0 # Reset the belly rubs too!
        st.rerun()

