from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
