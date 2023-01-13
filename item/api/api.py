from item.models import Item
from rest_framework import viewsets, permissions
from item.api.serializers import ItemSerializers


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ItemSerializers

