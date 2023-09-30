from django.db import models


class ContactBook(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    url = models.URLField(max_length=200, unique=True)
    phone = models.CharField(max_length=30)
    image = models.ImageField(upload_to='contacts_event/', blank=True, null=True)

    class Meta:
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Events(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    dat_time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=30)
    contact_book = models.ManyToManyField(ContactBook, related_name='contact_event')

    def __str__(self):
        return self.title

