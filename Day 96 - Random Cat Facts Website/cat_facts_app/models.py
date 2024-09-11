from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FavoriteList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritelist', null=True)
    favorite_cat_id = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.favorite_cat_id}"