from django.db import models
import django

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    date=models.DateField(django.utils.timezone.now)

    def __str__(self):
        return self.name