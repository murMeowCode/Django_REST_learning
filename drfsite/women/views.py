from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.views import APIView
from .serializers import WomenSerializer
from .models import Women
import logging


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    
class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    
    
# class WomenAPIView(APIView):
#     def get(self, request):
#         lst = Women.objects.all()
#         return Response({'posts':WomenSerializer(lst,many = True).data})
    
#     def post(self, request):
#         serializer = WomenSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post':serializer.data})
    
#     def put(self,requset,*args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = WomenSerializer(data=requset.data,instance = instance)
#         serializer.is_valid()
#         serializer.save()
#         return Response(status=status.HTTP_200_OK)