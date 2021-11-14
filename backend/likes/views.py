from rest_framework import viewsets
from .models import Likes
from .serializers import LikesSerializer
# Create your views here.

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

