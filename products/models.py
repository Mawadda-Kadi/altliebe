from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)

# Choices Fields
CATEGORY = (
    (0, "Electronics"),
    (1, "Fashion and Apparel"),
    (2, "Home and Garden"),
    (3, "Sports and Outdoors"),
    (4, "Toys and Games"),
    (5, "Books and Media"),
    (6, "Pet Supplies"),
    (7, "Others"),
)

AVAILABILITY = (
    (0, "available"), (1, "reserved"), (2, "sold")
)

STATUS = (
    (0, "used"), (1, "new"), (2, "handmade")
)

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField(
        'image', default='static/images/product-default-image.jpg')
    category = models.IntegerField(choices=CATEGORY, default=0)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products")
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    availability = models.IntegerField(choices=AVAILABILITY, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.product.title}"


class Wishlist(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='wished_by')
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent duplicate wishlist items for the same user
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username}'s wishlist"
