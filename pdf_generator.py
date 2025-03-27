from fpdf import FPDF
import os

def generate_pdf(destination, start_date, duration, budget, preferences, itinerary):
    """Generate a PDF file with the travel itinerary."""
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    
    # Title
    pdf.cell(200, 10, "AI-Generated Travel Itinerary", ln=True, align="C")
    pdf.ln(10)
    
    # Trip Details
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, f"📍 Destination: {destination}", ln=True)
    pdf.cell(200, 10, f"📅 Start Date: {start_date}", ln=True)
    pdf.cell(200, 10, f"⏳ Duration: {duration} days", ln=True)
    pdf.cell(200, 10, f"💰 Budget: {budget}", ln=True)
    pdf.cell(200, 10, f"🎭 Preferences: {preferences}", ln=True)
    pdf.ln(10)

    # Itinerary Content
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, itinerary)

    # Save PDF
    filename = "itinerary.pdf"
    pdf.output(filename)
    return filename
