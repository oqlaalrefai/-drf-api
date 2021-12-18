from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class order(models.Model):
    foodName = models.CharField(max_length=255)
    content = models.TextField()
    times = models.DateTimeField(auto_now = False, auto_now_add=True)


    def __str__(self):
        return self.foodName