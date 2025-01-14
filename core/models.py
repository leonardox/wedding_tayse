import os

from django.db import models


# Create your models here.
class Present(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="presents", verbose_name="Presentes")

    def delete(self, *args, **kwargs):
        # Delete the file from storage
        file_path = self.image.path
        if os.path.exists(file_path):
            os.remove(file_path)
        super().delete(*args, **kwargs)
