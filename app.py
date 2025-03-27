import streamlit as st
import requests
import json
import time
import os
import google.generativeai as genai
from dotenv import load_dotenv
from tts import text_to_speech  # Ensure this function exists in tts.py

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = genai.GenerativeModel("gemini-pro") 
# Check if the API key is missing
if not GOOGLE_API_KEY:
    st.error("❌ Error: GOOGLE_API_KEY is missing. Please set it in a `.env` file.")
    st.stop()

# Initialize Google AI client
google_client = genai.Client(api_key=GOOGLE_API_KEY)

USER_HISTORY_FILE = "user_history.json"

def generate_itinerary(destination, start_date, duration, budget, preferences):
    """Generate travel itinerary using Google Gemini API."""
    prompt = f"""
    Create a detailed {duration}-day travel itinerary for {destination} starting on {start_date}. 
    The budget is {budget}, and the user prefers {preferences}. 
    Include sightseeing, activities, local food recommendations, and hidden gems.
    """
    response = google_client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text

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
        audio_file = text_to_speech(itinerary)
        if audio_file:
            st.audio(audio_file, format="audio/mp3")
        else:
            st.warning("Unable to generate audio.")
