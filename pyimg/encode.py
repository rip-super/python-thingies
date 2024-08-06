from PIL import Image
import struct
import zlib

def image_to_rgb(image_path):
    """Extract RGB values from an image."""
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        width, height = img.size

        # Extract RGB values
        rgb_values = [img.getpixel((x, y)) for y in range(height) for x in range(width)]

    return rgb_values, width, height

# Path to the input image file
image_path = 'image.png'
rgb_values, width, height = image_to_rgb(image_path)

# Convert RGB values to bytes
rgb_bytes = struct.pack('II', width, height)
rgb_bytes += b''.join(struct.pack('BBB', r, g, b) for r, g, b in rgb_values)

# Compress the data
compressed_rgb_bytes = zlib.compress(rgb_bytes, level=9)

# Write to the .pyimg file
with open("image.pyimg", "wb") as f:
    f.write(compressed_rgb_bytes)
