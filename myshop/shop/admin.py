from django.contrib import admin
from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}  # 1

# 1. атрибут prepopulated_fields используется для того,
#    чтобы указывать поля, значение которых устанавливается
#    автоматически с использованием значения других полей.
#    это удобно для генерирования слагов
