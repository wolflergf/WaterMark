#!/usr/bin/env python3
"""
Watermark App: A simple application to add watermarks to images using Tkinter and PIL.
"""

# Import necessary libraries
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk

# Global variables for image paths and objects
image_path = ""
image_obj = None
image_to_save = None

def upload_image():
    """
    Function to upload an image and display it on the canvas.
    """
    global image_obj, image_path

    # Open file dialog to choose an image file
    image_path = askopenfilename()

    # Update the label to show the uploaded image path
    label_path.config(text="Image uploaded: " + image_path)

    # Open the image using PIL and create a thumbnail for display
    img = Image.open(image_path)
    img.thumbnail((500, 500), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    # Display the image on the canvas
    canvas.create_image(0, 0, image=photo, anchor=NW)
    canvas.update()

    # Save the PhotoImage object for later use
    image_obj = photo

    # Enable the "Upload Watermark" button
    upload_image_watermark_button.config(state=NORMAL)

def add_watermark():
    """
    Function to add a watermark to the uploaded image and display the result.
    """
    global image_obj, image_to_save

    # Open file dialog to choose a watermark image file
    watermark_path = askopenfilename()

    # Open the watermark image using PIL
    watermark = Image.open(watermark_path)

    # Open the original image and convert it to RGBA mode for transparency support
    image = Image.open(image_path).convert("RGBA")

    # Paste the watermark onto the image at a specific position with a mask
    image.paste(watermark, (100, 300), mask=watermark)

    # Create a thumbnail for display
    image.thumbnail((500, 500), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Display the watermarked image on the canvas
    canvas.create_image(0, 0, image=photo, anchor=NW)
    canvas.update()

    # Save the watermarked image for later use
    image_to_save = image
    image_obj = photo

def save_image():
    """
    Function to save the watermarked image to a file.
    """
    # Open file dialog to choose a file path for saving
    file_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

    # Save the watermarked image to the chosen file path
    image_to_save.save(file_path)

# Create the main application window
root = Tk()
root.title("Watermark App")

# Label to display the path of the uploaded image
label_path = Label(root, text="Upload an image to add a watermark")
label_path.pack()

# Canvas for displaying images
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Button to upload an image
upload_image_button = Button(root, text="Upload Image", command=upload_image)
upload_image_button.pack()

# Button to upload a watermark and add it to the image
upload_image_watermark_button = Button(root, text="Upload Watermark", command=add_watermark, state=DISABLED)
upload_image_watermark_button.pack()

# Button to save the watermarked image
save_image_button = Button(root, text="Save", command=save_image)
save_image_button.pack()

# Start the Tkinter event loop
root.mainloop()
