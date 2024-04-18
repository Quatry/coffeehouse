from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from api.coffeehouse.serializers import CoffeeHouseSerializer
from api.models import CoffeeHouse


class CoffeeHouseListAPIView(generics.ListAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    permission_classes = [AllowAny, ]


class CoffeeHouseCreateAPIView(generics.CreateAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    permission_classes = [IsAdminUser, ]


class CoffeeHouseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny, ]


class CoffeeHouseRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUser, ]
