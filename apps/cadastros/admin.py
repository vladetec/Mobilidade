from django.contrib import admin
from .models import (
	Onibus,
	Parada,
	Endereco,
    Destino
)

admin.site.register(Onibus)
admin.site.register(Parada)
admin.site.register(Endereco)
admin.site.register(Destino)
