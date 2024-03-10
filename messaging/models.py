from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='conversation')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='Open')

    def get_absolute_url(self):
        return reverse('conversation_detail', kwargs={'conversation_id': self.id})

    def __str__(self):
        return f"Conversation about {self.product.title}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.sent_at}"

    class Meta:
        ordering = ['sent_at']