from django.contrib import admin
from .models.ocupacoes import OcupacaoCBO
from .models.rh import Profissional

admin.site.register(OcupacaoCBO)
admin.site.register(Profissional)
