"""
File: image_editor_thingy_oct28.py
Author: Xander Hunt
Purpose: Make a rudimentary green screen.
"""

# This line imports or includes the library we will need
from PIL import Image

# Opens the images and load them into variables, create the new image.
image_background = Image.open("snowscape.jpg")
image_subject = Image.open("cat_small.jpg")
image_new = Image.new("RGB", image_background.size)

# Record the original image's dimensions as a variable.
(width, height) = image_subject.size

# Create a pixel's variable, print it.
pixels1 = image_background.load()
pixels2 = image_subject.load()
pixels3 = image_new.load()

# Create the new image.
for column in range(width):
    for row in range(height):
        (r, g, b) = pixels2[column, row]
        if (g > 180) and (r < 100) and (b < 100):
            pixels3[column, row] = pixels1[column, row]
        else:
            pixels3[column, row] = pixels2[column, row]

# Display the new image, save it.
image_new.show()
image_new.save("the_new_image.jpg")