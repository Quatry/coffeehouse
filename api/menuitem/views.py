from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from api.menuitem.serializers import MenuItemSerializer
from api.models import MenuItem


class MenuItemCreateAPIView(generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser, ]


class MenuItemRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny, ]



class MenuItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser, ]
