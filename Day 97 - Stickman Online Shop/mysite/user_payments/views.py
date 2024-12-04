from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.conf import settings
from app_stickmanshop.models import SavedStickman
from .models import UserPayment
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
product_id = settings.PRODUCT_ID


@login_required(login_url='login')
def stickman(request, id):
    user_stickman = SavedStickman.objects.filter(id=id).first()

    if user_stickman in request.user.saved_stickmen.all():

        if request.method == "POST":
            delete = request.POST.get('delete_stickman', None)
            purchase = request.POST.get('purchase_stickman', None)

            if delete:
                user_stickman.delete()
                return redirect('collection')
            
            elif purchase:
                # Creating UserPayment object in my database
                initial_user_payment = UserPayment(
                    user = request.user,
                    stickman_id = user_stickman,
                    payment_bool = False,
                )

                # Creating Session
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types = ['card'],
                    line_items = [
                        {
                            'quantity': 1,
                            'price_data': {
                                'currency': 'usd',
                                'unit_amount': int(user_stickman.price * 100),
                                'product': product_id,  
                            }
                        },
                    ],
                    mode = 'payment',
                    customer_creation = 'always',
                    success_url = f'{settings.BASE_URL}{reverse("payment_successful")}?session_id={{CHECKOUT_SESSION_ID}}',
                    cancel_url = f'{settings.BASE_URL}{reverse('payment_cancelled')}'
                )

                # Updating rest of initial payment information based on checkout session
                initial_user_payment.stripe_checkout_id = checkout_session.id
                initial_user_payment.stripe_product_id = product_id
                initial_user_payment.save()

                return redirect(checkout_session.url, code=303)
            
        return render(request, 'stickman.html', {'stickman': user_stickman})
    
    return render(request, 'content_unavailable.html')


def payment_successful(request):
    checkout_session_id = request.GET.get('session_id', None)

    # if checkout_session_id:
    #     session = stripe.checkout.Session.retrieve(checkout_session_id)
    #     customer_id = session.customer

    #     user_payment = UserPayment.objects.get(stripe_checkout_id=checkout_session_id)
    #     user_payment.stripe_customer_id = customer_id
    #     user_payment.payment_bool = True
    #     user_payment.save()

    return render(request, 'payment_successful.html')


def payment_cancelled(request):
    return render(request, 'payment_cancelled.html')


# TEST WITH CLI
# stripe login --api-key *APIKEY*
# # stripe listen --forward-to http://127.0.0.1:8000/payment/stripe_webhook

import logging
logger = logging.getLogger(__name__)

@require_POST
@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    payload = request.body
    signature_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    try:
        event = stripe.Webhook.construct_event(payload, signature_header, endpoint_secret)
    except ValueError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        print('worked')
        session = event['data']['object']
        checkout_session_id = session.get('id')
        user_payment = UserPayment.objects.get(stripe_checkout_id=checkout_session_id)
        user_payment.stripe_customer_id = session.get('customer')
        user_payment.payment_bool = True
        user_payment.save()
        print('worked')

    return HttpResponse(status=200)
