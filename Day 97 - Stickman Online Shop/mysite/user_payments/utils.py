from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from io import BytesIO

def send_email_stickman(session, user_stickman):

    subject = f'{user_stickman.stickman_name} now belongs to you!'
    html_message = render_to_string("purchase_successful.html", {'stickman': user_stickman})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = [session['customer_details']['email']]


    # Convert base64 string to an image
    # Save the image in memory buffer as PNG
    buffer = BytesIO(f"data:image/jpeg;base64,{user_stickman.stickman_img_base64}")
    
    email = EmailMultiAlternatives(
        subject, 
        plain_message, 
        from_email, 
        to
    )

    # Attach image to the e-mail
    email.attach(
        
    )

    email.attach_alternative(html_message, "text/html")
    email.send()
    