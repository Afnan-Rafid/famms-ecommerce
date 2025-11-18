from django.db import models

# Create your models here.
class Product(models.Model):
    img = models.ImageField(upload_to='media/product_img/', blank=True, null=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name