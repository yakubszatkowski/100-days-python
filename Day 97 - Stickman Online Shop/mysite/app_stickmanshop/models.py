from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SavedStickman(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_stickmen', null=True) 
    stickman_name = models.CharField(max_length=20)
    stickman_clothes = models.JSONField()
    stickman_img_base64 = models.CharField(max_length=60000)
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.user.username} - {self.stickman_name}"
