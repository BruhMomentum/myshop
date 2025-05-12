from django.db import models

class Product(models.Model):
    productname = models.CharField(max_length=30, verbose_name='Название товара')
    company = models.CharField(max_length=20, verbose_name='Компания')
    productcount = models.IntegerField(default=0, verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    isdiscounted = models.BooleanField(default=False, verbose_name='Со скидкой')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение товара')
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"Товар = '{self.productname}'\nКомпания = '{self.company}'\nЦена = {self.price}\n\n"
