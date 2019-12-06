from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser


# class Organisation(models.Model):
#     orgName = models.CharField(max_length=32)
#     orgDescription = models.TextField(max_length=360)
#
#     def no_of_ratings(self):
#         ratings = Rating.objects.filter(organisation=self)
#         return len(ratings)
#
#     def avg_ratings(self):
#         sum = 0
#         ratings = Rating.objects.filter(organisation=self)
#         for rating in ratings:
#             sum += rating.stars
#         if len(ratings) > 0:
#             return sum / len(ratings)
#         else:
#             return 0
#
#
# class Rating(models.Model):
#     organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#
#     class Meta:
#         unique_together = (('user', 'organisation'),)
#         index_together = (('user', 'organisation'),)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField(unique=True, primary_key=True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=40)

    first_name = models.CharField(default='', max_length=15)
    last_name = models.CharField(default='', max_length=15)
    login = models.CharField(max_length=15)
    age = models.IntegerField()
    street = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    zip = models.CharField(blank=True, max_length=10)
    role = models.CharField(default='', max_length=10)

    USERNAME_FIELD = 'id'


class UserSettings(models.Model):
    id = models.OneToOneField(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              primary_key=True)
    theme = models.CharField(max_length=10)