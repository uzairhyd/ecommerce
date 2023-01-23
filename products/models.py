from django.db import models
import random
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 39102209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{final_filename}".format(final_filename=final_filename)

# Create your models here.

class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    #image       = models.ImageField(upload_to='products/', null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    objects = ProductManager()
    def __str__(self):
        return self.title
