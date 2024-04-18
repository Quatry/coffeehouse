from django.urls import path

from api.menuitem.views import MenuItemCreateAPIView, MenuItemRetrieveAPIView, MenuItemRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('add/', MenuItemCreateAPIView.as_view()),
    path('<slug:id>/', MenuItemRetrieveAPIView.as_view()),
    path('<slug:id>/edit/', MenuItemRetrieveUpdateDestroyAPIView.as_view()),
]
