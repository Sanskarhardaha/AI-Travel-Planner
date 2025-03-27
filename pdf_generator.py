from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        """Add a header to the PDF."""
        self.set_font("Arial", style="B", size=16)
        self.cell(200, 10, "AI-Generated Travel Itinerary", ln=True, align="C")
        self.ln(10)

def generate_pdf(destination, start_date, duration, budget, preferences, itinerary):
    """Generate a PDF file with the travel itinerary and handle Unicode encoding issues."""

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set font to DejaVu (supports Unicode) or Arial if unavailable
    try:
        pdf.add_font("DejaVu", "", "DejaVuSansCondensed.ttf", uni=True)
        pdf.set_font("DejaVu", size=12)
    except:
        pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, f"📍 Destination: {destination}", ln=True)
    pdf.cell(200, 10, f"📅 Start Date: {start_date}", ln=True)
    pdf.cell(200, 10, f"⏳ Duration: {duration} days", ln=True)
    pdf.cell(200, 10, f"💰 Budget: {budget}", ln=True)
    pdf.cell(200, 10, f"🎭 Preferences: {preferences}", ln=True)
    pdf.ln(10)

    # Handle special characters in the itinerary
    safe_text = itinerary.encode("latin-1", "replace").decode("latin-1")

    # Itinerary Content
    pdf.multi_cell(0, 10, safe_text)

    # Save PDF
    filename = "itinerary.pdf"
    pdf.output(filename, "F")
    return filename
