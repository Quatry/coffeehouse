from django.urls import path

from api.menu.views import MenuCreateAPIView, MenuRetrieveAPIView, MenuRetrieveDestroyUpdateAPIView

urlpatterns = [
    path('add/', MenuCreateAPIView.as_view()),
    path('<slug:slug>/', MenuRetrieveAPIView.as_view()),
    path('<slug:slug>/edit/', MenuRetrieveDestroyUpdateAPIView.as_view()),
]
