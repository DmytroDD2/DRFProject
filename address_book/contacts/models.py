from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    url = models.URLField(max_length=200)
    phone = models.CharField(max_length=30)
    image = models.ImageField(upload_to='contacts/', blank=True, null=True)

    class Meta:
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}' + "Example"


class ContactGroup(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.ManyToManyField(Contact, related_name='contact_groups')

    def __str__(self):
        return self.name


class ContactActivityLog(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50, choices=[('CREATED', 'Created'), ('EDITED', 'Edited')])
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.contact} was {self.activity_type}: {self.timestamp}"


@receiver(post_save, sender=Contact)
def create_contact_activity_log(sender, instance, created, **kwargs):
    if created:
        activity_type = 'CREATED'
    else:
        activity_type = 'EDITED'

    ContactActivityLog.objects.create(
        contact=instance,
        activity_type=activity_type,
        details=f"Contact {instance} was created."
    )
