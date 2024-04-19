from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from api.coffeehouse.serializers import CoffeeHouseSerializer
from api.menu.serializers import MenuSerializer
from api.menuitem.serializers import MenuItemSerializer
from api.models import CoffeeHouse, Menu, MenuItem


class CoffeeHouseListAPIView(generics.ListAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    permission_classes = [AllowAny, ]


class CoffeeHouseCreateAPIView(generics.CreateAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    permission_classes = [IsAdminUser, ]


class CoffeeHouseMenuListAPIView(generics.ListAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny, ]

    def list(self, request, *args, **kwargs):
        coffeehouse_slug = kwargs.get('slug')
        coffeehouse_obj = CoffeeHouse.objects.get(slug=coffeehouse_slug)
        data = list()
        menu_list = Menu.objects.filter(coffeehouse=coffeehouse_obj).all()
        for item in menu_list:
            menu_serializer = MenuSerializer(item, many=False).data
            menu_items = MenuItem.objects.filter(menu=item.id).all()
            menu_item_serializer = MenuItemSerializer(menu_items, many=True).data
            data.append(menu_serializer)
            data.append(menu_item_serializer)
        return Response(data, status=status.HTTP_200_OK)


class CoffeeHouseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUser, ]
