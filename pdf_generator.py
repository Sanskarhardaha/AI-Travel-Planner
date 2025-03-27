from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(destination, start_date, duration, budget, preferences, itinerary):
    """Generate a PDF file with travel itinerary using ReportLab (supports Unicode)."""
    
    filename = "itinerary.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Set title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "AI-Generated Travel Itinerary")

    # Move to next line
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"📍 Destination: {destination}")
    c.drawString(100, 700, f"📅 Start Date: {start_date}")
    c.drawString(100, 680, f"⏳ Duration: {duration} days")
    c.drawString(100, 660, f"💰 Budget: {budget}")
    c.drawString(100, 640, f"🎭 Preferences: {preferences}")

    # Add itinerary content
    text = c.beginText(100, 600)
    text.setFont("Helvetica", 12)
    
    # Wrap text for readability
    itinerary_lines = itinerary.split("\n")
    for line in itinerary_lines:
        text.textLine(line)

    c.drawText(text)

    # Save the PDF
    c.save()
    
    return filename
