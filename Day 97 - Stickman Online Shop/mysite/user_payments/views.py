from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from app_stickmanshop.models import SavedStickman
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
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=[
                        {
                            'quantity': 1,
                            'price_data': {
                                'currency': 'usd',
                                'unit_amount': int(user_stickman.price * 100),
                                'product': product_id,  
                            }
                        },
                    ],
                    mode='payment',
                    customer_creation='always',
                    success_url = f'{settings.BASE_URL}{reverse("payment_successful")}?session_id={{CHECKOUT_SESSION_ID}}',
                    cancel_url = f'{settings.BASE_URL}{reverse('payment_cancelled')}'
                )
                return redirect(checkout_session.url, code=303)

        return render(request, 'stickman.html', {'stickman': user_stickman})

    return render(request, 'content_unavailable.html')


def payment_successful(request):
    return render(request, 'payment_successful.html')


def payment_cancelled(request):
    return render(request, 'payment_cancelled.html')
