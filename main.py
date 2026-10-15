from PIL import Image
from PIL import ImageOps

scale = 10

cutoff = 1.0

caracters = " .:-=+*#%@"

x = len(caracters)

y = 256 // x


with Image.open("image.png") as im:
    imag = im.convert(mode = "L")
    (width, height) = (imag.width // (scale - (scale // 2)), imag.height // scale)
    imag = imag.resize((width, height))
    imag = ImageOps.autocontrast(image=imag, cutoff=cutoff)

    for h in range(height):
        line = ""
        for w in range (width):
            pixel = imag.getpixel((w, h))
            index = pixel // y
            if index >= x:
                index = x - 1
            caracter = caracters[index]
            line += caracter
        print(line)

        
