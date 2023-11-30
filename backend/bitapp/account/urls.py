from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


app_name = "account"



urlpatterns = [
    # Tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', views.MyTokenObtainView.as_view(), name='token_obtain_pair'),

    path('users/', views.UserList.as_view(), name="user_list"),
    path('user/panel/<str:user_name>/', views.UserPanel.as_view(), name="user_panel"),
    path('user/<str:user_name>/', views.UserProfile.as_view(), name="user_profile"),

    # Authenticating urls
    path('user/login/', views.UserLogin.as_view(), name="user_login"),
    path('user/register/', views.UserRegister.as_view(), name="user_register"),
    path('user/check/otp/', views.UserCheckOtp.as_view(), name="user_check_otp")

]