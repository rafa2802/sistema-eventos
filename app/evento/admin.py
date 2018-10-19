from django.contrib import admin
from app.evento.models import *

class EventoAdmin(admin.ModelAdmin):
    filter_horizontal = ['palestras', 'minicursos',]

class AtividadeAdmin(admin.ModelAdmin):
    filter_horizontal = ['inscritos']

admin.site.register(Evento, EventoAdmin)
admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(Palestrante)
