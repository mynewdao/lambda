from django.db import models


class Item(models.Model):
    brand = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    condition = models.CharField(max_length=16)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.brand} {self.model} {self.price}$"


class ManyImage(models.Model):
    image = models.ImageField(upload_to='inside_img', max_length=255)
    item_img = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_images')

