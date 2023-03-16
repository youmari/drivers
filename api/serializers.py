from rest_framework import serializers
from .models import Driver, Truck, Language, District, City


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('__all__')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('__all__')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('__all__')


class DriverListSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=True)
    aasignedTruck = TruckSerializer()
    city = CitySerializer()
    district = DistrictSerializer()

    class Meta:
        model = Driver
        fields = ('__all__')


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ('__all__')
