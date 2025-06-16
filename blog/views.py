from .serializers import SectionSerializer , PostSerializer, MinimalPostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Section, Post


class PostViewSet(viewsets.ViewSet):
    """
    For the posts
    """
    lookup_field = 'url'  # Use 'slug' as the custom lookup field

    def list(self, request):
        queryset = Post.objects.filter(is_public=True)
        serializer = MinimalPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, url=None):
        try:
            post = Post.objects.get(is_public=True, url=url)
        except Post.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)
        serializer = PostSerializer(post)
        return Response(serializer.data)

