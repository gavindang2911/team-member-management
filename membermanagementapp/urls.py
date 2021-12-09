from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='membermangement-index'),
    path('addItem', views.add_item, name='membermangement-add-item')
]