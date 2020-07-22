from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', HelloViewset, basename = 'hello-viewset-base')
router.register('profiles-api', UserProfileViewSet)
router.register('profile-feed', ProfileFeedViewSet )

urlpatterns = [
    path('hello-view/',hello_api.as_view()),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)), #router here is a instance created of DefaultRouter not router itself
]