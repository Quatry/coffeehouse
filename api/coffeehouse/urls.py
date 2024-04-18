from django.urls import path

from api.coffeehouse.views import CoffeeHouseListAPIView, CoffeeHouseCreateAPIView, CoffeeHouseRetrieveAPIView, \
    CoffeeHouseRetriveUpdateDestroyAPIView

urlpatterns = [
    path('', CoffeeHouseListAPIView.as_view()),
    path('add_coffee_house', CoffeeHouseCreateAPIView.as_view()),
    path('<slug:slug>/', CoffeeHouseRetrieveAPIView.as_view()),
    path('<slug:slug>/edit', CoffeeHouseRetriveUpdateDestroyAPIView.as_view()),
]
