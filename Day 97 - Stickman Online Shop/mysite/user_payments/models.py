from django.db import models
from app_stickmanshop.models import SavedStickman
from register.models import AppUser


class UserPayment(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    stickman_id = models.OneToOneField(
        SavedStickman,
        on_delete=models.CASCADE
    )
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=255)
    stripe_customer_id = models.CharField(max_length=255)
    stripe_product_id = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} - {self.stripe_checkout_id} - Paid: {self.payment_bool}'
