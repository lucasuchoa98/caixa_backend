from .models import Venda, Item

from .serializers import ItemSerializer

#from rest_framework.decorators imoport api_view
from rest_framework.views import APIView
from rest_framework.response import Response

#@api_view(['GET'])
#def todos_itens(request):
#    """
#    Lista todos os itens criados
#    """
#    if request.method == 'GET':
#        itens = Item.objects.all()
#        serializer = ItemSerializer(itens, many= True)
#        return Response(serializer.data)

class ItemListApiView(APIView):

    def get(self, request, *args, **kwargs):
        itens = Item.objects.all()
        serializer = ItemSerializer(itens, many=True)
        return Response(serializer.data)