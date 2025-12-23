#!/usr/bin/env python3
"""
Earth Science PDF Template Generator
Creates 8 professional PDF templates for 3rd Grade NGSS Earth Science investigations

Templates Created:
Section 1 (Weather Patterns):
1. Section1_Daily_Weather_Log.pdf
2. Section1_Temperature_Graph.pdf
3. Section1_Precipitation_Graph.pdf

Section 2 (Climate Regions):
4. Section2_Climate_Profile.pdf
5. Section2_Climate_Comparison.pdf
6. Section2_World_Climate_Map.pdf

Section 3 (Weather Hazards):
7. Section3_Hazard_Analysis.pdf
8. Section3_Solution_Evaluation.pdf

Requirements: pip install reportlab
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_header(c, title, section_info):
    """Create consistent header for all templates"""
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, 10.5*inch, title)

    # Section info
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 10.2*inch, section_info)

    # Name and Date fields
    c.setFont("Helvetica", 11)
    c.drawString(1*inch, 9.9*inch, "Name: ________________________")
    c.drawString(5*inch, 9.9*inch, "Date: ____________")

    # Separator line
    c.line(0.75*inch, 9.75*inch, 7.75*inch, 9.75*inch)

    return 9.5*inch  # Return y-position for content start


# =============================================================================
# SECTION 1: WEATHER PATTERNS
# =============================================================================

def template1_daily_weather_log():
    """Section 1: Daily Weather Observation Log for 2-4 weeks"""
    filename = "Section1_Daily_Weather_Log.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Daily Weather Observation Log",
                     "Section 1: Weather Patterns | Standard 3-ESS2-1")

    # Instructions
    c.setFont("Helvetica", 10)
    y -= 0.3*inch
    c.drawString(1*inch, y, "Instructions: Observe and record weather at the SAME TIME each day for 2-4 weeks.")

    # Location field
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Location:")
    c.setFont("Helvetica", 11)
    c.drawString(1.8*inch, y, "_______________________________")

    # Observation time
    c.setFont("Helvetica-Bold", 11)
    c.drawString(4.5*inch, y, "Observation Time:")
    c.setFont("Helvetica", 11)
    c.drawString(5.9*inch, y, "_____________")

    # Data table header
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 10)

    # Column headers
    col1_x = 0.75*inch  # Date
    col2_x = 1.5*inch   # Temp
    col3_x = 2.4*inch   # Precipitation
    col4_x = 3.8*inch   # Wind
    col5_x = 5*inch     # Sky/Clouds
    col6_x = 6.2*inch   # Notes

    c.drawString(col1_x, y, "Date")
    c.drawString(col2_x, y, "Temp")
    c.drawString(col3_x, y, "Precipitation")
    c.drawString(col4_x, y, "Wind")
    c.drawString(col5_x, y, "Sky/Clouds")
    c.drawString(col6_x, y, "Notes")

    y -= 0.05*inch
    c.line(0.7*inch, y, 7.8*inch, y)  # Header underline

    # Data rows (28 rows for 4 weeks)
    c.setFont("Helvetica", 9)
    row_height = 0.25*inch

    for i in range(28):
        y -= row_height
        if y < 1*inch:  # Check if need new page
            c.showPage()
            y = create_header(c, "Daily Weather Observation Log (continued)",
                            "Section 1: Weather Patterns")
            y -= 0.3*inch
            c.setFont("Helvetica", 9)

        # Draw row lines
        c.line(0.7*inch, y, 7.8*inch, y)

        # Vertical lines for columns
        c.line(col1_x, y, col1_x, y + row_height)
        c.line(col2_x, y, col2_x, y + row_height)
        c.line(col3_x, y, col3_x, y + row_height)
        c.line(col4_x, y, col4_x, y + row_height)
        c.line(col5_x, y, col5_x, y + row_height)
        c.line(col6_x, y, col6_x, y + row_height)

    # Close outer borders
    c.line(0.7*inch, 9.3*inch, 0.7*inch, y)  # Left border (adjust top as needed)
    c.line(7.8*inch, 9.3*inch, 7.8*inch, y)  # Right border

    c.save()
    print(f"Created: {filename}")


def template2_temperature_graph():
    """Section 1: Temperature Line Graph Template"""
    filename = "Section1_Temperature_Graph.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Temperature Over Time - Line Graph",
                     "Section 1: Weather Patterns | Standard 3-ESS2-1")

    # Title field
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Graph Title:")
    c.setFont("Helvetica", 11)
    c.drawString(2*inch, y, "_____________________________________________")

    # Graph area
    y -= 0.5*inch
    graph_left = 1.5*inch
    graph_bottom = 2*inch
    graph_width = 5.5*inch
    graph_height = 4.5*inch

    # Y-axis label (vertical)
    c.setFont("Helvetica-Bold", 10)
    c.saveState()
    c.translate(0.8*inch, graph_bottom + graph_height/2)
    c.rotate(90)
    c.drawCentredString(0, 0, "Temperature (°F)")
    c.restoreState()

    # X-axis label
    c.drawCentredString(graph_left + graph_width/2, graph_bottom - 0.4*inch, "Date")

    # Draw graph grid
    c.setStrokeColorRGB(0.8, 0.8, 0.8)

    # Horizontal grid lines (10 lines)
    for i in range(11):
        y_pos = graph_bottom + (i * graph_height / 10)
        c.line(graph_left, y_pos, graph_left + graph_width, y_pos)

    # Vertical grid lines (14 lines for days)
    for i in range(15):
        x_pos = graph_left + (i * graph_width / 14)
        c.line(x_pos, graph_bottom, x_pos, graph_bottom + graph_height)

    # Draw axes (bold)
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(2)
    c.line(graph_left, graph_bottom, graph_left + graph_width, graph_bottom)  # X-axis
    c.line(graph_left, graph_bottom, graph_left, graph_bottom + graph_height)  # Y-axis
    c.setLineWidth(1)

    # Analysis section
    y = graph_bottom - 0.8*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Pattern Analysis:")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Warmest temperature: _______°F    Date: ___________")

    y -= 0.2*inch
    c.drawString(1*inch, y, "Coldest temperature: _______°F    Date: ___________")

    y -= 0.2*inch
    c.drawString(1*inch, y, "Overall pattern:")
    c.line(1*inch, y - 0.05*inch, 7.5*inch, y - 0.05*inch)
    y -= 0.2*inch
    c.line(1*inch, y, 7.5*inch, y)

    c.save()
    print(f"Created: {filename}")


def template3_precipitation_graph():
    """Section 1: Precipitation Bar Graph Template"""
    filename = "Section1_Precipitation_Graph.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Types of Weather Days - Bar Graph",
                     "Section 1: Weather Patterns | Standard 3-ESS2-1")

    # Title field
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Graph Title:")
    c.setFont("Helvetica", 11)
    c.drawString(2*inch, y, "_____________________________________________")

    # Tally section
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "First, Count Your Days:")

    c.setFont("Helvetica", 10)
    y -= 0.3*inch
    c.drawString(1.2*inch, y, "☀  Sunny (no precipitation): _______ days")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "🌧  Rainy: _______ days")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "❄  Snowy: _______ days")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "⚡ Other (sleet, hail, etc.): _______ days")

    # Graph area
    y -= 0.6*inch
    graph_left = 1.5*inch
    graph_bottom = 2.2*inch
    graph_width = 5.5*inch
    graph_height = 4*inch

    # Y-axis label
    c.setFont("Helvetica-Bold", 10)
    c.saveState()
    c.translate(0.7*inch, graph_bottom + graph_height/2)
    c.rotate(90)
    c.drawCentredString(0, 0, "Number of Days")
    c.restoreState()

    # X-axis label
    c.drawCentredString(graph_left + graph_width/2, graph_bottom - 0.5*inch, "Weather Type")

    # Draw graph grid
    c.setStrokeColorRGB(0.8, 0.8, 0.8)

    # Horizontal lines
    for i in range(11):
        y_pos = graph_bottom + (i * graph_height / 10)
        c.line(graph_left, y_pos, graph_left + graph_width, y_pos)

    # Draw axes
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(2)
    c.line(graph_left, graph_bottom, graph_left + graph_width, graph_bottom)
    c.line(graph_left, graph_bottom, graph_left, graph_bottom + graph_height)
    c.setLineWidth(1)

    # X-axis category labels
    c.setFont("Helvetica", 9)
    bar_width = graph_width / 4
    categories = ["Sunny", "Rainy", "Snowy", "Other"]
    for i, cat in enumerate(categories):
        x_pos = graph_left + (i * bar_width) + (bar_width / 2)
        c.drawCentredString(x_pos, graph_bottom - 0.25*inch, cat)

    # Analysis
    y = graph_bottom - 0.9*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Pattern Analysis:")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Most common weather type: _______________________")
    y -= 0.2*inch
    c.drawString(1*inch, y, "Does this match the season? Why? ______________________________________________")

    c.save()
    print(f"Created: {filename}")


# =============================================================================
# SECTION 2: CLIMATE REGIONS
# =============================================================================

def template4_climate_profile():
    """Section 2: Climate Region Research Profile"""
    filename = "Section2_Climate_Profile.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Climate Region Profile",
                     "Section 2: Climate Regions | Standard 3-ESS2-2")

    # Region name
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, y, "Climate Region:")
    c.setFont("Helvetica", 12)
    c.drawString(2.5*inch, y, "______________________________")

    # Location section
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "LOCATION")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Continent(s): _________________________________________________________")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Near equator or poles? _______________________________________________")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Example countries/regions: ___________________________________________")

    # Temperature section
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "TEMPERATURE")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Average summer temperature: __________°F")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Average winter temperature: __________°F")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Overall: (circle one)    HOT     WARM     COOL     COLD")

    # Precipitation section
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "PRECIPITATION")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Average rainfall per year: __________ inches")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Mostly rain or snow? _________________________________________________")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Rainy season or all year? ___________________________________________")

    # Seasons section
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "SEASONS")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "How many seasons? ____________________________________________________")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Describe them:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    # Plants and Animals
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "PLANTS AND ANIMALS")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Common plants: _______________________________________________________")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Common animals: ______________________________________________________")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Why do they live there? _____________________________________________")

    # Human Adaptations
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "HUMAN ADAPTATIONS")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "How do people live in this climate? ____________________________________")
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Special clothing needed? _____________________________________________")
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Special buildings? ___________________________________________________")

    # Drawing/photo space
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Draw or paste photo showing this climate:")

    # Box for drawing
    y -= 0.2*inch
    box_height = 1.8*inch
    c.rect(1*inch, y - box_height, 6.5*inch, box_height)

    c.save()
    print(f"Created: {filename}")


def template5_climate_comparison():
    """Section 2: Climate Comparison Chart"""
    filename = "Section2_Climate_Comparison.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Climate Region Comparison Chart",
                     "Section 2: Climate Regions | Standard 3-ESS2-2")

    # Instructions
    y -= 0.3*inch
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, y, "Use your Climate Profile notes to fill in this comparison chart.")

    # Table setup
    y -= 0.4*inch
    table_left = 0.75*inch
    col_width = 1.5*inch
    row_height = 0.5*inch

    # Column headers
    c.setFont("Helvetica-Bold", 9)
    x = table_left
    y_header = y

    headers = ["Feature", "Tropical", "Desert", "Temperate", "Polar"]
    for header in headers:
        c.drawCentredString(x + col_width/2, y_header, header)
        x += col_width

    # Header bottom line
    y -= 0.15*inch
    c.line(table_left, y, table_left + (col_width * 5), y)

    # Row labels and cells
    c.setFont("Helvetica", 8)

    rows = [
        "Location\n(latitude)",
        "Temperature\n(Hot/Warm/\nCool/Cold)",
        "Precipitation\n(amount per\nyear)",
        "Seasons\n(number &\ndescription)",
        "Typical\nPlants",
        "Typical\nAnimals",
        "How People\nAdapt"
    ]

    for row_label in rows:
        y -= row_height

        # Row label
        c.setFont("Helvetica-Bold", 8)
        # Handle multi-line labels
        lines = row_label.split('\n')
        label_y = y + row_height/2 + (len(lines)-1)*0.08*inch
        for line in lines:
            c.drawString(table_left + 0.05*inch, label_y, line)
            label_y -= 0.12*inch

        # Draw cells
        x = table_left
        for i in range(5):
            c.rect(x, y, col_width, row_height)
            x += col_width

    # Analysis section
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Analysis:")

    c.setFont("Helvetica", 10)
    y -= 0.3*inch
    c.drawString(1*inch, y, "Which region is hottest? ________________  Coldest? ________________")

    y -= 0.25*inch
    c.drawString(1*inch, y, "Which gets most precipitation? ________________  Least? ________________")

    y -= 0.25*inch
    c.drawString(1*inch, y, "Which region is most similar to where you live? ___________________________")

    y -= 0.25*inch
    c.drawString(1*inch, y, "Why? _____________________________________________________________________")

    c.save()
    print(f"Created: {filename}")


def template6_world_climate_map():
    """Section 2: World Climate Map Coloring Template"""
    filename = "Section2_World_Climate_Map.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    c.setPageSize((11*inch, 8.5*inch))  # Landscape orientation

    # Header (adjusted for landscape)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, 7.8*inch, "World Climate Zones Map")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 7.5*inch, "Section 2: Climate Regions | Standard 3-ESS2-2")

    c.setFont("Helvetica", 11)
    c.drawString(1*inch, 7.2*inch, "Name: ________________________")
    c.drawString(5*inch, 7.2*inch, "Date: ____________")

    c.line(0.75*inch, 7*inch, 10.25*inch, 7*inch)

    # Color key
    y = 6.7*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "Color Key:")

    c.setFont("Helvetica", 10)
    y -= 0.3*inch

    # Color boxes and labels
    colors = [
        ("Red/Orange", "Tropical (hot, wet)"),
        ("Yellow", "Desert (dry)"),
        ("Green", "Temperate (moderate)"),
        ("Blue", "Polar (cold)")
    ]

    box_size = 0.2*inch
    for color_name, description in colors:
        c.rect(1*inch, y, box_size, box_size)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(1.3*inch, y + 0.05*inch, f"{color_name}:")
        c.setFont("Helvetica", 10)
        c.drawString(2.3*inch, y + 0.05*inch, description)
        y -= 0.3*inch

    # Map area (large rectangle for student to draw/paste map)
    map_top = 5.5*inch
    map_height = 4.2*inch
    map_width = 9*inch

    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, map_top + 0.2*inch, "Color the climate zones on a world map:")

    # Map box
    c.setStrokeColorRGB(0.5, 0.5, 0.5)
    c.setLineWidth(2)
    c.rect(1*inch, map_top - map_height, map_width, map_height)

    # Equator line suggestion
    c.setStrokeColorRGB(0.8, 0.8, 0.8)
    c.setLineWidth(1)
    c.line(1*inch, map_top - map_height/2, 1*inch + map_width, map_top - map_height/2)
    c.setFont("Helvetica", 8)
    c.drawString(1.1*inch, map_top - map_height/2 + 0.05*inch, "EQUATOR (middle)")

    # Instructions
    y = map_top - map_height - 0.3*inch
    c.setFont("Helvetica", 9)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(1*inch, y, "Tip: Use a printed world map or draw continents, then color by climate zone.")

    c.save()
    print(f"Created: {filename}")


# =============================================================================
# SECTION 3: WEATHER HAZARDS
# =============================================================================

def template7_hazard_analysis():
    """Section 3: Weather Hazard Research and Analysis"""
    filename = "Section3_Hazard_Analysis.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Weather Hazard Analysis",
                     "Section 3: Weather Hazard Solutions | Standard 3-ESS3-1")

    # Hazard name
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, y, "Hazard Name:")
    c.setFont("Helvetica", 12)
    c.drawString(2.3*inch, y, "_______________________________")

    # What is it section
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "WHAT IS IT?")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Scientific description:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "What causes it? _____________________________________________________")
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Where does it happen? _______________________________________________")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "When/how often? _____________________________________________________")

    # How dangerous section
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "HOW DANGEROUS IS IT?")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Warning time: (circle one)    NONE    MINUTES    HOURS    DAYS")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Severity scale (if exists): ________________________________________")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Historical examples: ________________________________________________")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    # Impacts on People
    y -= 0.35*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "IMPACTS ON PEOPLE")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Health/safety risks: ________________________________________________")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Property damage: ____________________________________________________")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Disruption to daily life: ___________________________________________")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Economic costs: _____________________________________________________")

    # Impacts on Environment
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "IMPACTS ON ENVIRONMENT")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Effects on plants: __________________________________________________")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Effects on animals: _________________________________________________")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Effects on land/water: ______________________________________________")

    # Real Example
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "REAL EXAMPLE")

    c.setFont("Helvetica", 10)
    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Event: ______________________________________________________________")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "Date: ________________    Location: ___________________________________")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "What happened:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "How many people affected? ___________________________________________")

    c.save()
    print(f"Created: {filename}")


def template8_solution_evaluation():
    """Section 3: Solution Evaluation Matrix"""
    filename = "Section3_Solution_Evaluation.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    y = create_header(c, "Solution Evaluation Matrix",
                     "Section 3: Weather Hazard Solutions | Standard 3-ESS3-1")

    # Hazard name
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "Weather Hazard:")
    c.setFont("Helvetica", 11)
    c.drawString(2.3*inch, y, "______________________________________")

    # Instructions
    y -= 0.35*inch
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, y, "Research 3-4 solutions for this hazard. Evaluate each using the criteria below.")

    # Solution 1
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "SOLUTION #1:")
    c.setFont("Helvetica", 11)
    c.drawString(2.2*inch, y, "___________________________________________")

    y -= 0.3*inch
    c.setFont("Helvetica", 10)
    c.drawString(1.2*inch, y, "Type: (circle one)    PREDICTION    PROTECTION    PREPARATION")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "How it works:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1.2*inch, y, "Rate this solution (1-5 stars for each):")

    c.setFont("Helvetica", 9)
    y -= 0.25*inch
    c.drawString(1.4*inch, y, "Saves lives: ☆ ☆ ☆ ☆ ☆        Reduces property damage: ☆ ☆ ☆ ☆ ☆")
    y -= 0.2*inch
    c.drawString(1.4*inch, y, "Affordable: ☆ ☆ ☆ ☆ ☆         Easy to implement: ☆ ☆ ☆ ☆ ☆")
    y -= 0.2*inch
    c.drawString(1.4*inch, y, "Works reliably: ☆ ☆ ☆ ☆ ☆      TOTAL: _____/25 stars")

    y -= 0.25*inch
    c.setFont("Helvetica", 10)
    c.drawString(1.2*inch, y, "Costs/Limitations: __________________________________________________")

    # Solution 2
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "SOLUTION #2:")
    c.setFont("Helvetica", 11)
    c.drawString(2.2*inch, y, "___________________________________________")

    y -= 0.3*inch
    c.setFont("Helvetica", 10)
    c.drawString(1.2*inch, y, "Type: (circle one)    PREDICTION    PROTECTION    PREPARATION")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "How it works:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1.2*inch, y, "Rate this solution:")

    c.setFont("Helvetica", 9)
    y -= 0.25*inch
    c.drawString(1.4*inch, y, "Saves lives: ☆ ☆ ☆ ☆ ☆        Reduces property damage: ☆ ☆ ☆ ☆ ☆")
    y -= 0.2*inch
    c.drawString(1.4*inch, y, "Affordable: ☆ ☆ ☆ ☆ ☆         Easy to implement: ☆ ☆ ☆ ☆ ☆")
    y -= 0.2*inch
    c.drawString(1.4*inch, y, "Works reliably: ☆ ☆ ☆ ☆ ☆      TOTAL: _____/25 stars")

    y -= 0.25*inch
    c.setFont("Helvetica", 10)
    c.drawString(1.2*inch, y, "Costs/Limitations: __________________________________________________")

    # Solution 3
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "SOLUTION #3:")
    c.setFont("Helvetica", 11)
    c.drawString(2.2*inch, y, "___________________________________________")

    y -= 0.3*inch
    c.setFont("Helvetica", 10)
    c.drawString(1.2*inch, y, "Type: (circle one)    PREDICTION    PROTECTION    PREPARATION")

    y -= 0.25*inch
    c.drawString(1.2*inch, y, "How it works:")
    y -= 0.05*inch
    c.line(1.2*inch, y, 7.5*inch, y)
    y -= 0.2*inch
    c.line(1.2*inch, y, 7.5*inch, y)

    y -= 0.25*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1.2*inch, y, "Rate this solution:")

    c.setFont("Helvetica", 9)
    y -= 0.25*inch
    c.drawString(1.4*inch, y, "Saves lives: ☆ ☆ ☆ ☆ ☆        Reduces property damage: ☆ ☆ ☆ ☆ ☆")
    y -= 0.2*inch
    c.drawString(1.4*inch, y, "Affordable: ☆ ☆ ☆ ☆ ☆         Easy to implement: ☆ ☆ ☆ ☆ ☆")
    y -= 0.2*inch
    c.drawString(1.4*inch, y, "Works reliably: ☆ ☆ ☆ ☆ ☆      TOTAL: _____/25 stars")

    y -= 0.25*inch
    c.setFont("Helvetica", 10)
    c.drawString(1.2*inch, y, "Costs/Limitations: __________________________________________________")

    # Conclusion
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Which solution has most merit? Why?")

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
    """Generate all Earth Science PDF templates"""
    print("Generating Earth Science PDF Templates...")
    print("=" * 60)

    # Section 1: Weather Patterns
    print("\nSection 1: Weather Patterns and Graphing")
    print("-" * 60)
    template1_daily_weather_log()
    template2_temperature_graph()
    template3_precipitation_graph()

    # Section 2: Climate Regions
    print("\nSection 2: Climate in Different Regions")
    print("-" * 60)
    template4_climate_profile()
    template5_climate_comparison()
    template6_world_climate_map()

    # Section 3: Weather Hazards
    print("\nSection 3: Weather Hazard Solutions")
    print("-" * 60)
    template7_hazard_analysis()
    template8_solution_evaluation()

    print("\n" + "=" * 60)
    print("✓ All 8 Earth Science templates created successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
