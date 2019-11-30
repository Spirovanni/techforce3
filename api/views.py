from rest_framework import viewsets
from .models import Organisation, Rating
from .serializers import OrganisationSerializer, RatingSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = (OrganisationSerializer, )


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = (RatingSerializer, )
