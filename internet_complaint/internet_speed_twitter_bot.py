from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from environs import Env
import time

# Inicializar o carregamento de variáveis de ambiente
env = Env()
env.read_env()

# Velocidades prometidas
PROMISED_DOWN = 450
PROMISED_UP = 250

# Credenciais do Twitter
TWITTER_EMAIL = env.str("TWITTER_EMAIL")
TWITTER_PASSWORD = env.str("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        """Inicializa o WebDriver e as variáveis de velocidade"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """Realiza o teste de velocidade no Speedtest.net"""
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        # Aceitar os cookies, se necessário
        try:
            accept_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            accept_button.click()
        except Exception:
            pass  # Se não aparecer, continua normalmente

        # Clicar no botão de iniciar o teste
        start_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "start-button"))
        )
        start_button.click()

        # Esperar o teste terminar
        time.sleep(45)

        # Capturar as velocidades de download e upload
        self.down = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "download-speed"))
        ).text

        self.up = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "upload-speed"))
        ).text

        print(f"Download: {self.down} Mbps")
        print(f"Upload: {self.up} Mbps")
        self.up = float(self.up)
        self.down = float(self.down)
        if self.up < PROMISED_UP or self.down < PROMISED_DOWN:
            return True
        else:
            return False

    def tweet_at_provider(self):
        """Posta um tweet reclamando da velocidade de internet se estiver abaixo do esperado"""
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)

        # Inserir email
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(3)

        # Inserir senha
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        # Escrever e postar o tweet
        tweet_text = f"Oi, @Meu_Provedor! Estou pagando por {PROMISED_DOWN}Mbps de download e {PROMISED_UP}Mbps de upload, mas estou recebendo {self.down}Mbps e {self.up}Mbps! O que está acontecendo? #InternetLenta"
        tweet_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.public-DraftStyleDefault-block'))
        )
        tweet_box.send_keys(tweet_text)

        tweet_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Tweetar']"))
        )
        tweet_button.click()

        print("Tweet enviado com sucesso!")

        # Fechar o navegador
        self.driver.quit()


# Executar o bot
bot = InternetSpeedTwitterBot()
if bot.get_internet_speed():
    bot.tweet_at_provider()
