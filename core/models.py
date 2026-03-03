from django.db import models
from django.contrib.auth.models import User  # Importamos el modelo de Usuario

class Incident(models.Model):  # IMPORTANTE: Renombrado a 'Incident' para coincidir con la tabla 'core_incident'
    
    # Opciones para la severidad (conservamos tu código)
    class Severity(models.TextChoices):
        HIGH = 'H', 'Alta'
        MEDIUM = 'M', 'Mitjana'
        LOW = 'L', 'Baixa'

    title = models.CharField(max_length=200)
    description = models.TextField()
    
    severity = models.CharField(
        max_length=1,
        choices=Severity.choices,
        default=Severity.MEDIUM
    )
    
    # Usamos auto_now_add=True para que la fecha se ponga sola al crear
    date = models.DateTimeField(auto_now_add=True) 

    # IMPORTANTE: Campo necesario para la Fase 4 (IDOR) de la guía
    # Relaciona el incidente con el usuario que lo creó
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title