from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='membermangement-index'),
    path('addMember', views.add_item, name='membermangement-add-item'),
    path('edit/<int:pk>/', views.edit, name='membermangement-edit-item')
]