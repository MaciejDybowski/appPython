from django.contrib import admin

# Register your models here.
from .models import Person,Duty,Ceremony,PersonOnCeremony,PersonOnDuty

admin.site.register(Person)
admin.site.register(Duty)
admin.site.register(Ceremony)
admin.site.register(PersonOnDuty)
admin.site.register(PersonOnCeremony)