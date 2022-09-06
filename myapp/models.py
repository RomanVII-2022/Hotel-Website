from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.image


class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    no_of_people = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length= 300)
    message = models.TextField()


    def __str__(self):
        return self.name + ' - ' + self.subject