"""
File: image_editor_thingy_oct28.py
Author: Xander Hunt
Purpose: Make a rudimentary green screen.
"""

# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("snowscape.jpg")
image_other = Image.open("cat_small.jpg")


# This line attempts to open a new window to display the image.
# image_original.show()

# Record the original image's dimensions as variables.
(width1, height1) = image_original.size
print("Background dimensions: ", width1, height1)
(width2, height2) = image_other.size
print("Other dimensions: ", width2, height2)

# Create a pixels variable, check it too.
pixels1 = image_original.load()
pixels2 = image_other.load()
print(pixels2[0, 0])

# Change the green background.
for column in range(width2):
    for row in range(height2):
        (r, g, b) = pixels2[column, row]
        if (g > 180) and (r < 100) and (b < 100):
            pixels2[column, row] = pixels1[column, row]

# Return the color value of the pixel at (400, 300).
#pixels = image_original.load()
#print(pixels[400, 300])

# Draw some neat diagonal lines.
"""y_val = 0
for column in range(width1):
    pixels[column, y_val] = (0, 0, 0)
    y_val += 1
    if y_val >= 600:
        y_val = 0

y_val = 200
for column in range(width1):
    pixels[column, y_val] = (0, 0, 0)
    y_val += 1
    if y_val >= 600:
        y_val = 0

y_val = 599
for column in range(width1):
    pixels[column, y_val] = (0, 0, 0)
    y_val -= 1
    if y_val <= 0:
        y_val = 599

y_val = 399
for column in range(width1):
    pixels[column, y_val] = (0, 0, 0)
    y_val -= 1
    if y_val <= 0:
        y_val = 599"""

# Stick a red line down the middle.
"""for row in range(height1):
    pixels[400, row] = (255, 0, 0)"""

# Put on a dark filter
"""for row in range(height1):
    for column in range(width1):
        (r,g,b) = pixels[column, row]
        if r + g + b < 400:
            pixels[column, row] = (0, 0, 0)"""



#image_original.show()
image_other.show()