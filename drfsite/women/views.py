from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Women
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    """_summary_

    Args:
        viewsets (_type_): _description_

    Returns:
        _type_: _description_
    """
    serializer_class = WomenSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Women.objects.all()[:3]
        else:
            return Women.objects.filter(pk = pk)
    
    @action(methods = ['get'], detail = True)
    def category(self, request, pk = None):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        cats = Category.objects.get(pk=pk)
        return Response({'cats':cats.name})