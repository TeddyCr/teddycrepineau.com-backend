# from django.contrib.auth.models import User
from project.api.models import Posts, Profile
from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True
                                    , queryset=Posts.objects.all()
                                    )

    class Meta:
        model = Profile
        fields = ('id','url','profile_picture_url','first_name', 'last_name', 'short_bio','long_bio', 'posts')

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    author_id = serializers.ReadOnlyField(source='author_id.username')

    class Meta:
        model = Posts
        fields = ('id','slug','author_id','full_name', 'title', 'content','tags',
                 'creation_date', 'last_modified','is_published')


