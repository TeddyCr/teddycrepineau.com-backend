from django.shortcuts import render
from django.contrib.auth.models import User
from project.api.models import Posts
from project.api.permission import IsOwnerAdminOrReadOnly
from rest_framework import viewsets, serializers, permissions, mixins
from project.api.serializers import UserSerializer, PostsSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostsViewSet(viewsets.ModelViewSet):

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerAdminOrReadOnly,)
    http_method_names = ['get', 'options','post','head', 'put', 'delete']

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user)