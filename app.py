import streamlit as st
import time
import os
import google.generativeai as genai  # ✅ Correct import
from dotenv import load_dotenv
from tts import text_to_speech  # Ensure this function exists in tts.py

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if the API key is missing
if not GOOGLE_API_KEY:
    st.error("❌ Error: GOOGLE_API_KEY is missing. Please set it in a `.env` file.")
    st.stop()

# Configure Google AI client
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini model ✅ Use a valid model
model = genai.GenerativeModel("gemini-pro")

USER_HISTORY_FILE = "user_history.json"

def generate_itinerary(destination, start_date, duration, budget, preferences):
    """Generate travel itinerary using Google Gemini API."""
    prompt = f"""
    Create a detailed {duration}-day travel itinerary for {destination} starting on {start_date}. 
    The budget is {budget}, and the user prefers {preferences}. 
    Include sightseeing, activities, local food recommendations, and hidden gems.
    """

    try:
        response = model.generate_content([prompt])  # ✅ Correct usage
        return response.text if response and hasattr(response, 'text') else "⚠️ Unable to generate itinerary."
    except Exception as e:
        return f"❌ API Error: {e}"

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
    with st.spinner("Generating your
