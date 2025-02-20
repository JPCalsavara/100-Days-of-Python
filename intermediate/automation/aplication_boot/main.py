from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from environs import Env
import time

# Inicializar dotenv
env = Env()
env.read_env()

# Credenciais
EMAIL = "joaocalsavara456@yahoo.com"
PASSWORD = env.str("MY_EMAIL_PASSWORD")

# Configuração do WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Acessar o LinkedIn Jobs
driver.get("https://www.linkedin.com/jobs/search/"
           "?currentJobId=3982452213&"
           "keywords=estagio%20desenvolvedor"
           "&location=Campinas%20e%20Região"
           "&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&"
           "refresh=true")

time.sleep(2)  # Espera inicial para carregamento da página

def sign_in():
    """Realiza o login no LinkedIn"""
    try:
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button'))
        )
        sign_in_button.click()

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="base-sign-in-modal_session_key"]'))
        )
        email_input.send_keys(EMAIL)

        password_input = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
        password_input.send_keys(PASSWORD)

        sign_button = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
        sign_button.click()
        print("Login realizado com sucesso!")

    except Exception as e:
        print(f"Erro ao fazer login: {e}")

def save_application():
    """Salva a vaga clicando no botão de salvar"""
    try:
        save_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "jobs-save-button"))
        )
        save_button.click()
        print("Vaga salva com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar a vaga: {e}")

def jobs_application():
    """Percorre todas as vagas listadas e salva cada uma delas"""
    try:
        # Esperar até que a lista de vagas esteja carregada
        time.sleep(3)
        job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")

        for index, listing in enumerate(job_listings):
            try:
                print(f"Abrindo vaga {index + 1} de {len(job_listings)}")
                listing.click()  # Clicar na vaga
                time.sleep(2)  # Espera para carregamento da página da vaga
                save_application()  # Salvar a vaga
            except Exception as e:
                print(f"Erro ao processar vaga {index + 1}: {e}")

    except Exception as e:
        print(f"Erro ao obter a lista de vagas: {e}")

# Executar funções
sign_in()
time.sleep(3)  # Aguardar login ser processado
jobs_application()

# Manter o navegador aberto por alguns segundos antes de fechar
time.sleep(5)
driver.quit()
