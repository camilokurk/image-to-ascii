from PIL import Image, ImageOps 

scale = 5

cutoff = 1.0

caracters = " .:-=+*#%@"

image_to_convert = "image.png"

GRAY_TONES = 256

def conversor(scale, cutoff, caracters, image_to_convert):

    x = len(caracters)

    y = GRAY_TONES // x

    with Image.open(image_to_convert) as im:
        imag = im.convert(mode = "L")
        (width, height) = (imag.width // (scale - (scale // 2)), imag.height // scale)
        imag = imag.resize((width, height))
        imag = ImageOps.autocontrast(image=imag, cutoff=cutoff)

        lines = ""

        for h in range(height):
            line = ""
            for w in range (width):
                pixel = imag.getpixel((w, h))
                index = pixel // y
                if index >= x:
                    index = x - 1
                caracter = caracters[index]
                line += caracter
            if lines == "":
                lines = line
            elif lines != "":
                lines = lines + "\n" + line

    return lines

result = conversor(scale, cutoff, caracters, image_to_convert) 

print(result)