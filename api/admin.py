from django.contrib import admin

from .models import Truck, City, Driver, District, Language


admin.site.register(Driver)
admin.site.register(Truck)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Language)
