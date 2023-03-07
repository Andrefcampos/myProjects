from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
sleep(30)

contatos = ['Armandinho']
mensagem = 'kjkkkkkkk boto fé'

def buscar_contatos(contato):
    caixa_busca = driver.find_element(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    sleep(3)
    caixa_busca.click()
    caixa_busca.send_keys(contato)
    sleep(5)
    caixa_busca.send_keys(Keys.ENTER)
    sleep(5)


def enviar_mensagem(msg):
    caixa_mensagem = driver.find_elements(By.XPATH, '//div[contains(@class,"selectable-text copyable-text")]')
    caixa_mensagem[-1].click()
    sleep(3)
    caixa_mensagem[-1].send_keys(mensagem)
    sleep(5)
    caixa_mensagem[-1].send_keys(Keys.ENTER)
    sleep(2)


for contato in contatos:
    buscar_contatos(contato)
    enviar_mensagem(mensagem)
