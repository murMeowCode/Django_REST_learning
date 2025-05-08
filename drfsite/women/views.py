from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from .models import Category, Women
from .serializers import WomenSerializer

class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
class WomenAPIList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    pagination_class = WomenAPIListPagination
    
class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    #authentication_classes = [TokenAuthentication]
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    
class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Women.objects.all()
    serializer_class = WomenSerializer