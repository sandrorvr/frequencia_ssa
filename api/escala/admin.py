from django.contrib import admin
from .models import Escala

@admin.register(Escala)
class EscalaAdimin(admin.ModelAdmin):
    list_display = (
        'group',
        'equipment',
        'date',
        'road',
        'begin',
        'end',
        'foothold',
        'worker',
        'zone'
        )
