from django.conf import settings
from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.subject + " from: " + self.name
