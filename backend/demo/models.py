from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=18, decimal_places=0, validators=[MinValueValidator(1)])


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name="orders", through="OrderPosition")


class OrderPosition(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="positions")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="positions")
    qty = models.IntegerField(validators=[MinValueValidator(1)], default=1)
