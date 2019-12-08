from django.contrib import admin
from .models import Pies, Adopcja, Adopter, Box

admin.site.register(Pies)
admin.site.register(Box)
admin.site.register(Adopcja)
admin.site.register(Adopter)
# Register your models here.
