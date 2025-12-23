#!/usr/bin/env python3
"""
Life Science PDF Template Generator
Creates 17 professional PDF templates for 3rd Grade NGSS Life Science investigations

Templates Created:
1. Section1_Life_Cycle_Comparison.pdf - Compare life cycles across organisms
2. Section1_Life_Cycle_Model.pdf - Circular life cycle diagram template
3. Section2_Family_Traits_Data.pdf - Family traits data collection
4. Section2_Traits_Comparison.pdf - Venn diagram for trait comparison
5. Section2_Plant_Traits.pdf - Plant observation log
6. Section3_Environment_Effects_Data.pdf - Environmental conditions comparison
7. Section3_Sunlight_Experiment.pdf - Plant growth tracking
8. Section4_Variation_Observations.pdf - Within-species variation data
9. Section4_Survival_Advantages.pdf - Claim-Evidence-Reasoning template
10. Section5_Animal_Groups_Research.pdf - Animal group benefits research
11. Section5_Group_Survival_Analysis.pdf - Argument construction template
12. Section6_Fossil_Observations.pdf - Fossil evidence analysis
13. Section6_Ancient_Environment.pdf - Environment reconstruction
14. Section7_Habitat_Match.pdf - Organism-habitat matching
15. Section7_Survival_Needs.pdf - Survival needs checklist
16. Section8_Problem_Definition.pdf - Environmental problem analysis
17. Section8_Solution_Design.pdf - Engineering design template
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
import os

# Create output directory if it doesn't exist
output_dir = os.path.dirname(os.path.abspath(__file__))

def create_header(c, title, section_info):
    """Create consistent header for all templates"""
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, 10.5*inch, title)

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 10.2*inch, section_info)

    # Name and Date fields
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.9*inch, "Name: ________________________")
    c.drawString(5*inch, 9.9*inch, "Date: ____________")

    # Draw line under header
    c.line(0.75*inch, 9.75*inch, 7.75*inch, 9.75*inch)

def template1_life_cycle_comparison():
    """Section 1: Life Cycle Comparison Table"""
    filename = os.path.join(output_dir, "Section1_Life_Cycle_Comparison.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Life Cycle Comparison", "Section 1: Life Cycles")

    # Instructions
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Compare the life cycles of 4-5 different organisms. Fill in what happens at each stage.")

    # Create table
    y_start = 9*inch
    col_width = 1.3*inch
    row_height = 0.6*inch

    # Table headers
    c.setFont("Helvetica-Bold", 9)
    headers = ["Organism", "Birth", "Growth", "Reproduction", "Death"]
    for i, header in enumerate(headers):
        c.drawString(1*inch + i*col_width, y_start, header)

    # Draw table grid
    c.setFont("Helvetica", 8)
    for row in range(6):  # 5 organisms + header
        y = y_start - (row * row_height)
        c.line(0.75*inch, y - 0.05*inch, 7.25*inch, y - 0.05*inch)

        if row > 0:  # Number the organism rows
            c.drawString(0.8*inch, y - 0.4*inch, str(row))

    # Vertical lines
    for i in range(6):
        x = 0.75*inch + i*col_width
        c.line(x, y_start, x, y_start - 5*row_height)

    # Drawing space at bottom
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, 4.5*inch, "Drawing Space: Choose one organism and draw its complete life cycle")
    c.rect(1*inch, 1.5*inch, 6*inch, 2.8*inch)

    c.save()
    print(f"Created: {filename}")

def template2_life_cycle_model():
    """Section 1: Circular Life Cycle Model"""
    filename = os.path.join(output_dir, "Section1_Life_Cycle_Model.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Life Cycle Circle Model", "Section 1: Life Cycles")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Create a circular model showing the life cycle stages. Draw and label each stage.")

    # Draw large circle
    center_x = 4.25*inch
    center_y = 5.5*inch
    radius = 2.5*inch

    c.circle(center_x, center_y, radius, stroke=1, fill=0)

    # Draw cross dividing into 4 sections
    c.line(center_x - radius, center_y, center_x + radius, center_y)
    c.line(center_x, center_y - radius, center_x, center_y + radius)

    # Label sections
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(center_x, center_y + radius + 0.3*inch, "BIRTH")
    c.drawCentredString(center_x + radius + 0.5*inch, center_y, "GROWTH")
    c.drawCentredString(center_x, center_y - radius - 0.3*inch, "REPRODUCTION")
    c.drawCentredString(center_x - radius - 0.6*inch, center_y, "DEATH")

    # Draw arrows showing cycle
    c.setFont("Helvetica", 9)
    c.drawString(center_x + 0.2*inch, center_y + 1.5*inch, "→")
    c.drawString(center_x + 1.5*inch, center_y + 0.2*inch, "→")
    c.drawString(center_x - 0.2*inch, center_y - 1.5*inch, "→")
    c.drawString(center_x - 1.5*inch, center_y - 0.2*inch, "→")

    # Organism name
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, 2.5*inch, "Organism: _______________________________")

    c.save()
    print(f"Created: {filename}")

def template3_family_traits():
    """Section 2: Family Traits Data Table"""
    filename = os.path.join(output_dir, "Section2_Family_Traits_Data.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Family Traits Data Collection", "Section 2: Inherited Traits")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Collect data on traits from your family members. Observe or ask about each trait.")

    # Create table
    y_start = 9*inch
    col_widths = [1.2*inch, 0.8*inch, 0.9*inch, 0.9*inch, 0.9*inch, 0.9*inch, 0.9*inch]
    row_height = 0.45*inch

    # Headers
    c.setFont("Helvetica-Bold", 8)
    headers = ["Trait", "Student", "Parent 1", "Parent 2", "Sibling 1", "Sibling 2", "Other"]
    x = 0.75*inch
    for i, header in enumerate(headers):
        c.drawString(x, y_start, header)
        x += col_widths[i]

    # Trait rows
    traits = [
        "Eye Color",
        "Hair Color",
        "Hair Texture",
        "Height (cm)",
        "Skin Tone",
        "Freckles?",
        "Dimples?",
        "Earlobe Type",
        "Tongue Roll?",
        "Other: _____"
    ]

    c.setFont("Helvetica", 8)
    for row, trait in enumerate(traits):
        y = y_start - ((row + 1) * row_height)
        c.drawString(0.8*inch, y + 0.15*inch, trait)

        # Draw row line
        c.line(0.75*inch, y, 7.25*inch, y)

    # Draw vertical lines
    x = 0.75*inch
    for width in [0] + col_widths:
        c.line(x, y_start + 0.05*inch, x, y_start - len(traits)*row_height)
        x += width

    # Bottom line
    c.line(0.75*inch, y_start - len(traits)*row_height, 7.25*inch, y_start - len(traits)*row_height)

    # Analysis section
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, 3*inch, "Pattern Analysis:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, 2.7*inch, "Which traits match Parent 1? _______________________________________________")
    c.drawString(1*inch, 2.4*inch, "Which traits match Parent 2? _______________________________________________")
    c.drawString(1*inch, 2.1*inch, "Are you exactly like one parent? _______________________________________________")

    c.save()
    print(f"Created: {filename}")

def template4_traits_comparison():
    """Section 2: Venn Diagram for Trait Comparison"""
    filename = os.path.join(output_dir, "Section2_Traits_Comparison.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Inherited Traits Comparison", "Section 2: Inherited Traits")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Use the Venn diagram to compare inherited traits vs. learned traits/behaviors.")

    # Draw Venn diagram
    center_y = 6*inch
    left_circle_x = 2.5*inch
    right_circle_x = 4.5*inch
    radius = 1.8*inch

    c.circle(left_circle_x, center_y, radius, stroke=1, fill=0)
    c.circle(right_circle_x, center_y, radius, stroke=1, fill=0)

    # Labels
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(left_circle_x - 1*inch, center_y + 2.3*inch, "INHERITED")
    c.drawCentredString(left_circle_x - 1*inch, center_y + 2*inch, "TRAITS")
    c.drawCentredString(right_circle_x + 1*inch, center_y + 2.3*inch, "LEARNED")
    c.drawCentredString(right_circle_x + 1*inch, center_y + 2*inch, "BEHAVIORS")
    c.drawCentredString(3.5*inch, center_y + 2.5*inch, "BOTH")

    # Examples space
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, 3.2*inch, "Examples of Inherited Traits:")
    c.drawString(1*inch, 2.9*inch, "1. ________________________________")
    c.drawString(1*inch, 2.6*inch, "2. ________________________________")
    c.drawString(1*inch, 2.3*inch, "3. ________________________________")

    c.drawString(4.5*inch, 3.2*inch, "Examples of Learned:")
    c.drawString(4.5*inch, 2.9*inch, "1. ________________________________")
    c.drawString(4.5*inch, 2.6*inch, "2. ________________________________")
    c.drawString(4.5*inch, 2.3*inch, "3. ________________________________")

    c.save()
    print(f"Created: {filename}")

def template5_plant_traits():
    """Section 2: Plant Traits Observation Log"""
    filename = os.path.join(output_dir, "Section2_Plant_Traits.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Plant Growth Observation Log", "Section 2: Inherited Traits")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Track your bean plants over 2-3 weeks. Measure and observe weekly.")

    # Table for observations
    y_start = 9*inch
    col_widths = [0.6*inch, 1*inch, 0.9*inch, 1*inch, 2.5*inch]
    row_height = 0.5*inch

    # Date header
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y_start + 0.3*inch, "Date: _______________")

    # Table headers
    c.setFont("Helvetica-Bold", 8)
    headers = ["Plant #", "Height (cm)", "# Leaves", "Leaf Color", "Notes"]
    x = 0.75*inch
    for i, header in enumerate(headers):
        c.drawString(x + 0.1*inch, y_start, header)
        x += col_widths[i]

    # Plant rows (1-10)
    c.setFont("Helvetica", 8)
    for row in range(11):  # 10 plants + header
        y = y_start - (row * row_height)
        c.line(0.75*inch, y - 0.05*inch, 7.25*inch, y - 0.05*inch)

        if row > 0:
            c.drawString(0.85*inch, y - 0.3*inch, str(row))

    # Vertical lines
    x = 0.75*inch
    for width in [0] + col_widths:
        c.line(x, y_start + 0.05*inch, x, y_start - 10*row_height)
        x += width

    # Summary section
    y_bottom = y_start - 10.5*row_height
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y_bottom, "Summary:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, y_bottom - 0.3*inch, "Average height: _______ cm       Tallest: _______ cm       Shortest: _______ cm")
    c.drawString(1*inch, y_bottom - 0.6*inch, "Most common leaf color: _________________")
    c.drawString(1*inch, y_bottom - 0.9*inch, "Overall observations: _______________________________________________________________")

    c.save()
    print(f"Created: {filename}")

def template6_environment_effects():
    """Section 3: Environmental Effects Data"""
    filename = os.path.join(output_dir, "Section3_Environment_Effects_Data.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Environmental Effects on Traits - Data Collection", "Section 3: Environmental Effects")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Compare plants grown in two different conditions. Record measurements weekly.")

    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, 9*inch, "Environmental Variable Being Tested: _________________________________")

    # Sunlight Group Table
    y_start = 8.5*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y_start, "SUNLIGHT GROUP (or Condition 1)")

    y_start -= 0.3*inch
    create_data_table(c, y_start, "Sunlight")

    # Shade Group Table
    y_start = 5*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y_start, "SHADE GROUP (or Condition 2)")

    y_start -= 0.3*inch
    create_data_table(c, y_start, "Shade")

    # Analysis
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, 1.5*inch, "Data Analysis:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, 1.2*inch, "Average height - Sunlight group: _______    Shade group: _______    Difference: _______")
    c.drawString(1*inch, 0.9*inch, "Which group grew better? ________________    Why? _________________________________")

    c.save()
    print(f"Created: {filename}")

def create_data_table(c, y_start, group_name):
    """Helper function to create plant data table"""
    col_widths = [0.8*inch, 1*inch, 0.9*inch, 1.2*inch, 2.2*inch]
    row_height = 0.4*inch

    # Headers
    c.setFont("Helvetica-Bold", 8)
    headers = ["Plant", "Height (cm)", "# Leaves", "Leaf Color (1-5)", "Notes"]
    x = 0.75*inch
    for i, header in enumerate(headers):
        c.drawString(x + 0.05*inch, y_start, header)
        x += col_widths[i]

    # Rows
    c.setFont("Helvetica", 8)
    for row in range(4):  # 3 plants + header
        y = y_start - (row * row_height)
        c.line(0.75*inch, y - 0.05*inch, 7*inch, y - 0.05*inch)

        if row > 0:
            c.drawString(0.8*inch, y - 0.25*inch, f"{group_name}-{row}")

    # Vertical lines
    x = 0.75*inch
    for width in [0] + col_widths:
        c.line(x, y_start + 0.05*inch, x, y_start - 3*row_height)
        x += width

def template7_sunlight_experiment():
    """Section 3: Daily Sunlight Experiment Tracking"""
    filename = os.path.join(output_dir, "Section3_Sunlight_Experiment.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Daily Plant Growth Tracking", "Section 3: Environmental Effects")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Track your plants every 2-3 days. Measure height and note changes.")

    # Create tracking table
    y_start = 9*inch
    col_widths = [0.8*inch, 1*inch, 1*inch, 1*inch, 2.5*inch]
    row_height = 0.4*inch

    # Headers
    c.setFont("Helvetica-Bold", 8)
    headers = ["Day #", "Date", "Sun Height", "Shade Height", "Observations"]
    x = 0.75*inch
    for i, header in enumerate(headers):
        c.drawString(x + 0.05*inch, y_start, header)
        x += col_widths[i]

    # Create 14 rows for daily tracking
    c.setFont("Helvetica", 7)
    for row in range(15):  # 14 days + header
        y = y_start - (row * row_height)
        c.line(0.75*inch, y - 0.05*inch, 7.25*inch, y - 0.05*inch)

        if row > 0:
            c.drawString(0.85*inch, y - 0.25*inch, str(row))

    # Vertical lines
    x = 0.75*inch
    for width in [0] + col_widths:
        c.line(x, y_start + 0.05*inch, x, y_start - 14*row_height)
        x += width

    c.save()
    print(f"Created: {filename}")

def template8_variation_observations():
    """Section 4: Variation Within Species"""
    filename = os.path.join(output_dir, "Section4_Variation_Observations.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Variation Within Species - Observations", "Section 4: Variation and Survival")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Observe and record variation among individuals of the same species.")

    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, 9*inch, "Species/Organism: _________________________________")

    # Table for individuals
    y_start = 8.6*inch
    col_widths = [0.8*inch, 1.5*inch, 1.5*inch, 1.5*inch, 1.8*inch]
    row_height = 0.5*inch

    # Headers
    c.setFont("Helvetica-Bold", 8)
    headers = ["Individual", "Trait 1:", "Trait 2:", "Trait 3:", "Special Features"]
    x = 0.75*inch
    for i, header in enumerate(headers):
        c.drawString(x + 0.05*inch, y_start, header)
        x += col_widths[i]

    # Rows for 8 individuals
    c.setFont("Helvetica", 8)
    for row in range(9):
        y = y_start - (row * row_height)
        c.line(0.75*inch, y - 0.05*inch, 7.25*inch, y - 0.05*inch)

        if row > 0:
            c.drawString(0.8*inch, y - 0.3*inch, f"#{row}")

    # Vertical lines
    x = 0.75*inch
    for width in [0] + col_widths:
        c.line(x, y_start + 0.05*inch, x, y_start - 8*row_height)
        x += width

    # Analysis section
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, 3.8*inch, "Variation Analysis:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, 3.5*inch, "Range of variation for Trait 1: _________________________________________________")
    c.drawString(1*inch, 3.2*inch, "Range of variation for Trait 2: _________________________________________________")
    c.drawString(1*inch, 2.9*inch, "Most common variation: ________________________________________________________")
    c.drawString(1*inch, 2.6*inch, "Rarest variation: ______________________________________________________________")
    c.drawString(1*inch, 2.3*inch, "Why might this variation be helpful? ___________________________________________")
    c.drawString(1*inch, 2*inch, "____________________________________________________________________________")

    c.save()
    print(f"Created: {filename}")

def template9_survival_advantages():
    """Section 4: Claim-Evidence-Reasoning Template"""
    filename = os.path.join(output_dir, "Section4_Survival_Advantages.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Variation and Survival Advantages - Argument", "Section 4: Variation and Survival")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Build a scientific argument using Claim-Evidence-Reasoning framework.")

    # CLAIM section
    y = 9*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "CLAIM:")
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, y - 0.25*inch, "State your main argument about how variation helps survival:")
    c.rect(1*inch, y - 0.9*inch, 6*inch, 0.5*inch)

    # EVIDENCE section
    y -= 1.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "EVIDENCE:")
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, y - 0.25*inch, "Provide at least 3 specific pieces of evidence:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, y - 0.5*inch, "1. ___________________________________________________________________________")
    c.drawString(1*inch, y - 0.8*inch, "   ___________________________________________________________________________")
    c.drawString(1*inch, y - 1.1*inch, "2. ___________________________________________________________________________")
    c.drawString(1*inch, y - 1.4*inch, "   ___________________________________________________________________________")
    c.drawString(1*inch, y - 1.7*inch, "3. ___________________________________________________________________________")
    c.drawString(1*inch, y - 2*inch, "   ___________________________________________________________________________")

    # REASONING section
    y -= 2.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "REASONING:")
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, y - 0.25*inch, "Explain how your evidence supports your claim:")
    c.rect(1*inch, y - 2*inch, 6*inch, 1.6*inch)

    # Drawing space
    y -= 2.5*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y, "Drawing/Diagram (optional):")
    c.rect(1*inch, y - 1.8*inch, 6*inch, 1.5*inch)

    c.save()
    print(f"Created: {filename}")

def template10_animal_groups_research():
    """Section 5: Animal Groups Research Template"""
    filename = os.path.join(output_dir, "Section5_Animal_Groups_Research.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Animal Groups Research", "Section 5: Animal Groups")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Research how different animal groups help members survive. Complete for 3-4 animals.")

    # Create template for one animal (will fit 2 per page)
    def create_animal_section(y_start):
        c.setFont("Helvetica-Bold", 11)
        c.drawString(1*inch, y_start, "Animal: _________________________________")

        c.setFont("Helvetica", 9)
        y = y_start - 0.3*inch
        c.drawString(1*inch, y, "Type of group: ___________________________    Group size: ______________")

        y -= 0.3*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(1*inch, y, "What they do together:")
        c.setFont("Helvetica", 8)
        y -= 0.2*inch
        for i in range(3):
            c.drawString(1.2*inch, y, "• _________________________________________________________________")
            y -= 0.2*inch

        y -= 0.1*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(1*inch, y, "How group helps members survive:")
        c.setFont("Helvetica", 8)
        y -= 0.2*inch
        benefits = ["Protection:", "Food/Hunting:", "Raising Young:", "Other:"]
        for benefit in benefits:
            c.drawString(1.2*inch, y, f"{benefit} _________________________________________________")
            y -= 0.2*inch

        y -= 0.1*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(1*inch, y, "Evidence sources:")
        c.setFont("Helvetica", 8)
        y -= 0.2*inch
        c.drawString(1.2*inch, y, "• _________________________________________________________________")

        # Drawing box
        y -= 0.3*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(1*inch, y, "Sketch/Photo:")
        y -= 0.2*inch
        c.rect(1*inch, y - 1.2*inch, 2.5*inch, 1.2*inch)

    # Create two animal sections
    create_animal_section(9*inch)
    create_animal_section(5.5*inch)

    c.save()
    print(f"Created: {filename}")

def template11_group_survival_analysis():
    """Section 5: Group vs Solo Survival Analysis"""
    filename = os.path.join(output_dir, "Section5_Group_Survival_Analysis.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Solo vs. Group Survival - Argument Template", "Section 5: Animal Groups")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Build an argument that animal groups help members survive.")

    # Comparison table
    y_start = 9*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y_start, "Survival Benefits Comparison:")

    y_start -= 0.3*inch
    col_widths = [2*inch, 2.3*inch, 2.3*inch]
    row_height = 0.5*inch

    # Headers
    c.setFont("Helvetica-Bold", 9)
    headers = ["Survival Need", "Living Alone", "Living in Group"]
    x = 0.75*inch
    for i, header in enumerate(headers):
        c.drawString(x + 0.1*inch, y_start, header)
        x += col_widths[i]

    # Rows
    needs = ["Finding food", "Protection from predators", "Raising young", "Finding shelter", "Overall survival"]
    c.setFont("Helvetica", 8)
    for row, need in enumerate(needs):
        y = y_start - ((row + 1) * row_height)
        c.drawString(0.8*inch, y + 0.2*inch, need)
        c.line(0.75*inch, y, 7.25*inch, y)

    # Vertical lines
    x = 0.75*inch
    for width in [0] + col_widths:
        c.line(x, y_start + 0.05*inch, x, y_start - len(needs)*row_height)
        x += width

    # Argument section
    y_arg = y_start - len(needs)*row_height - 0.5*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y_arg, "CLAIM:")
    c.setFont("Helvetica", 9)
    c.rect(1.8*inch, y_arg - 0.4*inch, 5.2*inch, 0.4*inch)

    y_arg -= 0.8*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y_arg, "EVIDENCE (3 examples):")
    c.setFont("Helvetica", 8)
    for i in range(3):
        y_arg -= 0.25*inch
        c.drawString(1*inch, y_arg, f"{i+1}. __________________________________________________________________")
        y_arg -= 0.2*inch
        c.drawString(1.2*inch, y_arg, "   __________________________________________________________________")

    y_arg -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y_arg, "REASONING:")
    c.setFont("Helvetica", 9)
    c.rect(1*inch, y_arg - 1.2*inch, 6*inch, 1*inch)

    c.save()
    print(f"Created: {filename}")

def template12_fossil_observations():
    """Section 6: Fossil Evidence Analysis"""
    filename = os.path.join(output_dir, "Section6_Fossil_Observations.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Fossil Evidence Analysis", "Section 6: Fossils and Ancient Environments")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Analyze fossil evidence to determine what we can learn about ancient organisms.")

    # Create template for analyzing multiple fossils
    y_start = 9*inch

    for i in range(3):  # 3 fossil analysis sections
        c.setFont("Helvetica-Bold", 10)
        c.drawString(1*inch, y_start, f"Fossil #{i+1}:")

        c.setFont("Helvetica", 9)
        y = y_start - 0.3*inch
        c.drawString(1*inch, y, "Type of fossil: ______________    Organism type: ____________________")

        y -= 0.3*inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(1*inch, y, "What we can learn from this fossil:")

        c.setFont("Helvetica", 8)
        questions = [
            "What did the organism look like?",
            "How big was it?",
            "What did it eat? (if we can tell)",
            "Where did it live? (land/water/air)",
            "What environment was it in?"
        ]
        for q in questions:
            y -= 0.2*inch
            c.drawString(1.2*inch, y, f"• {q} _______________________________________")

        # Drawing box
        y -= 0.3*inch
        c.rect(1*inch, y - 0.8*inch, 2*inch, 0.8*inch)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(1*inch, y - 0.9*inch, "Sketch/Photo")

        y_start = y - 1.1*inch

    c.save()
    print(f"Created: {filename}")

def template13_ancient_environment():
    """Section 6: Ancient Environment Reconstruction"""
    filename = os.path.join(output_dir, "Section6_Ancient_Environment.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Ancient Environment Reconstruction", "Section 6: Fossils")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Use multiple fossil clues to reconstruct what an ancient environment was like.")

    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, 9*inch, "Location: _______________________________    Time Period: _______________")

    # Evidence table
    y_start = 8.6*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y_start, "Fossil Evidence Found:")

    y_start -= 0.3*inch
    col_widths = [2.5*inch, 4*inch]
    row_height = 0.4*inch

    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.8*inch, y_start, "Fossil")
    c.drawString(3.5*inch, y_start, "What It Tells Us")

    c.setFont("Helvetica", 8)
    for row in range(6):
        y = y_start - ((row + 1) * row_height)
        c.line(0.75*inch, y, 7.25*inch, y)
        if row == 0:
            c.line(0.75*inch, y_start + 0.05*inch, 7.25*inch, y_start + 0.05*inch)

    # Vertical line
    c.line(0.75*inch, y_start + 0.05*inch, 0.75*inch, y_start - 6*row_height)
    c.line(3.25*inch, y_start + 0.05*inch, 3.25*inch, y_start - 6*row_height)
    c.line(7.25*inch, y_start + 0.05*inch, 7.25*inch, y_start - 6*row_height)

    # Analysis section
    y_analysis = y_start - 6.5*row_height
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y_analysis, "Environment Analysis:")

    c.setFont("Helvetica", 9)
    y_analysis -= 0.3*inch
    c.drawString(1*inch, y_analysis, "Climate (hot/cold/moderate): _______________    Wet or Dry: _______________")
    y_analysis -= 0.3*inch
    c.drawString(1*inch, y_analysis, "Landscape (ocean/forest/desert/grassland/etc.): _____________________________")
    y_analysis -= 0.3*inch
    c.drawString(1*inch, y_analysis, "Organisms that lived there: ___________________________________________________")
    y_analysis -= 0.3*inch
    c.drawString(1*inch, y_analysis, "How is this different from today? ______________________________________________")
    y_analysis -= 0.2*inch
    c.drawString(1*inch, y_analysis, "___________________________________________________________________________")

    # Drawing space
    y_analysis -= 0.5*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y_analysis, "Draw the ancient environment:")
    c.rect(1*inch, 1*inch, 6*inch, y_analysis - 1.2*inch)

    c.save()
    print(f"Created: {filename}")

def template14_habitat_match():
    """Section 7: Organism-Habitat Matching"""
    filename = os.path.join(output_dir, "Section7_Habitat_Match.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Habitat and Organism Matching", "Section 7: Habitat and Survival")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Match organisms to habitats and rate how well they would survive (0-10 scale).")

    # Create table
    y_start = 9*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y_start, "Habitat: _______________________________")

    y_start -= 0.4*inch
    col_widths = [1.8*inch, 1*inch, 3.5*inch]
    row_height = 0.6*inch

    # Headers
    c.setFont("Helvetica-Bold", 9)
    headers = ["Organism", "Rating (0-10)", "Explanation/Reasoning"]
    x = 0.75*inch
    for i, header in enumerate(headers):
        c.drawString(x + 0.1*inch, y_start, header)
        x += col_widths[i]

    # Rows for organisms
    c.setFont("Helvetica", 8)
    for row in range(9):  # 8 organisms + header
        y = y_start - (row * row_height)
        c.line(0.75*inch, y - 0.05*inch, 7.25*inch, y - 0.05*inch)

    # Vertical lines
    x = 0.75*inch
    for width in [0] + col_widths:
        c.line(x, y_start + 0.05*inch, x, y_start - 8*row_height)
        x += width

    # Rating key
    y_key = y_start - 8.5*row_height
    c.setFont("Helvetica-Bold", 9)
    c.drawString(1*inch, y_key, "Rating Scale:")
    c.setFont("Helvetica", 8)
    c.drawString(1*inch, y_key - 0.2*inch, "10 = Perfectly adapted, thrives     5 = Barely survives     0 = Cannot survive at all")

    # Summary
    y_summary = y_key - 0.6*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y_summary, "Summary:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, y_summary - 0.25*inch, "Organisms that survive WELL in this habitat: _____________________________________")
    c.drawString(1*inch, y_summary - 0.5*inch, "Organisms that survive POORLY: ___________________________________________________")
    c.drawString(1*inch, y_summary - 0.75*inch, "Organisms that CANNOT survive: ___________________________________________________")

    c.save()
    print(f"Created: {filename}")

def template15_survival_needs():
    """Section 7: Survival Needs Checklist"""
    filename = os.path.join(output_dir, "Section7_Survival_Needs.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Survival Needs Checklist", "Section 7: Habitat and Survival")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Check whether each habitat provides the survival needs for different organisms.")

    # Create grid
    y_start = 9*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y_start, "Organism: _______________________________")

    y_start -= 0.4*inch
    col_widths = [1.5*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.3*inch]
    row_height = 0.5*inch

    # Headers
    c.setFont("Helvetica-Bold", 8)
    headers = ["Survival Need", "Desert", "Rainforest", "Arctic", "Ocean"]
    x = 0.75*inch
    for i, header in enumerate(headers):
        c.drawString(x + 0.05*inch, y_start, header)
        x += col_widths[i]

    # Rows
    needs = ["Food available?", "Water available?", "Shelter available?", "Right temperature?", "Enough space?", "CAN SURVIVE?"]
    c.setFont("Helvetica", 8)
    for row, need in enumerate(needs):
        y = y_start - ((row + 1) * row_height)
        c.drawString(0.8*inch, y + 0.15*inch, need)
        c.line(0.75*inch, y, 7.25*inch, y)

        if row == len(needs) - 1:  # Last row
            c.setFont("Helvetica-Bold", 8)

    # Vertical lines
    x = 0.75*inch
    for width in [0] + col_widths:
        c.line(x, y_start + 0.05*inch, x, y_start - len(needs)*row_height)
        x += width

    # Instructions
    y_inst = y_start - (len(needs) + 0.5)*row_height
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, y_inst, "Mark each box: ✓ = Yes, needs met    ✗ = No, needs not met    ? = Uncertain")

    # Repeat for second organism
    y_start2 = y_inst - 0.5*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y_start2, "Organism: _______________________________")
    # (Would create same table structure again)

    c.save()
    print(f"Created: {filename}")

def template16_problem_definition():
    """Section 8: Environmental Problem Definition"""
    filename = os.path.join(output_dir, "Section8_Problem_Definition.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Environmental Problem Definition", "Section 8: Environmental Change Solutions")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Define an environmental problem and analyze its impact on organisms.")

    # Problem description
    y = 9*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "PROBLEM:")
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, y - 0.25*inch, "What environmental change is occurring?")
    c.rect(1*inch, y - 0.8*inch, 6*inch, 0.4*inch)

    # What's changing
    y -= 1.2*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y, "Details of Change:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, y - 0.2*inch, "What is changing? _______________________________________________________________")
    y -= 0.3*inch
    c.drawString(1*inch, y, "How fast? _______________________________________________________________________")
    y -= 0.3*inch
    c.drawString(1*inch, y, "Why is it happening? _____________________________________________________________")

    # Organisms affected
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y, "Organisms Affected:")
    c.setFont("Helvetica", 9)
    y -= 0.2*inch
    for i in range(4):
        c.drawString(1*inch, y, f"{i+1}. ________________    How affected: _____________________________________")
        y -= 0.25*inch

    # Impact analysis
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y, "Impact Analysis:")
    c.setFont("Helvetica", 9)
    y -= 0.25*inch
    c.drawString(1*inch, y, "Loss of food: ____________________________________________________________________")
    y -= 0.25*inch
    c.drawString(1*inch, y, "Loss of shelter: _________________________________________________________________")
    y -= 0.25*inch
    c.drawString(1*inch, y, "Temperature changes: _____________________________________________________________")
    y -= 0.25*inch
    c.drawString(1*inch, y, "Pollution effects: _______________________________________________________________")

    # Criteria and Constraints
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "CRITERIA (What solution must do):")
    c.setFont("Helvetica", 9)
    y -= 0.2*inch
    for i in range(3):
        c.drawString(1*inch, y, f"{i+1}. ________________________________________________________________________")
        y -= 0.25*inch

    y -= 0.2*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "CONSTRAINTS (Limitations):")
    c.setFont("Helvetica", 9)
    y -= 0.2*inch
    for i in range(3):
        c.drawString(1*inch, y, f"{i+1}. ________________________________________________________________________")
        y -= 0.25*inch

    c.save()
    print(f"Created: {filename}")

def template17_solution_design():
    """Section 8: Solution Design Template"""
    filename = os.path.join(output_dir, "Section8_Solution_Design.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    create_header(c, "Environmental Solution Design", "Section 8: Environmental Change Solutions")

    c.setFont("Helvetica", 10)
    c.drawString(1*inch, 9.4*inch, "Design a solution to help organisms affected by environmental change.")

    # Solution name
    y = 9*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "SOLUTION NAME: ___________________________________________________________")

    # Problem it solves
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y, "Problem it solves:")
    c.rect(1*inch, y - 0.5*inch, 6*inch, 0.4*inch)

    # How it works
    y -= 1*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y, "How it works (step-by-step):")
    c.setFont("Helvetica", 9)
    y -= 0.2*inch
    for i in range(4):
        c.drawString(1*inch, y, f"{i+1}. ________________________________________________________________________")
        y -= 0.25*inch

    # Materials needed
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y, "Materials/Resources needed:")
    c.setFont("Helvetica", 9)
    y -= 0.2*inch
    for i in range(3):
        c.drawString(1*inch, y, f"• __________________________________________________________________________")
        y -= 0.2*inch

    # Benefits
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y, "Benefits:")
    c.setFont("Helvetica", 9)
    y -= 0.2*inch
    c.drawString(1*inch, y, "Organisms helped: _______________________________________________________________")
    y -= 0.25*inch
    c.drawString(1*inch, y, "How much problem reduced: _______________________________________________________")
    y -= 0.25*inch
    c.drawString(1*inch, y, "Other positive effects: _________________________________________________________")

    # Limitations
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y, "Potential Problems/Limitations:")
    c.setFont("Helvetica", 9)
    y -= 0.2*inch
    for i in range(2):
        c.drawString(1*inch, y, f"• __________________________________________________________________________")
        y -= 0.2*inch

    # Drawing space
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, y, "Solution Diagram:")
    c.rect(1*inch, 0.75*inch, 6*inch, y - 0.95*inch)

    c.save()
    print(f"Created: {filename}")

def main():
    """Generate all PDF templates"""
    print("=" * 70)
    print("Generating Life Science PDF Templates")
    print("3rd Grade NGSS Home Learning Guide")
    print("=" * 70)
    print()

    # Section 1: Life Cycles (2 templates)
    print("Section 1: Life Cycles")
    template1_life_cycle_comparison()
    template2_life_cycle_model()

    # Section 2: Inherited Traits (3 templates)
    print("\nSection 2: Inherited Traits")
    template3_family_traits()
    template4_traits_comparison()
    template5_plant_traits()

    # Section 3: Environmental Effects (2 templates)
    print("\nSection 3: Environmental Effects on Traits")
    template6_environment_effects()
    template7_sunlight_experiment()

    # Section 4: Variation and Survival (2 templates)
    print("\nSection 4: Variation and Survival")
    template8_variation_observations()
    template9_survival_advantages()

    # Section 5: Animal Groups (2 templates)
    print("\nSection 5: Animal Groups")
    template10_animal_groups_research()
    template11_group_survival_analysis()

    # Section 6: Fossils (2 templates)
    print("\nSection 6: Fossils and Ancient Environments")
    template12_fossil_observations()
    template13_ancient_environment()

    # Section 7: Habitat and Survival (2 templates)
    print("\nSection 7: Habitat and Survival")
    template14_habitat_match()
    template15_survival_needs()

    # Section 8: Environmental Change Solutions (2 templates)
    print("\nSection 8: Environmental Change Solutions")
    template16_problem_definition()
    template17_solution_design()

    print()
    print("=" * 70)
    print("✓ ALL 17 TEMPLATES CREATED SUCCESSFULLY!")
    print("=" * 70)
    print(f"\nTemplates saved to: {output_dir}")
    print("\nTemplate files:")
    for i in range(1, 18):
        print(f"  - Section{i//2 + 1 if i <= 2 else (i-1)//2 + 1}_*.pdf")

if __name__ == "__main__":
    main()
