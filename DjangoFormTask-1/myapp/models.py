from django.db import models

# Create your models here.

class Form(models.Model):
    #relation
    user = models.ForeignKey('Users', on_delete=models.CASCADE, related_name="forms")
    #moderator
    email = models.EmailField(),
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipp = models.CharField(max_length=50)
    check_me = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Users(models.Model):
    #moderator
    fullname = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname