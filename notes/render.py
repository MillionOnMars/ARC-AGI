#!/usr/bin/python3
import json
import sys
from PIL import Image

# Define the color mapping
color_map = {
    0: "#000000",  # black
    1: "#0074D9",  # blue
    2: "#FF4136",  # red
    3: "#2ECC40",  # green
    4: "#FFDC00",  # yellow
    5: "#AAAAAA",  # grey
    6: "#F012BE",  # fuschia
    7: "#FF851B",  # orange
    8: "#7FDBFF",  # teal
    9: "#870C25"   # brown
}

# Get the JSON filename from command-line arguments
json_file = sys.argv[1]

# Load the JSON data
with open(json_file, "r") as file:
    data = json.load(file)

# Process and generate images for "train" and "test" data
for data_type in ["train", "test"]:
    for i, item in enumerate(data[data_type], start=1):
        for io_type in ["input", "output"]:
            # Get the dimensions of the grid
            grid = item[io_type]
            rows = len(grid)
            cols = len(grid[0])

            # Define the size of each square and the grid line width
            square_size = 20
            grid_width = 1

            # Calculate the dimensions of the output image
            output_width = cols * square_size + (cols - 1) * grid_width
            output_height = rows * square_size + (rows - 1) * grid_width

            # Create a new image with the specified dimensions
            image = Image.new("RGB", (output_width, output_height), "white")

            # Iterate over each square and set the color
            for r in range(rows):
                for c in range(cols):
                    color_code = grid[r][c]
                    color = color_map[color_code]
                    
                    # Calculate the coordinates of the square
                    x1 = c * (square_size + grid_width)
                    y1 = r * (square_size + grid_width)
                    x2 = x1 + square_size
                    y2 = y1 + square_size
                    
                    # Create a new image for the square and paste it onto the main image
                    square = Image.new("RGB", (square_size, square_size), color)
                    image.paste(square, (x1, y1))

            # Save the image as PNG
            image_filename = f"{json_file[:-5]}_{data_type}_{i:02d}_{io_type}.png"
            image.save(image_filename)
