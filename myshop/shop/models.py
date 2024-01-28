from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    #  название товара
    name = models.CharField(max_length=200)
    #  слаг этого товара для создания красивых URL-адресов
    slug = models.SlugField(max_length=200)
    # изображение товара
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    #  описание товара
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    # доступность товара
    available = models.BooleanField(default=True)
    # дата/время создания
    created = models.DateTimeField(auto_now_add=True)
    # дата/время обновления
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name
