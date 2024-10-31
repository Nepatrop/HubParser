from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add_hub/', views.add_hub, name='add_hub'),
    path('edit_hub/<int:hub_id>/', views.edit_hub, name='edit_hub'),
    path('delete_hub/<int:hub_id>/', views.delete_hub, name='delete_hub'),
]