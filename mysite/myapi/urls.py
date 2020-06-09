from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from . import views

router = routers.DefaultRouter()
router.register(r'comment', views.CommentViewSet)
router.register(r'like', views.LikeViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='login'),
    path('post/', views.post, name='login'),
    path('followers/', views.follow, name='followers'),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]