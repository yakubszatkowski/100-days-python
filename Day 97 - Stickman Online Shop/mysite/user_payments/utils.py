from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from base64 import b64decode
from io import BytesIO
from PIL import Image

def send_email_stickman(session, user_stickman):

    # Email details
    subject = f'{user_stickman.stickman_name} now belongs to you!'
    html_message = render_to_string("purchase_successful.html", {'stickman': user_stickman})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = [session['customer_details']['email']]

    # Convert base64 string to an image
    imgdata = b64decode(user_stickman.stickman_img_base64)
    img = Image.open(BytesIO(imgdata))

    # Save the image in memory buffer as PNG
    png_buffer = BytesIO()
    img.save(png_buffer, format='PNG')
    png_buffer.seek(0)

    # Create email
    email = EmailMultiAlternatives(
        subject, 
        plain_message, 
        from_email, 
        to
    )

    # Attach image to the e-mail
    email.attach(
        filename=f'{user_stickman.stickman_name}.png',
        content=png_buffer.read(),
        mimetype='image/png'
    )

    # Send
    email.attach_alternative(html_message, "text/html")
    email.send()
    