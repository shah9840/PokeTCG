from django.db import models

# Create your models here.
class Account(models.Model):
    identity = models.IntegerField(primary_key=True)
    username = models.TextField(max_length=100)
    password = models.TextField()

class Deck(models.Model):
    identity = models.IntegerField()
    rank = models.IntegerField()
    amount = models.IntegerField()
