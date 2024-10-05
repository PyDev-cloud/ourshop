from django.db import models
from User.models import *

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SliderItem(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider_images/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.heading


class Product(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='static/product')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    discount_price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.CharField(max_length=500)
    aditional_information=models.CharField(max_length=1000)
    catagory_name=models.ForeignKey(Category,related_name="catagory", on_delete=models.CASCADE )
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE)
    quantity=models.DecimalField(max_digits=100,decimal_places=2)
    feature=models.BooleanField(default=True)
    active=models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.title
    
    @property
    def related(self):
        return self.catagory_name.catagory.all().exclude(pk=self.pk)
    

class Cart(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)