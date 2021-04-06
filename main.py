import os
import glob
from PIL import Image, ImageFont, ImageDraw


def get_all_files():
    files = []
    for filename in glob.iglob('source-images/*.jpg', recursive=True):
        files.append(filename)
    return files


def set_author_to_picture(result):
    for img in result:
        text = os.path.basename(img)
        raw_author = text.split('.')[0].split('-')
        author = ' '.join(raw_author).title()
        author = '© ' + str(author)
        image = Image.open(img)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 16)
        font_size = font.getsize(text=author)
        x, y = image.size
        margin = 10
        position = (x - margin - font_size[0], y - margin - font_size[1])
        draw.text(position, author, (255, 255, 255), font=font)
        output_dir = './output-images/' + text
        try:
            image.save(output_dir, 'JPEG')
        except FileNotFoundError:
            os.makedirs('output-images', exist_ok=True)
            image.save(output_dir, 'JPEG')


if __name__ == '__main__':
    set_author_to_picture(get_all_files())
