from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from api.menu.serializers import MenuSerializer
from api.menuitem.serializers import MenuItemSerializer
from api.models import Menu, MenuItem


class MenuCreateAPIView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminUser, ]


class MenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny, ]

    def list(self, request, *args, **kwargs):
        menu_name = kwargs.get('slug')
        menu = Menu.objects.get(slug=menu_name)
        menu_items = MenuItem.objects.filter(menu=menu.id).all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MenuRetrieveDestroyUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUser, ]
