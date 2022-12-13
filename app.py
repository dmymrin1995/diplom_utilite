from PIL import Image, ImageDraw, ImageFont
import pandas as pd

data = pd.read_csv('static/names.csv')

name_list = data['names'].tolist()



path_to_font = './static/Montserrat-Bold.ttf'
path_to_image = './static/static2.png'

def create_diplom (path_to_font, path_to_image, names):
    for names in names:
        font = ImageFont.truetype(path_to_font, 104)
        img = Image.open(path_to_image, mode ="r")
        image_width = img.width
        image_height = img.height 
        draw = ImageDraw.Draw(img)
        text_width, _ = draw.textsize(names, font = font)
        draw.text(((image_width - text_width) / 2, 1425), names, font=font, fill=(0, 0, 0))
     return img.save("{}.png".format(names))

if __name__ == "__main__":
    create_diplom (path_to_font, path_to_image, name_list)
