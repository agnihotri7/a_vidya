from django.contrib import admin

# Register your models here.
from myapp.models import Skill, Profiles, Designation, City

admin.site.register(Skill)
admin.site.register(Profiles)
admin.site.register(Designation)
admin.site.register(City)
