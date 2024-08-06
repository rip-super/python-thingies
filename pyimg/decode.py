from PIL import Image, ImageTk
import struct
import tkinter as tk
import sys
import os
import io
import zlib
import numpy as np

def read_rgb_values(file_path):
    """Read RGB values and dimensions from a compressed binary file."""
    with open(file_path, "rb") as f:
        # Decompress the file
        compressed_data = f.read()
        rgb_data = zlib.decompress(compressed_data)
        
        # Read width and height from the decompressed data
        header = rgb_data[:8]
        width, height = struct.unpack('II', header)
        
        # Read RGB values
        rgb_array = np.frombuffer(rgb_data[8:], dtype=np.uint8).reshape((height, width, 3))

    return rgb_array, width, height

def create_image(rgb_array, width, height):
    """Create an image from RGB array."""
    img = Image.fromarray(rgb_array, 'RGB')

    # Convert the image to a BytesIO object with compression
    image_bytes = io.BytesIO()
    img.save(image_bytes, format='PNG', optimize=True, compress_level=9)
    image_bytes.seek(0)
    return image_bytes

def preprocess_image(image_bytes, max_width=800, max_height=600):
    """Preprocess the image to resize it while maintaining aspect ratio."""
    with Image.open(image_bytes) as img:
        img.thumbnail((max_width, max_height), Image.LANCZOS)
        
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
    return img_bytes

def display_image(image_bytes, file_name):
    """Display the image in a tkinter window with preprocessing."""
    root = tk.Tk()
    
    preprocessed_image_bytes = preprocess_image(image_bytes)
    
    img = Image.open(preprocessed_image_bytes)
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=img_tk)
    label.pack(padx=5, pady=5)

    margin = 10
    window_width = img_tk.width() + margin
    window_height = img_tk.height() + margin
    root.geometry(f"{window_width}x{window_height}")

    root.title(f"Decoded Image - {file_name}")
    root.attributes('-topmost', True)
    
    root.mainloop()

def main():
    if len(sys.argv) != 2:
        print("Usage: decode.py <path_to_pyimg_file>")
        sys.exit(1)

    pyimg_file_path = sys.argv[1]

    if not os.path.isfile(pyimg_file_path):
        print("The specified .pyimg file does not exist.")
        sys.exit(1)

    rgb_array, width, height = read_rgb_values(pyimg_file_path)
    image_bytes = create_image(rgb_array, width, height)

    file_name = os.path.basename(pyimg_file_path)
    display_image(image_bytes, file_name)

if __name__ == "__main__":
    main()
