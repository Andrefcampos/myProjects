from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
sleep(45)

mensagem = 'Testando bot'
contatos = ['PINHEIRO CARNA', 'ACOMPANHAMENTO REDE', 'JHULIANY']


def procurar_contato(contato):
    search_box = driver.find_element(By.XPATH, '//div[@class="_2S1VP copyable-text selectable-text"]')
    search_box.send_keys(contatos)
    sleep(2)
    search_box.send_keys(webdriver.common.keys.Keys.RETURN)


def enviar_mensagem(msg):
    message_box = driver.find_element(By.XPATH, '//div[@class="_2A8P4"][@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(msg)
    message_box.send_keys(webdriver.common.keys.Keys.RETURN)


for contato in contatos:
    procurar_contato(contatos)
    enviar_mensagem(mensagem)
driver.quit()
