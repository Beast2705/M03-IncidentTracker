from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.db import connection

class SecurityAuditTest(TestCase):
    def setUp(self):
        # 1. Preparación: Creamos un usuario normal (NO es admin)
        self.user = User.objects.create_user(username='auditor', password='password123', email='normal@test.com')
        self.client = Client()
        self.client.login(username='auditor', password='password123')

    def test_sqli_privilege_escalation(self):
        """
        Test de regresión para CVE-Simulado: Escalada de privilegios vía SQLi en update de email.
        """
        # 2. Verificar estado inicial (No debe ser admin)
        self.assertFalse(self.user.is_superuser, "El usuario no debería ser superusuario inicialmente")

        # 3. Ejecutar el ataque (Payload Malicioso)
        payload = "hacker@test.com', is_superuser='t' --"
        
        self.client.post('/update-email/', {'email': payload})

        # 4. Verificar el estado después del ataque
        self.user.refresh_from_db()

        # ASSERT DE SEGURIDAD:
        self.assertFalse(self.user.is_superuser, "FALLO DE SEGURIDAD: ¡Inyección SQL exitosa! El usuario ha escalado a Admin.")