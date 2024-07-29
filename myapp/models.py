from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.email} - {self.password}"