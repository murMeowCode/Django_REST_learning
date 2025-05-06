from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from .models import Category, Women
from .serializers import WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    
class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [TokenAuthentication]
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    
class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Women.objects.all()
    serializer_class = WomenSerializer