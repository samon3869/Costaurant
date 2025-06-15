from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    img_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name