from django.contrib import admin
from .models import Especie, Mascota

class mascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'sexo', 'edad', 'descripcion')
    list_filter = ('especie','sexo')
    search_fields = ('nombre','id')

admin.site.register(Especie)
admin.site.register(Mascota, mascotaAdmin)
