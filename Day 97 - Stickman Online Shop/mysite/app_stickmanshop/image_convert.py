from io import BytesIO
import base64


def png_to_base64(png_image):
    
    png_image.convert('RGB')
    buffer_stickman = BytesIO()
    png_image.save(buffer_stickman, 'PNG')
    buffer_stickman.seek(0)
    stickman_image_base64 = base64.b64encode(buffer_stickman.getvalue()).decode('utf-8')

    return stickman_image_base64
