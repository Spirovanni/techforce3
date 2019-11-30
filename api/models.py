from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Organisation(models.Model):
    orgName = models.CharField(max_length=32)
    orgDescription = models.TextField(max_length=360)


class Rating(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'organisation'),)
        index_together = (('user', 'organisation'),)
