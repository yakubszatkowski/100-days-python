from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SavedStickman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # , related_name=''
    stickman_name = models.CharField(max_length=20)
    stickman_data = models.JSONField('Stickman parameters')

    def __str__(self) -> str:
        return f"{self.user.username} - {self.stickman_data}"
