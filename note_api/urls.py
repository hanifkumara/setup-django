from django.urls import base, path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('login', LoginViewSet, basename='login')
router.register('register', RegisterViewSet, basename='register')
router.register('category', CategoryViewSet, basename='category')
router.register('note', NoteViewSet, basename='note')

urlpatterns = [
  path('v1/', include(router.urls))
]