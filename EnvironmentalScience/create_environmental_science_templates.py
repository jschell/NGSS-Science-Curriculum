#!/usr/bin/env python3
"""
Environmental & Sustainability Education PDF Template Generator
Creates 10 professional PDF templates for 3rd Grade NGSS Environmental Science projects

Templates Created:
Project 1 (Sustainability Research):
1. Project1_Source_Tracking.pdf
2. Project1_Perspective_Analysis.pdf

Project 2 (Home Grounds Investigation):
3. Project2_Investigation_Plan.pdf
4. Project2_Data_Collection.pdf
5. Project2_Data_Graphs.pdf
6. Project2_Data_Analysis.pdf

Project 3 (Personal Action):
7. Project3_Action_Research.pdf
8. Project3_Action_Plan.pdf
9. Project3_Progress_Tracker.pdf
10. Project3_Results_Summary.pdf

Requirements: pip install reportlab
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_header(c, title, project_info):
    """Create consistent header for all templates"""
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, 10.5*inch, title)

    # Project info
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 10.2*inch, project_info)

    # Name and Date fields
    c.setFont("Helvetica", 11)
    c.drawString(1*inch, 9.9*inch, "Name: ________________________")
    c.drawString(5*inch, 9.9*inch, "Date: ____________")

    # Separator line
    c.line(0.75*inch, 9.75*inch, 7.75*inch, 9.75*inch)

    return 9.5*inch  # Return y-position for content start


# =============================================================================
# PROJECT 1: SUSTAINABILITY RESEARCH
# =============================================================================

def template1_source_tracking():
    """Project 1: Source Tracking Template (for multiple sources)"""
    filename = "Project1_Source_Tracking.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Environmental Research - Source Tracking",
                     "Project 1: Sustainability Research | Standard 3.ESE.1-1")

    # Instructions
    y -= 0.3*inch
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, y, "Use this sheet to track each source you use. Complete one per source (aim for at least 5 total).")

    # Source tracking template (repeat 2 times per page)
    for source_num in range(1, 3):
        y -= 0.4*inch

        # Source number
        c.setFont("Helvetica-Bold", 14)
        c.drawString(1*inch, y, f"SOURCE #{source_num}")

        c.setFont("Helvetica", 11)
        y -= 0.3*inch
        c.drawString(1.2*inch, y, "Title: _________________________________________________________________")

        y -= 0.25*inch
        c.drawString(1.2*inch, y, "Author or Organization: _______________________________________________")

        y -= 0.25*inch
        c.drawString(1.2*inch, y, "Type: (circle one)    Website    Book    Article    Video    Interview    Other")

        y -= 0.25*inch
        c.drawString(1.2*inch, y, "Link or Location: ____________________________________________________")

        y -= 0.25*inch
        c.drawString(1.2*inch, y, "Date accessed or published: _________________________________________")

        y -= 0.3*inch
        c.setFont("Helvetica-Bold", 11)
        c.drawString(1.2*inch, y, "What I learned from this source:")

        c.setFont("Helvetica", 10)
        y -= 0.05*inch
        c.line(1.2*inch, y, 7.5*inch, y)
        y -= 0.2*inch
        c.line(1.2*inch, y, 7.5*inch, y)
        y -= 0.2*inch
        c.line(1.2*inch, y, 7.5*inch, y)

        y -= 0.25*inch
        c.setFont("Helvetica-Bold", 11)
        c.drawString(1.2*inch, y, "Which perspective does this represent? (circle all that apply)")

        c.setFont("Helvetica", 11)
        y -= 0.25*inch
        c.drawString(1.4*inch, y, "Individual    Community    Tribal/Indigenous    Scientific    Other: __________")

        # Separator line
        y -= 0.15*inch
        c.setStrokeColorRGB(0.5, 0.5, 0.5)
        c.line(1*inch, y, 7.5*inch, y)
        c.setStrokeColorRGB(0, 0, 0)

    c.save()
    print(f"Created: {filename}")


def template2_perspective_analysis():
    """Project 1: Perspective Analysis and Comparison"""
    filename = "Project1_Perspective_Analysis.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Perspective Analysis & Comparison",
                     "Project 1: Sustainability Research | Standard 3.ESE.1-1")

    # Topic
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "My Topic:")
    c.setFont("Helvetica", 11)
    c.drawString(2*inch, y, "___________________________________________________")

    # Comparison questions
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "PERSPECTIVE COMPARISON")

    # Question 1
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Question: What does each perspective value most?")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Individual perspective values:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Community perspective values:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Tribal/Indigenous perspective values:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    # Question 2
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Question: What solutions does each perspective offer?")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Individual solutions:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Community solutions:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Tribal/Indigenous solutions:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    # Question 3
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Question: What are the challenges for each perspective?")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Individual challenges:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Community challenges:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Tribal/Indigenous challenges:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    # Analysis section
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "WHAT I NOTICED")

    c.setFont("Helvetica-Bold", 11)
    y -= 0.3*inch
    c.drawString(1*inch, y, "Similarities across perspectives:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.setFont("Helvetica-Bold", 11)
    y -= 0.3*inch
    c.drawString(1*inch, y, "Differences I found:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.setFont("Helvetica-Bold", 11)
    y -= 0.3*inch
    c.drawString(1*inch, y, "Why these differences might exist:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.save()
    print(f"Created: {filename}")


# =============================================================================
# PROJECT 2: HOME GROUNDS INVESTIGATION
# =============================================================================

def template3_investigation_plan():
    """Project 2: Investigation Planning Template"""
    filename = "Project2_Investigation_Plan.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Environmental Investigation Plan",
                     "Project 2: Home Grounds Investigation | Standard 3.ESE.1-2")

    # Focus area
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "My Environmental Focus: (circle one)")
    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Water Quality        Air Quality        Biodiversity        Waste Management")

    # Investigation question
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "MY INVESTIGATION QUESTION")

    c.setFont("Helvetica", 11)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # What I will observe/measure
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "WHAT I WILL OBSERVE OR MEASURE")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Where
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "WHERE I WILL COLLECT DATA")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Location 1: __________________________________________________________")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Location 2: __________________________________________________________")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Location 3: __________________________________________________________")

    # When
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "WHEN I WILL COLLECT DATA")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "How often? (circle one)    Daily    Every other day    Twice/week    Weekly")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "How many total days? __________    Start date: __________   End date: __________")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "What time of day? _____________________________________________________")

    # Tools
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "TOOLS I WILL USE")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Recording
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "HOW I WILL RECORD DATA")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Comparison
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "WHAT I WILL COMPARE")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Prediction
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "MY PREDICTION")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "I predict I will find:")
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.save()
    print(f"Created: {filename}")


def template4_data_collection():
    """Project 2: Data Collection Sheet (customizable)"""
    filename = "Project2_Data_Collection.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Data Collection Sheet",
                     "Project 2: Home Grounds Investigation | Standard 3.ESE.1-2")

    # Instructions
    y -= 0.3*inch
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(1*inch, y, "Use this sheet to record observations each time you collect data. Make copies as needed.")

    # Observation details
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Date: ___________")
    c.drawString(2.5*inch, y, "Time: ___________")
    c.drawString(4.5*inch, y, "Weather: ___________________")

    y -= 0.25*inch
    c.drawString(1*inch, y, "Location: _________________________________________________________________")

    # Main observation area
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "OBSERVATIONS")

    # Create a large box for observations
    y -= 0.2*inch
    box_height = 3.5*inch
    c.rect(1*inch, y - box_height, 6.5*inch, box_height)

    # Grid lines in box
    c.setStrokeColorRGB(0.8, 0.8, 0.8)
    for i in range(1, 14):
        line_y = y - (i * box_height / 14)
        c.line(1*inch, line_y, 7.5*inch, line_y)
    c.setStrokeColorRGB(0, 0, 0)

    # Measurements section
    y -= box_height + 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "MEASUREMENTS (if applicable):")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "____________: ________    ____________: ________    ____________: ________")

    # Notes section
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "NOTES / QUESTIONS:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Drawing/photo space
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "SKETCH OR PASTE PHOTO:")

    y -= 0.15*inch
    c.rect(1*inch, y - 1.2*inch, 6.5*inch, 1.2*inch)

    c.save()
    print(f"Created: {filename}")


def template5_data_graphs():
    """Project 2: Graph Templates for Data Visualization"""
    filename = "Project2_Data_Graphs.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Data Graphs and Charts",
                     "Project 2: Home Grounds Investigation | Standard 3.ESE.1-2")

    # Graph 1: Bar graph
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "GRAPH 1: BAR GRAPH")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Title: ____________________________________________________________________")

    # Bar graph grid
    y -= 0.4*inch
    graph_left = 1.5*inch
    graph_bottom = y - 2.5*inch
    graph_width = 5*inch
    graph_height = 2.5*inch

    # Y-axis label
    c.setFont("Helvetica-Bold", 10)
    c.saveState()
    c.translate(0.8*inch, graph_bottom + graph_height/2)
    c.rotate(90)
    c.drawCentredString(0, 0, "Amount/Count")
    c.restoreState()

    # X-axis label
    c.drawCentredString(graph_left + graph_width/2, graph_bottom - 0.5*inch, "Categories")

    # Grid
    c.setStrokeColorRGB(0.8, 0.8, 0.8)
    for i in range(11):
        y_pos = graph_bottom + (i * graph_height / 10)
        c.line(graph_left, y_pos, graph_left + graph_width, y_pos)
    c.setStrokeColorRGB(0, 0, 0)

    # Axes
    c.setLineWidth(2)
    c.line(graph_left, graph_bottom, graph_left + graph_width, graph_bottom)
    c.line(graph_left, graph_bottom, graph_left, graph_bottom + graph_height)
    c.setLineWidth(1)

    # Graph 2: Line graph on second page
    c.showPage()
    y = create_header(c, "Data Graphs and Charts (continued)",
                     "Project 2: Home Grounds Investigation")

    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "GRAPH 2: LINE GRAPH (for change over time)")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Title: ____________________________________________________________________")

    # Line graph grid
    y -= 0.4*inch
    graph_bottom = y - 2.5*inch

    # Y-axis label
    c.setFont("Helvetica-Bold", 10)
    c.saveState()
    c.translate(0.8*inch, graph_bottom + graph_height/2)
    c.rotate(90)
    c.drawCentredString(0, 0, "Measurement")
    c.restoreState()

    # X-axis label
    c.drawCentredString(graph_left + graph_width/2, graph_bottom - 0.5*inch, "Time (Day/Week)")

    # Grid
    c.setStrokeColorRGB(0.8, 0.8, 0.8)
    for i in range(11):
        y_pos = graph_bottom + (i * graph_height / 10)
        c.line(graph_left, y_pos, graph_left + graph_width, y_pos)
    for i in range(11):
        x_pos = graph_left + (i * graph_width / 10)
        c.line(x_pos, graph_bottom, x_pos, graph_bottom + graph_height)
    c.setStrokeColorRGB(0, 0, 0)

    # Axes
    c.setLineWidth(2)
    c.line(graph_left, graph_bottom, graph_left + graph_width, graph_bottom)
    c.line(graph_left, graph_bottom, graph_left, graph_bottom + graph_height)
    c.setLineWidth(1)

    c.save()
    print(f"Created: {filename}")


def template6_data_analysis():
    """Project 2: Data Analysis and Conclusions"""
    filename = "Project2_Data_Analysis.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Data Analysis and Environmental Impact",
                     "Project 2: Home Grounds Investigation | Standard 3.ESE.1-2")

    # Investigation question review
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "MY INVESTIGATION QUESTION WAS:")

    c.setFont("Helvetica", 11)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Answer
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "WHAT I FOUND (Answer to my question):")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Evidence
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "EVIDENCE FROM MY DATA:")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "1. ____________________________________________________________________")
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1*inch, y, "2. ____________________________________________________________________")
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1*inch, y, "3. ____________________________________________________________________")
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    # Patterns
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "PATTERNS I NOTICED:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Environmental Impact Analysis
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, y, "ENVIRONMENTAL IMPACT ANALYSIS")

    # Things that helped
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "Things that HELPED environmental quality:")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")

    # Things that hurt
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "Things that HURT environmental quality:")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")

    # Built environment effect
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "The built environment (buildings, pavement, structures):")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Natural features effect
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Natural features (plants, soil, natural areas):")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.save()
    print(f"Created: {filename}")


# =============================================================================
# PROJECT 3: PERSONAL ACTION
# =============================================================================

def template7_action_research():
    """Project 3: Action Research Template"""
    filename = "Project3_Action_Research.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Environmental Action Research",
                     "Project 3: Personal Action | Standard 3.ESE.1-3")

    # Action area
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "My Action Area:")
    c.setFont("Helvetica", 11)
    c.drawString(2.5*inch, y, "___________________________________________________")

    # Individual actions
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "INDIVIDUAL ACTIONS - What can ONE person do?")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "1. ____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1*inch, y, "2. ____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1*inch, y, "3. ____________________________________________________________________")

    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "How much impact can individual actions have?")
    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Community actions
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "COMMUNITY ACTIONS - What are groups/organizations doing?")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "1. ____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1*inch, y, "2. ____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1*inch, y, "3. ____________________________________________________________________")

    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "How can individuals support community efforts?")
    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Examples of success
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "EXAMPLES OF SUCCESS (especially kids taking action)")

    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Example 1:")

    c.setFont("Helvetica", 10)
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "Who: __________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "What they did: ________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "Impact: _______________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "Source: _______________________________________________________________")

    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Example 2:")

    c.setFont("Helvetica", 10)
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "Who: __________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "What they did: ________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "Impact: _______________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "Source: _______________________________________________________________")

    c.save()
    print(f"Created: {filename}")


def template8_action_plan():
    """Project 3: Personal Action Plan"""
    filename = "Project3_Action_Plan.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Personal Environmental Action Plan",
                     "Project 3: Personal Action | Standard 3.ESE.1-3")

    # Goal
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "MY ENVIRONMENTAL GOAL:")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "In the next _______ weeks, I will:")
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Specific actions
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "SPECIFIC ACTIONS I WILL TAKE:")

    c.setFont("Helvetica-Bold", 11)
    y -= 0.3*inch
    c.drawString(1*inch, y, "Daily Actions (things I'll do every day):")

    c.setFont("Helvetica", 10)
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")

    c.setFont("Helvetica-Bold", 11)
    y -= 0.3*inch
    c.drawString(1*inch, y, "Weekly Actions (things I'll do each week):")

    c.setFont("Helvetica", 10)
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")

    c.setFont("Helvetica-Bold", 11)
    y -= 0.3*inch
    c.drawString(1*inch, y, "One-Time Actions:")

    c.setFont("Helvetica", 10)
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")

    # What I need
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "WHAT I NEED:")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Materials/tools: ______________________________________________________")

    y -= 0.25*inch
    c.drawString(1*inch, y, "Help from family: _____________________________________________________")

    y -= 0.25*inch
    c.drawString(1*inch, y, "Time required: _______ minutes per day  /  _______ hours per week")

    # Tracking
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "HOW I'LL TRACK PROGRESS:")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "What I'll measure: ____________________________________________________")

    y -= 0.25*inch
    c.drawString(1*inch, y, "How I'll measure it: __________________________________________________")

    y -= 0.25*inch
    c.drawString(1*inch, y, "How often I'll check: _________________________________________________")

    # Success criteria
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "SUCCESS CRITERIA - I'll know my action is successful if:")

    c.setFont("Helvetica", 10)
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")
    y -= 0.2*inch
    c.drawString(1.2*inch, y, "• _____________________________________________________________________")

    # Challenges
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "CHALLENGES I MIGHT FACE:")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Possible problem: _____________________________________________________")
    y -= 0.2*inch
    c.drawString(1*inch, y, "Solution: _____________________________________________________________")

    y -= 0.25*inch
    c.drawString(1*inch, y, "Possible problem: _____________________________________________________")
    y -= 0.2*inch
    c.drawString(1*inch, y, "Solution: _____________________________________________________________")

    # Dates
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "START DATE: _______________        PLANNED END DATE: _______________")

    c.save()
    print(f"Created: {filename}")


def template9_progress_tracker():
    """Project 3: Weekly Progress Tracking Log"""
    filename = "Project3_Progress_Tracker.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Weekly Progress Log",
                     "Project 3: Personal Action | Standard 3.ESE.1-3")

    # Week info
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "Week #: _______")
    c.drawString(3*inch, y, "Dates: _______________ to _______________")

    # Daily actions checklist
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "DAILY ACTIONS COMPLETED:")

    c.setFont("Helvetica", 10)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in days:
        y -= 0.25*inch
        c.drawString(1*inch, y, f"{day}:  ☐ Action 1   ☐ Action 2   ☐ Action 3")

    # Weekly actions
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "WEEKLY ACTIONS COMPLETED:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Data collected
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "DATA COLLECTED THIS WEEK:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Challenges
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "CHALLENGES THIS WEEK:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Successes
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "SUCCESSES THIS WEEK:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Feeling
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "HOW I FELT ABOUT MY ACTION THIS WEEK:")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "😊 Great      😐 Okay      ☹ Difficult      (circle one)")

    # Notes
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "NOTES:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.save()
    print(f"Created: {filename}")


def template10_results_summary():
    """Project 3: Final Results Summary"""
    filename = "Project3_Results_Summary.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Action Project Results Summary",
                     "Project 3: Personal Action | Standard 3.ESE.1-3")

    # Goal review
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "MY GOAL WAS:")

    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Duration
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Duration: _______ weeks (from ____________ to ____________)")

    # Quantitative results
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "QUANTITATIVE RESULTS (Numbers/Data):")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Total impact:")
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, y, "Create graph or table below showing your weekly progress:")

    # Space for graph
    y -= 0.2*inch
    graph_height = 2*inch
    c.rect(1*inch, y - graph_height, 6.5*inch, graph_height)

    # Qualitative results
    y -= graph_height + 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "QUALITATIVE RESULTS (Observations/Experiences):")

    c.setFont("Helvetica-Bold", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Changes I noticed:")
    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.setFont("Helvetica-Bold", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Challenges faced:")
    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.setFont("Helvetica-Bold", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Unexpected outcomes:")
    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.setFont("Helvetica-Bold", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Family/community response:")
    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)

    # Success evaluation
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "DID I MEET MY GOAL?")

    c.setFont("Helvetica", 11)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "☐ Yes, completely      ☐ Mostly      ☐ Partially      ☐ No")

    c.setFont("Helvetica-Bold", 11)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Why or why not?")
    c.setFont("Helvetica", 10)
    y -= 0.05*inch
    c.line(1*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.save()
    print(f"Created: {filename}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Generate all Environmental Science PDF templates"""
    print("Generating Environmental & Sustainability Education PDF Templates...")
    print("=" * 70)

    # Project 1: Sustainability Research
    print("\nProject 1: Environmental Sustainability Research")
    print("-" * 70)
    template1_source_tracking()
    template2_perspective_analysis()

    # Project 2: Home Grounds Investigation
    print("\nProject 2: Home Grounds Environmental Investigation")
    print("-" * 70)
    template3_investigation_plan()
    template4_data_collection()
    template5_data_graphs()
    template6_data_analysis()

    # Project 3: Personal Action
    print("\nProject 3: Personal Action and Civic Responsibility")
    print("-" * 70)
    template7_action_research()
    template8_action_plan()
    template9_progress_tracker()
    template10_results_summary()

    print("\n" + "=" * 70)
    print("✓ All 10 Environmental Science templates created successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
