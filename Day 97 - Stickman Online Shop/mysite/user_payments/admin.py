from django.contrib import admin
from .models import UserPayment

class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_bool', 'stripe_checkout_id', 'stripe_customer_id', 'stripe_product_id'] 


admin.site.register(UserPayment, UserPaymentAdmin)
