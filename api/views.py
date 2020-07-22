from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated # IsAuthenticatedOrReadOnly


from .serializers import NameSerializer, UserSerializer, ProfileFeedSerializer
from . import models
from . import permissions


class hello_api(APIView):
    """ A hello message API  """
    serializer_class = NameSerializer

    def get(self, request, format  = None):
        an_apiview = [
            'This is a trial list to create a object file',
            'This can almost correspond to above data',
            'This is a list created waiting for FCB vs Valadollid Game'
        ]
        return Response({
            'message' : ' Hello to the first program!',
            'an_apiview' : an_apiview
        })

    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                'message' : message
            })
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
            
    def put(self, request, pk = None): 
        """ Handle the completely updating the function """
        #The PK is usually used to receive the Key value passed in the url p.s. Not in this case
        # The value not given results in 'BLANK' field 
        return Response({"message" : "Still to complete PUT function"})


    def patch(self, request, pk = None): 
        """ Handle partially updating the function """
        #The PK is usually used to receive the Key value passed in the url p.s. Not in this case
        # The value not given results in not updating field and updates only given field
        return Response({"message" : "Still to complete PATCH "})


    def delete(self, request, pk = None):
        """ Handles Deleting the given object """    

        return Response({"message" : "Still to complete DELETE"}) 


# The HelloViewSet Class
class HelloViewset(viewsets.ViewSet):
    """ Test the API ViewSet """

    serializer_class = NameSerializer

    def list(self, request):
        """ Returns a Hello message """
        a_viewset = [
            'This is a base list', 
            'The viewset uses routers for routing purpose',
            'Viewset is less code work done way of creating API',
        ]
        return Response({
            "message" : "Hello from the viewset",
            "a_viewset" : a_viewset,
        })


    def create(self, request):
        """ Create a new Hello Object   """
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({
                "message" : message
            })
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk = None):
        """ For retrieving an object """
        # Your Logic Here
        return Response({
            "message" : "The retrieve function"
        })

        
    def update(self, request, pk = None):
        """ For Updating an object """
        # Your Logic Here
        return Response({
            "message" : "YOUR Update(PUT) function here"
        })


    def partial_update(self, request, pk = None):
        """ For partially updating an object """
        # Your Logic Here
        return Response({
            "message" : "YOUR Update(PATCH) function here"
        })

    
    def destroy(self, request, pk = None):
        """ For destroying or deleting an object"""
        # Your logic Here
        return Response({
            "message" : "Your Destroy(DELETE) function here."
        })


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Creates and updates the User profile """
    serializer_class = UserSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication ,) # It is a tuple
    permission_classes = (permissions.UserProfilePermissions,) # It is a tuple
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """ Handles creating user authentication token """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class  ProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles the CRUD of Profile feed """
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedSerializer
    queryset = models.ProfileFeed.objects.all()
    permission_classes = (
        permissions.ProfileFeedPermission,
        IsAuthenticated,
    )

    def perform_create(self, serializer):
        """ Sets the user profile to the request.user or current user """
        serializer.save(user_profile = self.request.user)