import streamlit as st
import time
import os
import google.generativeai as genai
from dotenv import load_dotenv
import pyttsx3  # Offline Text-to-Speech

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check API Key
if not GOOGLE_API_KEY:
    st.error("❌ Error: GOOGLE_API_KEY is missing. Please set it in a `.env` file.")
    st.stop()

# Configure Gemini AI
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

USER_HISTORY_FILE = "user_history.json"

def generate_itinerary(destination, start_date, duration, budget, preferences):
    """Generate travel itinerary using Google Gemini API."""
    prompt = f"""
    Create a detailed {duration}-day travel itinerary for {destination} starting on {start_date}. 
    The budget is {budget}, and the user prefers {preferences}. 
    Include sightseeing, activities, local food recommendations, and hidden gems.
    """

    try:
        response = model.generate_content([prompt])  
        return response.text if response and hasattr(response, 'text') else "⚠️ Unable to generate itinerary."
    except Exception as e:
        return f"❌ API Error: {e}"

def text_to_speech_offline(text, filename="itinerary.mp3"):
    """Convert text to speech using offline pyttsx3."""
    try:
        engine = pyttsx3.init()
        engine.save_to_file(text, filename)
        engine.runAndWait()
        return filename  # Return saved audio file
    except Exception as e:
        st.error(f"❌ Text-to-Speech Error: {e}")
        return None

# Streamlit UI
st.set_page_config(page_title="AI Travel Planner", layout="wide")

st.title("🌍 AI-Powered Travel Planner")
st.write("Plan your trip effortlessly with AI-driven recommendations!")

# User inputs
destination = st.text_input("🌆 Destination", "Paris")
start_date = st.date_input("📅 Start Date")
duration = st.number_input("⏳ Trip Duration (Days)", min_value=1, max_value=30, value=5)
budget = st.selectbox("💰 Budget", ["Low", "Medium", "High"])
preferences = st.text_area("🎭 Preferences", "Culture, Sightseeing, Local Food")

# Generate itinerary button
if st.button("🚀 Generate Itinerary"):
    with st.spinner("Generating your personalized itinerary..."):
        itinerary = generate_itinerary(destination, start_date, duration, budget, preferences)
        time.sleep(2)
        st.subheader("📜 Your Itinerary")
        st.write(itinerary)

        # Convert itinerary to speech
        st.subheader("🔊 Listen to Your Itinerary")
        
        if not itinerary.strip():
            st.warning("⚠️ Generated itinerary is empty. No audio to generate.")
        else:
            audio_file = text_to_speech_offline(itinerary)

            if audio_file and os.path.exists(audio_file):
                st.audio(audio_file, format="audio/mp3")
            else:
                st.warning("❌ Error: Unable to generate audio.")
