from .serializers import SectionSerializer , PostSerializer, MinimalPostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Section, Post



class PostViewSet(viewsets.ViewSet):
    """
    For the posts
    """
    def list(self , request):
        queryset = Post.objects.filter(is_public=True)
        serializer = MinimalPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.filter(is_public=True)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
  

