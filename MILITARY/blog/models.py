from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Feed(models.Model):
    name = models.CharField(max_length=225)
    email= models.EmailField(max_length=225)
    Message =models.TextField()


    def __str__(self):
        return self.name


# class PersoneInfo(models.Model):
#     first_name = models.CharField(max_length=225)
#     last_name = models.CharField(max_length=225)
#     email = models.EmailField(max_length=225)
#     branch = models.CharField(max_length=225)
#     rank = models.CharField(max_length=225)
#     date_of_birth = models.DateTimeField()
#     year_into_service = models.DateTimeField()
#     matricule = models.ForeignKey(User, on_delete=models.CASCADE )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('realhome', args=[str(self.id)])