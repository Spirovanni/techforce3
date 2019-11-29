from django.db import models


class Organisation(models.Model):
    orgName = models.CharField(max_length=32)
    orgDescription = models.TextField(max_length=360)


class Rating(models.Model):
    organisation = models.ForeignKey(Organisation)
