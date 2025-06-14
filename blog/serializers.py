from rest_framework import serializers
from .models import Section, Post


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"


class MinimalPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
       