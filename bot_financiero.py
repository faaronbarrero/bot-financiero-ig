import requests
from datetime import datetime

def obtener_datos():
    print(f"Ejecución iniciada: {datetime.now()}")
    
    # 1. Obtener Dólares (DolarApi - Ámbito)
    try:
        url_dolar = "https://dolarapi.com/v1/cotizaciones"
        res_dolar = requests.get(url_dolar)
        if res_dolar.status_code == 200:
            dolares = res_dolar.json()
            print("--- COTIZACIONES DÓLAR ---")
            for d in dolares:
                # Filtramos los que más te interesan para Instagram
                if d['casa'] in ['oficial', 'blue', 'mep', 'cripto']:
                    print(f"{d['nombre']}: Compra ${d['compra']} | Venta ${d['venta']}")
    except Exception as e:
        print(f"Error Dólar: {e}")

    # 2. Obtener Riesgo País (Argentina Datos)
    try:
        url_riesgo = "https://api.argentinadatos.com/v1/finanzas/indices/riesgo-pais/ultimo"
        res_riesgo = requests.get(url_riesgo)
        if res_riesgo.status_code == 200:
            riesgo = res_riesgo.json()
            print("\n--- RIESGO PAÍS ---")
            print(f"Valor: {riesgo['valor']} puntos")
            print(f"Fecha: {riesgo['fecha']}")
    except Exception as e:
        print(f"Error Riesgo País: {e}")

if __name__ == "__main__":
    obtener_datos()
