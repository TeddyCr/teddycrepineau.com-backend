from django.shortcuts import render
# from django.contrib.auth.models import User
from project.api.models import Posts, Profile
from project.api.permission import IsOwnerAdminOrReadOnly
from rest_framework import viewsets, serializers, permissions, mixins
from project.api.serializers import ProfileSerializer, PostsSerializer

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class PostsViewSet(viewsets.ModelViewSet):

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerAdminOrReadOnly,)
    http_method_names = ['get', 'options','head']

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user)