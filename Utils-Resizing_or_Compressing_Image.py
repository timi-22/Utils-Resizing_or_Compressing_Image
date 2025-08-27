from PIL import Image

# Open the image file
img = Image.open("/path/to/UNRESIZED_IMG.png")

# Resize the image to a specific pixel size
img = img.resize((128, 128))  # width, height
# Resize the image using the LANCZOS resampling filter. at
#img = img.resize((128, 128), Image.LANCZOS)


# Save the resized image with compression
#img.save('output.png', optimize=True, quality=50)
img.save("/path/resized_img.png")



# OR

from PIL import Image, ImageDraw

# Open the image file
img = Image.open("/UNRESIZED_IMG.png")

# Resize the image to a specific pixel size
img = img.resize((1280, 1280))  # width, height

# Create a new image with a transparent background
new_img = Image.new('RGBA', img.size, (0, 0, 0, 0))

# Create a mask image with a white background
mask_img = Image.new('L', img.size, 0)

# Create a drawing context
draw = ImageDraw.Draw(mask_img)

# Draw a rounded rectangle
draw.rounded_rectangle((0, 0) + img.size, fill=255, outline=255, width=0, radius=80)

# Paste the original image onto the new image, using the rounded rectangle as a mask
new_img.paste(img, (0, 0), mask=mask_img)

# Save the new image
new_img.save("/resized_imgcurve.png")