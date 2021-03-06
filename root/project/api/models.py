from django.db import models
from django.contrib.auth.models import User
from  django.contrib.postgres.fields import ArrayField
from teddycrepineau import settings
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from tinymce.models import HTMLField
from django.db import models

class Posts(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    content = HTMLField()
    tags = ArrayField(
            models.CharField(max_length=20, blank=True
            , help_text="Enter a tag related to your post"),
            size=4,
           )
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False) 
    slug = models.SlugField(max_length=100, blank=True)

    def _get_full_name(self):
        return self.author_id.get_full_name()

    full_name = property(_get_full_name)

    class Meta:
        db_table = 'posts'
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_bio = HTMLField(blank=True, null=True)
    long_bio = HTMLField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='uploads/%Y/%m/%d/',
                                        blank=True, null=True)

    def _get_first_name(self):
        return self.user.first_name

    def _get_last_name(self):
        return self.user.last_name

    def _get_username(self):
        return self.user.username
    
    def _get_posts(self):
        return self.user.posts

    def _get_profile_picture_url(self):
        return f'{self.profile_picture.url}'

    first_name = property(_get_first_name)
    last_name = property(_get_last_name)
    username = property(_get_username)
    posts = property(_get_posts)
    profile_picture_url = property(_get_profile_picture_url)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class UserManager(BaseUserManager):
    def create_super_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have a valid email address')

        if not kwargs.get('username'):
            raise ValueError('User must have a valid username')

        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username')
        )

        account.set_password(password)
        account.is_admin = True
        account.is_active = True
        account.is_staff = True
        account.save()

        return account


class Users(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=40,
        unique=True,
    )
    slug = models.SlugField(max_length=60)

    name = models.CharField(
        verbose_name='Full Name',
        max_length=120,
        blank=True
    )
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    



