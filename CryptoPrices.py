import PySimpleGUI as sg

from selenium import webdriver # Controlar navegador
from selenium.webdriver.common.keys import Keys # Usar teclado
from selenium.webdriver.common.by import By # Localizar os itens no navegador

# Criando o navegador
navegador = webdriver.Chrome()

# Entrar no google e pesquisar cotação do dolar
navegador.get("https://www.google.com/")

# Pegar a cotação do dolar
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

# Entrar no google e pesquisar cotação do euro
navegador.get("https://www.google.com/")

# Pegar a cotação do euro 
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)                                      

# Entrar no https://www.melhorcambio.com/ouro-hoje
navegador.get("https://www.melhorcambio.com/ouro-hoje")


# Pegar cotação do ouro
cotacao_ouro = navegador.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_ouro)

# Entrar no binance e pesquisar cotação do btc
navegador.get("https://binance.com/pt-BR/markets")

# Pegar a cotação do BTC 
cotacao_btc = navegador.find_element(By.XPATH,'//*[@id="tabContainer"]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div').text
print(cotacao_btc)

# Pegar cotação do ETH
cotacao_eth = navegador.find_element(By.XPATH,'//*[@id="tabContainer"]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div').text
print(cotacao_eth)

navegador.quit()

#--GUI--
class PythonScreen:
    def __init__(self):
        #layout
        layout= [ 
            [sg.Text("BTC "+cotacao_btc+"                                          ")],
            [sg.Text("Ether "+cotacao_eth)],
            [sg.Text("Dolar "+cotacao_dolar)],
            [sg.Text("Euro "+cotacao_euro)],
            [sg.Text("Ouro "+cotacao_ouro)]
        ]
        #Janela
        window=sg.Window("Prices").layout(layout)

        self.button, self.values = window.Read()



screen=PythonScreen()

