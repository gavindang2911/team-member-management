from django.urls import path
from .views import MemberList, MemberCreate, MemberUpdate, MemberDelete

urlpatterns = [
    path('', MemberList.as_view(), name='membermangement-index'),
    path('addMember/', MemberCreate.as_view(), name='membermangement-add-item'),
    path('edit/<int:pk>/', MemberUpdate.as_view(), name='membermangement-edit-item'),
    path('delete/<int:pk>/', MemberDelete.as_view(), name='membermangement-delete-item')
]