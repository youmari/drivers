from django.urls import path
from .views import DriverList, DriverDetail, CreateDriver, LanguageList, CityList, TruckList, DistrictList

urlpatterns = [
    path('driver/', CreateDriver.as_view(), name='driver'),
    path('drivers/', DriverList.as_view(), name='drivers'),
    path('driver/<int:pk>/', DriverDetail.as_view(), name='driver_id'),
    path('language/', LanguageList.as_view(), name='language'),
    path('city/', CityList.as_view(), name='city'),
    path('truck/', TruckList.as_view(), name='truck'),
    path('district/', DistrictList.as_view(), name='district'),
]
