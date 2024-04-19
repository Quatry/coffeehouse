from django.urls import path

from api.menu.views import MenuCreateAPIView, MenuListAPIView, MenuRetrieveDestroyUpdateAPIView

urlpatterns = [
    path('add/', MenuCreateAPIView.as_view()),
    path('<slug:slug>/', MenuListAPIView.as_view()),
    path('<slug:slug>/edit/', MenuRetrieveDestroyUpdateAPIView.as_view()),
]
