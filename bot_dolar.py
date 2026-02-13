import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def extraer_datos_dolarito():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Este es el truco: le decimos que somos un Chrome normal de Windows
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        print("Entrando a Dolarito...")
        driver.get("https://www.dolarito.ar/cotizacion/bancos")
        
        # Esperamos 10 segundos fijos para que cargue todo
        print("Esperando que carguen los precios...")
        time.sleep(10)
        
        # En lugar de buscar tablas complejas, buscamos todos los textos
        # Esto nos ayudará a ver qué está leyendo el robot realmente
        elementos = driver.find_elements(By.XPATH, "//div[contains(@class, 'css-')]")
        
        print(f"--- DATOS CAPTURADOS ---")
        for el in elementos[:20]: # Imprimimos los primeros 20 resultados para probar
            texto = el.text.strip()
            if texto:
                print(f"Dato: {texto}")
                
        if not elementos:
            print("No se encontró nada. El sitio podría estar bloqueando el acceso.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    extraer_datos_dolarito()
