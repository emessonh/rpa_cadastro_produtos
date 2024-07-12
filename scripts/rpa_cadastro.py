from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from importacao_dados import *

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

timeout = 10
sleep_time = 2
driver.get('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

# Login
email = WebDriverWait(driver, timeout).until(
    EC.element_to_be_clickable((By.ID, 'email'))
)
email.send_keys('email.ficticio@gmail.com')
time.sleep(sleep_time)
senha = driver.find_element(by=By.ID, value='password')
senha.send_keys('12345678')
time.sleep(sleep_time)
driver.find_element(by=By.ID, value='pgtpy-botao').click()

# Dataframe dos dados
df = main()

# Preenche e envia o cadastro
for c in range(len(df)):
    code = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.ID, 'codigo'))
    )
    code.send_keys(str(df['codigo'].iloc[c]))
    
    time.sleep(1)
    marca = driver.find_element(by=By.ID, value='marca').send_keys(str(df['marca'].iloc[c]))

    time.sleep(1)
    tipo = driver.find_element(by=By.ID, value='tipo').send_keys(str(df['tipo'].iloc[c]))

    time.sleep(1)
    categoria = driver.find_element(by=By.ID, value='categoria').send_keys(str(df['categoria'].iloc[c]))

    time.sleep(1)
    preco_unitario = driver.find_element(by=By.ID, value='preco_unitario').send_keys(str(df['preco_unitario'].iloc[c]))

    time.sleep(1)
    custo_produto = driver.find_element(by=By.ID, value='custo').send_keys(str(df['custo'].iloc[c]))

    time.sleep(1)
    obs = driver.find_element(by=By.ID, value='obs').send_keys(str(df['obs'].iloc[c]))

    print({
        'mensagem':f'Item {str(df['codigo'].iloc[c])} cadastrado',
        'marca':str(df['marca'].iloc[c]),
        'tipo':str(df['tipo'].iloc[c]),
        'categoria':str(df['categoria'].iloc[c]),
        'preço unitário':str(df['preco_unitario'].iloc[c]),
        'custo produto':str(df['custo'].iloc[c]),
        'obs':str(df['obs'].iloc[c])
    })

    time.sleep(1)
    btn_enviar = driver.find_element(by=By.ID, value='pgtpy-botao').click()

# Encerra a rpa
time.sleep(sleep_time)
driver.quit()