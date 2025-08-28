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
chrome_options.add_argument("--headless") #Ejecutar en segundo plano
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
                date_str = cols[0].text
                close_price = float(cols[4].text.replace(",", ""))
                
                dates.append(datetime.strptime(date_str, "%b %d, %Y"))
                closes.append(close_price)
            except:
                continue
            
    # Crear Dataframe con los datos
    df = pd.DataFrame({"Data": dates, "Close": closes})
    df = df.sort_values("Data") # Ordenar por fecha
    
    # Crear visualizaciones
    plt.style.use("default")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Grafica de linea de precios de cierre
    ax1.plot(df["Data"], df["Close"], color="#2E86AB", linewidth=2)
    ax1.set_title(f'S&P 500 - Precios de cierre (6 meses)\nPrecio actual: {current_price} ({price_change})', fontsize=14, fontweight='bold')
    ax1.set_ylabel("precio(USD)")
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(axis="x", rotation=45)
    
    # Grafica de barras de variacion diario
    daily_change = df["Close"].pct_change() * 100
    colors = ["green" if x >= 0 else "red" for x in daily_change]
    ax2.bar(df["Data"], daily_change, color=colors, alpha=0.7)
    ax2.set_title("Variacion porcentual diaria", fontsize=14, fontweight='bold')
    ax2.set_ylabel('Cambio (%)')
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(axis='x', rotation=45)
    
    # Ajustar layout y mostrar
    plt.tight_layout()
    plt.show()
    
    # Mostrar estadísticas básicas
    print(f"Precio actual del S&P 500: {current_price}")
    print(f"Cambio: {price_change}")
    print(f"Precio más alto (6 meses): ${df['Close'].max():.2f}")
    print(f"Precio más bajo (6 meses): ${df['Close'].min():.2f}")
    print(f"Volatilidad promedio: {daily_change.std():.2f}%")
    
finally:
    # Cerrar el navegador
    driver.quit()
