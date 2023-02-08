from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('showMember', views.showMember, name="showMember"),
    path('createMember', views.createMember, name="createMember"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('editMember/<int:id>/', views.editMember, name="editMember")
]