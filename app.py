from PIL import Image
import os
from glob import glob

if not os.path.exists('input'):
    os.makedirs('input')

if not os.path.exists('output'):
    os.makedirs('output')

# Request user input for the maximum width of images and validate the input
while True:
    try:
        max_width = int(input("Please specify the width to which you want to scale the images \n"))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Get list of images in the 'input' folder
input_images = glob("input/*")

# If no images are found, notify the user
if not input_images:
    print("No images found to process. Add some images to input folder first.")
else:
    print("Scale the following images")
    for path in input_images:
        # Extract filename from the file path
        directory, filename = os.path.split(path)
        print(filename)  # Print current image name

        # Open, resize and save the image
        with Image.open(path) as im:
            im.thumbnail((max_width, im.height))
            im.save(f"output/{max_width}{filename}")

    print("Process completed. Check the output folder.")