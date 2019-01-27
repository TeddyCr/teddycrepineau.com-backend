from django.urls import re_path, include, path
from rest_framework import routers
from project.api import views
from rest_framework_simplejwt.views import (
                    TokenObtainPairView
                    , TokenRefreshView
                    , TokenVerifyView
                    )

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'posts', views.PostsViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('api-authentification/', include('rest_framework.urls')),
    re_path('token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path('token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    re_path('token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]