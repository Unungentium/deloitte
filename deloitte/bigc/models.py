from django.db import models

# Create your models here.

class CompanyName(models.Model):
    name = models.CharField(max_length = 45, unique=True)
    def __str__(self):
        return self.name