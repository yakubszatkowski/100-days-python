from io import BytesIO
from PIL import ImageDraw
import base64, re

coordinates = {
    'Boots': [(73, 629), (324, 629)],
    'Hat': [(200, 70)],
    'Pants': [(200, 450)],
    'T-Shirt': [(210, 300)]
}


def png_to_base64(png_image):
    
    png_image.convert('RGB')
    buffer_stickman = BytesIO()
    png_image.save(buffer_stickman, 'PNG')
    buffer_stickman.seek(0)
    stickman_image_base64 = base64.b64encode(buffer_stickman.getvalue()).decode('utf-8')

    return stickman_image_base64


def fill_color(base_img, item, color):
    item_coordinates = coordinates[item]
    rgb_tuple = tuple(map(int, re.findall(r'\d+', color)))
    for coordinate in item_coordinates:
        ImageDraw.floodfill(base_img, xy=coordinate, value=rgb_tuple)
    return base_img
    