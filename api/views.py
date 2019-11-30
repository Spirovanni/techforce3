from rest_framework import viewsets
from .models import Organisation, Rating
from .serializers import OrganisationSerializer, RatingSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

