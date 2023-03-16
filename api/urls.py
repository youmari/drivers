from django.urls import path
from .views import DriverList, DriverDetail, CreateDriver, LanguageList, CityList, TruckList, DistrictList

urlpatterns = [
    path('driver/', CreateDriver.as_view()),
    path('drivers/', DriverList.as_view()),
    path('driver/<int:pk>/', DriverDetail.as_view()),
    path('language/', LanguageList.as_view()),
    path('city/', CityList.as_view()),
    path('truck/', TruckList.as_view()),
    path('district/', DistrictList.as_view()),
]
