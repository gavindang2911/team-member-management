from django.urls import path
from .views import MemberList, MemberCreate, MemberUpdate
# from . import views

urlpatterns = [
    # path('', views.index, name='membermangement-index'),
    path('', MemberList.as_view(), name='membermangement-index'),
    path('addMember/', MemberCreate.as_view(), name='membermangement-add-item'),
    path('edit/<int:pk>/', MemberUpdate.as_view(), name='membermangement-edit-item'),
    # path('edit/<int:pk>/', views.edit, name='membermangement-edit-item'),
    # path('delete/<int:pk>/', views.delete, name='membermangement-delete-item')
]