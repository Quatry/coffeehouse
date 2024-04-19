from django.urls import path

from api.coffeehouse.views import CoffeeHouseListAPIView, CoffeeHouseCreateAPIView, \
    CoffeeHouseRetrieveUpdateDestroyAPIView, CoffeeHouseMenuListAPIView

urlpatterns = [
    path('', CoffeeHouseListAPIView.as_view()),
    path('add_coffee_house', CoffeeHouseCreateAPIView.as_view()),
    path('<slug:slug>/', CoffeeHouseMenuListAPIView.as_view()),
    path('<slug:slug>/edit', CoffeeHouseRetrieveUpdateDestroyAPIView.as_view()),
]
