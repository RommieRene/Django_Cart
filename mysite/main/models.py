from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category name', max_length=(50))\
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Cartegory"
        verbose_name_plural = 'Categories'

class Product(models.Model):
    pass

class Contact(models.Model):
    pass
class Cart(models.Model):
    pass