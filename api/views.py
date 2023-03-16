from rest_framework import generics

from .models import Driver, Truck, Language, City, District
from .serializers import DriverSerializer, TruckSerializer, DriverListSerializer, LanguageSerializer, CitySerializer, DistrictSerializer


class DriverList(generics.ListAPIView):
    serializer_class = DriverListSerializer

    def get_queryset(self):
        queryset = Driver.objects.all()
        mobileNumber = self.request.query_params.get('mobileNumber')
        plateNumber = self.request.query_params.get('plateNumber')
        email = self.request.query_params.get('email')
        if mobileNumber is not None:
            queryset = queryset.filter(mobileNumber=f"{mobileNumber}")
        if email is not None:
            queryset = queryset.filter(email__iexact=email)
        if plateNumber is not None:
            queryset = queryset.filter(aasignedTruck__plateNumber=plateNumber)
        return queryset


class CreateDriver(generics.CreateAPIView):
    serializer_class = DriverSerializer

    def get_queryset(self):
        queryset = Driver.objects.all()
        return queryset


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer

    def get_queryset(self):
        queryset = Driver.objects.all()
        return queryset


class TruckList(generics.ListCreateAPIView):
    serializer_class = TruckSerializer

    def get_queryset(self):
        queryset = Truck.objects.all()
        return queryset


class LanguageList(generics.ListCreateAPIView):
    serializer_class = LanguageSerializer

    def get_queryset(self):
        queryset = Language.objects.all()
        return queryset


class CityList(generics.ListCreateAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = City.objects.all()
        return queryset


class DistrictList(generics.ListCreateAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        queryset = District.objects.all()
        return queryset
