#---------------------------------------------------------------------------------
#
# Image Processing Test
# Script makes black & white thumbnails of photos
# Thx https://auth0.com/blog/image-processing-in-python-with-pillow/
#
#---------------------------------------------------------------------------------

# Import packages
from PIL import Image #pip install --upgrade Pillow
import os

# Path to folder with original photos from TDoR Info export
inpath = './tdor_export_73.133.212.249_2020-12-29T23_48_37/photos/'
# Path to folder for created output photos (make it a "photos" folder to match the paths in data)
outpath = './photos/'

# Process photos
for file in os.listdir(inpath):
	# Get filename and path
	photo = inpath + file
	# Load image
	image = Image.open(photo) #image.show()
	# Resize (scaled)
	image.thumbnail((200, 200))
	# Greyscale
	greyscale_image = image.convert('L')
	# Save new photo
	outphoto = outpath + file
	greyscale_image.save(outphoto)