from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    # 'date' es el nombre nuevo del campo de fecha
    # 'creator' es importante verlo para la fase de IDOR
    list_display = ('title', 'severity', 'date', 'creator')