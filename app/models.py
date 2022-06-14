from django.db import models

# Create your models here.


class StoreImg(models.Model):
    img = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name}"
