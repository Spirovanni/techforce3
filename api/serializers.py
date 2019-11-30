from rest_framework import serializers
from .models import Organisation, Rating


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Organisation
        fields = ('id', 'orgName', 'orgDescription')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Rating
        fields = ('id', 'stars', 'organisation', 'user')
