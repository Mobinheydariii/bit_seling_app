from django.urls import path
from . import views



app_name = "account"



urlpatterns = [
    path('users/', views.UserList.as_view(), name="user_list"),
    path('user/panel/<str:user_name>/', views.UserPanel.as_view(), name="user_panel"),
    path('user/<str:user_name>/', views.UserDetail.as_view(), name="user_detail"),
]