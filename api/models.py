from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Truck(models.Model):
    plateNumber = models.CharField(max_length=150, unique=True, db_index=True)
    registrationNumber = models.CharField(
        max_length=150, unique=True, db_index=True)


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Driver(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    mobileNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    mobileNumber = models.CharField(
        validators=[mobileNumberRegex], max_length=16, unique=True, db_index=True)
    email = models.EmailField(max_length=250, unique=True, db_index=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language)
    aasignedTruck = models.OneToOneField(
        Truck,
        on_delete=models.SET_NULL,
        null=True,
        db_index=True,
        blank=True,
    )
    created_at = models.DateField(auto_now_add=True)


@receiver(pre_save, sender=Language)
def capitalize(instance,  **kwargs):
    instance.name = instance.name.capitalize()


@receiver(pre_save, sender=City)
def capitalize(instance,  **kwargs):
    instance.name = instance.name.capitalize()


@receiver(pre_save, sender=District)
def capitalize(instance,  **kwargs):
    instance.name = instance.name.capitalize()
