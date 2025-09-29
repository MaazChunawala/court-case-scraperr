from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf(result):
    os.makedirs("data/downloads", exist_ok=True)
    pdf_path = "data/downloads/case_details.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    y = 750
    c.drawString(50, y, "Case Details")
    y -= 30
    for key, value in result.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 20

    c.save()
    return pdf_path