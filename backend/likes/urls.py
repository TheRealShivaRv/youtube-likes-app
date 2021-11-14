from django.urls import path,include
from rest_framework import routers
from .views import LikesViewSet

router = routers.DefaultRouter()
router.register('likes', LikesViewSet)

urlpatterns = router.urls
