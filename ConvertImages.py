from PIL import Image, ImageOps
import glob
import os.path

for name in glob.iglob('images/**/*.png', recursive=True):
    if os.path.isfile(name.replace('.png', '.jpg')):
        continue
    print("Processing " + name)
    image = Image.open(name).convert('RGBA')
    new_image = Image.new("RGB", image.size, (33, 37, 41))
    new_image.paste(image, (0, 0), image)
    im = ImageOps.pad(new_image, (200, 200), Image.LANCZOS, color=(33, 37, 41))
    im.convert('RGB').save(name.replace('.png', '.jpg'), 'JPEG')    


