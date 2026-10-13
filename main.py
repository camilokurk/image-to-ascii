from PIL import Image

scale = 10

caracters = " .:-=+*#%@"

with Image.open("image.png") as im:
    imag = im.convert(mode = "L")
    (width, height) = (imag.width // (scale - (scale // 2)), imag.height // scale)
    imag = imag.resize((width, height))
    print(imag)

    for h in range(height):
        line = ""
        for w in range (width):
            pixel = imag.getpixel((w, h))
            index = pixel // 28
            caracter = caracters[index]
            line += caracter
        print(line)
        
