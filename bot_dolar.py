import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extraer_datos_dolarito():
    # Configuración para que el navegador corra en el servidor de GitHub (sin ventana)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        print("Abriendo Dolarito...")
        driver.get("https://www.dolarito.ar/cotizacion/bancos")
        
        # Esperamos hasta 10 segundos a que aparezca un elemento con precio
        # Ajustamos el selector según la estructura de la web
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        
        # Capturamos las filas de la tabla de cotizaciones
        filas = driver.find_all("tr") # Buscamos las filas de la tabla
        
        print(f"--- COTIZACIONES ENCONTRADAS ---")
        for fila in filas[1:]: # Saltamos el encabezado
            columnas = fila.find_elements(By.TAG_NAME, "td")
            if len(columnas) >= 3:
                banco = columnas[0].text
                compra = columnas[1].text
                venta = columnas[2].text
                print(f"{banco}: Compra {compra} | Venta {venta}")
                
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    extraer_datos_dolarito()
