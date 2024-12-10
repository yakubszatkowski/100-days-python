from .models import SavedStickman

def save_stickman(request, name):
    last_item_data = request.session.get('last_item_data', None)
    last_image_data = request.session.get('last_image_data', None)
    last_price = request.session.get('last_price', None)
    if last_item_data:
        stickman = SavedStickman(
            stickman_name=name, 
            stickman_clothes=last_item_data,
            stickman_img_base64=last_image_data,
            price=last_price
        )
        stickman.save()
        request.user.saved_stickmen.add(stickman)
        request.session['last_item_data'] = None
        request.session['last_image_data'] = None
        request.session['last_price'] = None

        return stickman.id


def stickman_pricing(items):
    final_price = 0.50
    for item in items:
        color = items[item]
        item_price = 0.20
        color_price = 0.10 if color != 'rgb(255, 255, 255)' else 0
        final_price += item_price + color_price

    return f'{final_price:.2f}'