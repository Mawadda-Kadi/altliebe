from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='conversations')
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product.title + '-' + str(self.id))
        super().save(*args, **kwargs)

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