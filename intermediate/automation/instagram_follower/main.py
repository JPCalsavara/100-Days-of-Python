from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from environs import Env

# Carregar variáveis de ambiente
env = Env()
env.read_env()

# Credenciais e dados do Instagram
SIMILAR_ACCOUNT = "loud_caiox"
INSTA_ENDPOINT = "https://www.instagram.com/"
INSTA_EMAIL = env.str("MY_EMAIL")
INSTA_PASSWORD = env.str("MY_EMAIL_PASSWORD")


class InstaFollower:
    def __init__(self):
        """Inicializa o WebDriver com configurações."""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def wait_for_element(self, by, value, timeout=10):
        """Espera um elemento ficar visível e interagível."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def login(self):
        """Realiza login no Instagram."""
        self.driver.get(INSTA_ENDPOINT)

        # Preencher email e senha
        self.wait_for_element(By.NAME, "username").send_keys(INSTA_EMAIL)
        self.wait_for_element(By.NAME, "password").send_keys(INSTA_PASSWORD, Keys.ENTER)

        # Fechar pop-up "Agora não" caso apareça
        try:
            not_now = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Agora não')]"))
            )
            not_now.click()
        except TimeoutException:
            pass  # Seguir normalmente se o pop-up não aparecer

    def go_to_account(self):
        """Navega até o perfil desejado."""
        search_input = self.wait_for_element(By.XPATH, "//input[@aria-label='Pesquisar']")
        search_input.send_keys(SIMILAR_ACCOUNT)

        # Clicar no primeiro resultado da pesquisa
        account = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '/{SIMILAR_ACCOUNT}/')]"))
        )
        account.click()

    def open_followers_list(self):
        """Abre a lista de seguidores do perfil alvo."""
        try:
            followers_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]"))
            )
            followers_button.click()
        except TimeoutException:
            print("Erro: Não foi possível encontrar o botão de seguidores.")

    def find_followers(self):
        """Rola a lista de seguidores para carregar mais perfis."""
        try:
            modal = self.wait_for_element(By.XPATH, "//div[@role='dialog']//ul")

            for _ in range(5):  # Rola a lista 5 vezes
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//ul//li"))
                )
        except TimeoutException:
            print("Erro ao carregar a lista de seguidores.")

    def follow(self):
        """Segue usuários da lista de seguidores."""
        buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Seguir')]")

        for button in buttons:
            try:
                button.click()
                WebDriverWait(self.driver, 2).until(
                    EC.text_to_be_present_in_element((By.XPATH, "//button"), "Seguindo")
                )
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancelar')]")
                cancel_button.click()

    def start(self):
        """Executa todas as funções na ordem correta."""
        self.login()
        self.go_to_account()
        self.open_followers_list()
        self.find_followers()
        self.follow()


# Instanciar e rodar o bot
insta_follower = InstaFollower()
insta_follower.start()
