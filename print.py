from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time


def take_screenshot(url, username, password, save_path):
    # Configurando o navegador
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Remova temporariamente para depuração
    options.add_argument('--window-size=1920,1080')  # Definindo o tamanho da janela para 1920x1080
    driver = webdriver.Chrome(options=options)
    try:
        # Abrindo a URL
        driver.get(url)
        # Encontrando os campos de login e senha e enviando as informações
        wait = WebDriverWait(driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.ID, 'floatingInput')))
        password_field = wait.until(EC.presence_of_element_located((By.ID, 'floatingPassword')))
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        
        # Esperando um tempo extra para garantir que a página seja carregada completamente
        time.sleep(7)
        
        # Tirando o print da tela
        driver.save_screenshot(save_path)
        print("Screenshot tirado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
    finally:
        # Fechando o navegador
        driver.quit()
hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# URL que você deseja capturar                   
url = "http://dashboard.bomfuturo.com.br/ChamadosBI/dashboard"
# InformaÃ§Ãµes de login                    
username = "rafael.barbosa"
password = "Josias1409@"
# Caminho onde você deseja salvar o screenshot
save_path = f"MonitBi_{hora}.png"  
# Chamando a função para tirar o screenshot
take_screenshot(url, username, password, save_path)