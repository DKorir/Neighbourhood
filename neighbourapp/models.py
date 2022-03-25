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

    def __str__(self):
        return self.name

    def create_neighbourhood(self):
        self.save()
        
    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)