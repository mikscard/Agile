from django.db import models

# Create your models here.
class Value(models.Model):
    value_text = models.CharField(max_length=200)

    def __str__(self):
        return self.value_text


class Characteristic(models.Model):
    characteristic_text = models.CharField(max_length=200)

    def __str__(self):
        return self.characteristic_text
