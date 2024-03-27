import numpy as np

def dominant_colors_extraction(pil_image):
    image_array = np.array(pil_image)
    pixels_array = image_array.reshape((-1, 3))
    unique_values, count = np.unique(pixels_array, axis=0, return_counts=True)
    total_pixels = sum(count)
    top_10_indices = np.argsort(count)[-10:][::-1]

    list_10_dominant_colors = []
    for index in top_10_indices:
        rgb_value = tuple(unique_values[index].tolist())
        hex_value = '#%02x%02x%02x' % rgb_value
        color_percentage = round(count[index]/total_pixels*100, 6)
        list_10_dominant_colors.append((hex_value, color_percentage))

    return list_10_dominant_colors
    