from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import WomenSerializer
from .models import Women

class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values_list()
        return Response({'posts':lst})
    
    def post(self, request):
        post_new = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )
        return Response({'post':model_to_dict(post_new)})