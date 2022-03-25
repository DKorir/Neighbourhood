from django.db import models
from django.contrib.auth.models import User
class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    description = models.TextField()
    health_info = models.IntegerField(null=True, blank=True)
    health_officer = models.CharField(max_length=60, null=True, blank=True)
    police_info = models.IntegerField(null=True, blank=True)
    police_officer = models.CharField(max_length=60, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="neighbourhood")
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    def create_neighbourhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)


class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact = models.EmailField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    def __str__(self):
        return f'{self.user.username} Profile'
