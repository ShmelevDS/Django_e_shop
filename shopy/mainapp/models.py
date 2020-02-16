from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя продукта", max_length=128)
    image = models.ImageField(upload_to="products_images", blank=True)
    short_desc = models.CharField(verbose_name="краткое описание продукта", max_length=60, blank=True)
    full_desc = models.TextField(verbose_name="описание продукта", blank=True)
    price = models.DecimalField(verbose_name="цена продукта", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="количество на складе", default=0)
    size = models.CharField(verbose_name="размер", max_length=30)
    brand = models.CharField(verbose_name="производитель", max_length=100)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class IconCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name


class Icon(models.Model):
    category = models.ForeignKey(IconCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    image = models.ImageField(upload_to="icons_images", blank=True)
    text = models.CharField(verbose_name="значение", max_length=100, blank=True)

    def __str__(self):
        return self.name
