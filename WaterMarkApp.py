from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

from PIL import Image, ImageTk

image_path = ""
image_obj = None
image_to_salve = None


def upload_image():
    global image_obj, image_path
    image_path = askopenfilename()
    label_path.config(text="Image uploaded: " + image_path)
    img = Image.open(image_path)
    img.thumbnail((500, 500), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=photo, anchor=NW)
    canvas.update()
    image_obj = photo
    upload_image_watermark_button.config(state=NORMAL)


def add_watermark():
    global image_obj, image_to_salve
    watermark_path = askopenfilename()
    watermark = Image.open(watermark_path)
    image = Image.open(image_path).convert("RGBA")
    image.paste(watermark, (100, 300), mask=watermark)
    image.thumbnail((500, 500), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor=NW)
    canvas.update()
    image_to_salve = image
    image_obj = photo


def save_image():
    file_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    image_to_salve.save(file_path)


root = Tk()
root.title("Water Mark App")
label_path = Label(root, text="Upload an image to add a Water Mark")
label_path.pack()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

upload_image_button = Button(root, text="Upload Image", command=upload_image)
upload_image_button.pack()

upload_image_watermark_button = Button(root, text="Upload Water Mark", command=add_watermark, state=DISABLED)
upload_image_watermark_button.pack()

save_image_button = Button(root, text="Save", command=save_image)
save_image_button.pack()

root.mainloop()
