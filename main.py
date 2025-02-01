from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
from customtkinter import *

# Initialize the main window
win = CTk()
win.title("Image Watermarking App")
win.geometry("400x300")
set_appearance_mode("dark")

def upload_image():
    global filepath
    filepath = filedialog.askopenfilename()
    if filepath:
        Image.open(filepath)
        success_label = CTkLabel(win, text="Image uploaded successfully.", text_color="red")
        success_label.pack()

        watermark_label = CTkLabel(win, text="State the name of your watermark")
        watermark_label.pack()

        watermark_text = CTkEntry(win, width=150)
        watermark_text.pack()

        watermark_btn = CTkButton(win, text="Add Watermark",
                                  command=lambda: add_watermark(filepath, watermark_text.get()), corner_radius=30)
        watermark_btn.pack(pady=20, padx=20)

def add_watermark(image_path, watermark_text):
    original = Image.open(image_path)
    width, height = original.size
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(original, (0, 0))

    draw = ImageDraw.Draw(transparent)
    font = ImageFont.truetype("arial.ttf", 50)  # Adjust font and size as needed
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = (width - text_width - 10, height - text_height - 10)  # Bottom right corner
    draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)  # White text with transparency

    transparent.show()  # Display the watermarked image
    transparent.save("watermarked_image.png")  # Save the watermarked image

    # Provide an option to upload a new image
    reset_app()

def reset_app():
    # Clear previous widgets
    for widget in win.winfo_children():
        widget.destroy()

    # Recreate the upload button
    upload_btn = CTkButton(win, text="Upload Image", command=upload_image, corner_radius=30)
    upload_btn.pack(pady=20, padx=20)

# Start the application with the upload button
reset_app()

# Run the main loop
win.mainloop()