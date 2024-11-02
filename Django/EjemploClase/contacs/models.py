from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}  {self.lastName}"


class Person(Contact):
    work = models.CharField(max_length=250)
