import os

from django.db import models


# Create your models here.
class Present(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="presents", verbose_name="Presentes")

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Delete the file from storage
        file_path = self.image.path
        if os.path.exists(file_path):
            os.remove(file_path)
        super().delete(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)

    def __str__(self):
        return self.name


class Indication(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to="indication", verbose_name="Imagem")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Delete the file from storage
        file_path = self.image.path
        if os.path.exists(file_path):
            os.remove(file_path)
        super().delete(*args, **kwargs)
