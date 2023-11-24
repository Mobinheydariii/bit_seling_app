from django.urls import path
from . import views



app_name = "account"



urlpatterns = [
    path('producer/official/api/list', views.OfficialProducerAPIList.as_view(), name="producer_official_api_list"),
]