from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def create_pdf(report_text):

    pdf_path = "research_report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph("AI Research Report", styles["Title"])
    content.append(title)

    content.append(Spacer(1, 12))

    report = Paragraph(
        report_text.replace("\n", "<br/>"),
        styles["BodyText"]
    )

    content.append(report)

    doc.build(content)

    return pdf_path