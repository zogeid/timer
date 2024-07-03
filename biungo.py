from reportlab.pdfgen import canvas
import numpy as np


def generate_bingo_card():
    # Create an empty 5x5 matrix for the bingo card
    card = np.zeros((5, 5), dtype=int)

    # Fill the columns with random numbers within a specific range
    for i in range(5):
        card[:, i] = np.random.choice(range(i * 19 + 1, (i + 1) * 19 + 1), size=5, replace=False)

    return card


# PDF configuration
A4 = (595, 842)  # A4 page size in points
card_size = (300, 250)  # Bingo card size in points
margin = 10  # Margin between cards

# Create a PDF file
pdf_filename = "bingo_popa.pdf"
pdf = canvas.Canvas(pdf_filename, pagesize=A4)

# Generate and draw bingo cards for each player
for player_number in range(1, 685):
    if player_number % 4 == 1:
        pdf.showPage()  # Start a new page for every set of 4 cards

    card = generate_bingo_card()  # Generate your bingo card

    # Calculate the position for the current card
    col = (player_number - 1) % 2  # Column index (0 or 1)
    row = 1 - ((player_number - 1) % 4) // 2  # Row index (0 or 1)

    x = col * (card_size[0] + margin)
    y = row * (card_size[1] + margin)

    # Draw the bingo card on the page
    pdf.rect(x, y, card_size[0], card_size[1])
    for i in range(5):
        for j in range(5):
            center = (
            x + i * (card_size[0] / 5) + (card_size[0] / 10), y + j * (card_size[1] / 5) + (card_size[1] / 10))
            pdf.drawCentredString(*center, str(card[i, j]))

# Save the PDF file
pdf.save()
