from django.urls import path

from wonder.views import UserCreateView, UserUpdateView, UserListView

urlpatterns = [
    path("", UserListView.as_view(), name="users"),
    path("create", UserCreateView.as_view(), name="user_create"),
    path("<int:pk>", UserUpdateView.as_view(), name="user_retrieve_update_delete")
]
