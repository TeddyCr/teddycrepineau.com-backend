from django.contrib.auth.models import User
from project.api.models import Posts
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True
                                    , queryset=Posts.objects.all()
                                    )

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'posts')

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    author_id = serializers.ReadOnlyField(source='author_id.username')

    class Meta:
        model = Posts
        fields = ('url','author_id', 'title', 'content', 'tags', 'creation_date'
                 , 'last_modified')


