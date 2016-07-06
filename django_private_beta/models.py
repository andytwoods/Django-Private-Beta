from django.db import models


class PrivateBetaModel(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()

