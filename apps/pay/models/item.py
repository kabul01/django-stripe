from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    description = models.CharField(max_length=400, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    file = models.FileField(upload_to="product_files/", blank=True, null=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'Products'
        ordering = ["-id"]
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
