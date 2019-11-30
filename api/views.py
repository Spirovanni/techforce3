from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Organisation, Rating
from .serializers import OrganisationSerializer, RatingSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()

    @action(detail=True, methods=['POST'])
    def rate_organisation(self, request, pk=None):
        if 'stars' in request.data:

            organisation = Organisation.objects.get(id=pk)
            stars = request.data['stars']
            user = User.objects.get(id=2)
            # user = request.user
            # print('Organisation Name', organisation.orgName)
            print('user', user.username)

            try:
                rating = Rating.objects.get(user=user.id, organisation=organisation.id)
                rating.stars = stars
                rating.save()
            except:
                Rating.objects.create(user=user, organisation=organisation, stars=stars)
            response = {'message': 'its working'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
