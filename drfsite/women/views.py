from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import WomenSerializer
from .models import Women

class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all()
        return Response({'posts':WomenSerializer(lst,many = True).data})
    
    def post(self, request):
        serializer = WomenSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        
        post_new = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )
        return Response({'post':WomenSerializer(post_new).data})