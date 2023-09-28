from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    url = models.URLField(max_length=200, unique=True)
    phone = models.CharField(max_length=30)
    image = models.ImageField(upload_to='contacts/', blank=True, null=True)

    class Meta:
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
