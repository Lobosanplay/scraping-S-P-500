import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Cofigurar opciones de Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless") #Ejecutar en segundo plano
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Inicializar el driver en Chrome
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navegar a la página de Yahoo Finance del S&P 500
    url = "https://finance.yahoo.com/quote/%5EGSPC"
    driver.get(url)
    
    # Esperar a que la pagina cargue
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='qsp-price']"))
    )
    
    # Obtener el precio actual
    price_element = driver.find_element(By.CSS_SELECTOR, "[data-testid='qsp-price']")
    current_price = price_element.text
    
    # Obtener el cambio en precio y porcentage
    change_element = driver.find_element(By.CSS_SELECTOR, "[data-testid='qsp-price-change']")
    price_change = change_element.text
    
    # Navegar a la pestaña de datos historicos
    driver.find_element(By.XPATH, "//span[contains(text(), 'Historical Data')]").click()

    # Esperar a que carguen los datos historicos
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='history-table']"))
    )
    
    # Botom de las opciones de cambio de tiempo
    time_period_options = driver.find_element(By.CSS_SELECTOR, "button[title='Aug 28, 2024 - Aug 28, 2025']")
    time_period_options.click()
    time.sleep(2)
    
    # Cambiar el rango de tiempo de 6 meses
    time_period_buttom = driver.find_element(By.CSS_SELECTOR, "button[value='6_M']")
    time_period_buttom.click()
    time.sleep(2) # Esperar a que carguen los datos
    
    # Extraer datos de la tabla
    tabla = driver.find_element(By.CSS_SELECTOR, "table[class='table yf-1jecxey noDl hideOnPrint']")
    rows = tabla.find_elements(By.TAG_NAME, "tr")
    
    # Procesar los datos
    dates = []
    closes = []
    opens = []
    highs = []
    lows = []
    
    for row in rows[1:]:  # Saltar encabezado
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 5:
            try:
                date_str = [0].text
                close_price = float(cols[4].text.replace(",", ""))
                
                dates.append(datetime.strptime(date_str, "%b %d, %Y"))
                closes.append(close_price)
            except:
                continue
    
finally:
    # Cerrar el navegador
    driver.quit()
