import tesserocr
from PIL import Image
image = Image.open('/home/tyf/image.png')
print(tesserocr.image_to_text(image))
# print(tesserocr.file_to_text('/home/tyf/image.png'))
