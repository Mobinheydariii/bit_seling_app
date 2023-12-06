from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


app_name = "account"



urlpatterns = [

    path('users/', views.UserList.as_view(), name="user_list"),
    path('user/panel/<str:user_name>/', views.UserPanel.as_view(), name="user_panel"),
    path('user/<str:user_name>/', views.UserProfile.as_view(), name="user_profile"),

    # Authenticating urls
    path('login/', views.UserLogin.as_view(), name="user_login"),
    path('register/simple/user/', views.SimleUserRegisterView.as_view(), name="simple_user_register"),
    # path('user/check/otp/', views.UserCheckOtp.as_view(), name="user_check_otp"),

]