from rest_framework import serializers
from . import models


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organisation
        fields = ['id', 'orgName', 'orgDescription']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = ['id', 'stars', 'user', 'organisation']
