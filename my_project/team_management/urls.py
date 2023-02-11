from django.urls import path
from . import views
from .views import MemberCreate, MemberEdit, MemberList


urlpatterns = [
    path('', MemberList.as_view(), name="index"),
    path('createMember', MemberCreate.as_view(), name="createMember"),
    path('editMember/<int:id>/', MemberEdit.as_view(), name="editMember")
]