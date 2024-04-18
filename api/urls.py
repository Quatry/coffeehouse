from django.urls import path, include

urlpatterns = [
    path('', include('api.coffeehouse.urls')),
    path('<slug:c_h_slug>/menu/', include('api.menu.urls')),
    path('<slug:c_h_slug>/menu/<slug:menu_slug>/items/', include('api.menuitem.urls')),
]
