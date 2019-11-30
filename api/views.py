from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Organisation, Rating
from .serializers import OrganisationSerializer, RatingSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class OrganisationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()
    authentication_classes = (TokenAuthentication, )

    @action(detail=True, methods=['POST'])
    def rate_organisation(self, request, pk=None):
        if 'stars' in request.data:

            organisation = Organisation.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print('user ', user)

            try:
                rating = Rating.objects.get(user=user.id, organisation=organisation.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Ratings Updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                Rating.objects.create(user=user, organisation=organisation, stars=stars)
                response = {'message': 'Ratings Created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    authentication_classes = (TokenAuthentication, )
