from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=50, unique=True) 
    slug = models.SlugField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.cat_name


