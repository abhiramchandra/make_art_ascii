import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import sys

symbols_list = ["#", "-", "*", ".", "+", "o"]
threshold_list = [0, 50, 100, 150, 200]

def print_out_ascii(array):
    """Prints the coded image with symbols."""
    for row in array:
        for e in row:
            print(symbols_list[int(e) % len(symbols_list)], end=" ")
        print()

def img_to_ascii(image):
    """Returns the numeric coded image."""
    height, width = image.shape
    new_width = int(width / 20)
    new_height = int(height / 40)

    resized_image = cv2.resize(image, (new_width, new_height))

    thresh_image = np.zeros(resized_image.shape)

    for i, threshold in enumerate(threshold_list):
        thresh_image[resized_image > threshold] = i
    return thresh_image

def select_file():
    """Open a file dialog and return the selected file path."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    return file_path

if __name__ == "__main__":
    # Get the image path using file dialog
    image_path = select_file()

    if not image_path:
        print("No image file selected. Exiting.")
        sys.exit()

    print(f"Using {image_path} as Image Path\n")

    image = cv2.imread(image_path, 0)

    if image is None:
        print(f"Failed to load image at path: {image_path}")
        sys.exit()

    ascii_art = img_to_ascii(image)
    print_out_ascii(ascii_art)
