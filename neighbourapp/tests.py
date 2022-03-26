from django.test import TestCase
from django.test import TestCase
from .models import Post,Neighbourhood,Profile,User
class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user = Profile(user='Levy')
        self.user.save()
        self.user_profile = Profile(user=self.user, profile_picture="image.png", bio="My bio")
    def tearDown(self):
        Profile.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.user_profile,Profile))