from django.contrib.staticfiles.testing import StaticLiveServerTestCase # [cite: 38]
from selenium.webdriver.firefox.webdriver import WebDriver # [cite: 39]
from selenium.webdriver.firefox.options import Options # [cite: 39]
from selenium.webdriver.common.by import By # [cite: 39]
from selenium.webdriver.common.keys import Keys

class SecurityRegressionTests(StaticLiveServerTestCase): # [cite: 40]
    fixtures = ['testdb.json'] # [cite: 41]

    @classmethod # [cite: 42]
    def setUpClass(cls): # [cite: 55]
        super().setUpClass() # [cite: 56]
        opts = Options() # [cite: 57]
        opts.add_argument("--headless") # mode Headless [cite: 58]
        cls.selenium = WebDriver(options=opts) # [cite: 59]
        
        # Implicit Wait perquè Selenium no intenti clicar abans que carregui [cite: 60, 93]
        cls.selenium.implicitly_wait(10) 

    @classmethod # [cite: 61]
    def tearDownClass(cls): # [cite: 62]
        cls.selenium.quit() # [cite: 63]
        super().tearDownClass() # [cite: 64]

    def test_role_restriction(self): # [cite: 65]
        """AUDITORIA: L'analista no ha d'entrar a /admin/""" # [cite: 66]
        
        # 1. Anar a la pàgina de login [cite: 67]
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/')) 
        
        # 2. Implementar el login amb l'usuari (adaptat al teu JSON) [cite: 68]
        username_input = self.selenium.find_element(By.NAME, "username") # [cite: 68]
        username_input.send_keys("hacker_local") 
        
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("1234") # Contrasenya del teu JSON
        password_input.send_keys(Keys.RETURN) # Prem la tecla Enter per enviar el formulari
        
        # 3. Intentar forçar URL d'admin [cite: 71]
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/')) # [cite: 72]
        
        # 4. ASSERT de Seguretat [cite: 73]
        # Comprova que el títol de la pàgina no és el de l'administració de Django
        self.assertNotEqual(self.selenium.title, "Site administration", "Error de seguretat: L'usuari ha accedit a l'admin.") # [cite: 73]