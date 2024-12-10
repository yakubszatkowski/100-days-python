from app_stickmanshop.models import SavedStickman
from .models import UserPayment
import stripe


def checkout(checkout_session_id):
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer_id = session.customer
    user_payment = UserPayment.objects.get(stripe_checkout_id=checkout_session_id)
    user_payment.stripe_customer_id = customer_id
    user_payment.payment_bool = True
    user_payment.save()

    user_stickman = SavedStickman.objects.filter(id=user_payment.stickman_id).first()
    user_stickman.payment_bool = True
    user_stickman.save()