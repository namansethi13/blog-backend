from django.urls import path 
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'', PostViewSet , basename='post')


urlpatterns = router.urls
