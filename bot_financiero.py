import requests
from datetime import datetime

# URL que te va a dar Make.com más adelante
MAKE_WEBHOOK_URL = "TU_URL_DE_MAKE_AQUI"

def obtener_y_enviar():
    datos = {
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "blue": 0,
        "mep": 0,
        "oficial": 0,
        "riesgo": 0
    }
    
    # Obtener Dólares
    res_dolar = requests.get("https://dolarapi.com/v1/cotizaciones").json()
    for d in res_dolar:
        if d['casa'] == 'blue': datos['blue'] = d['venta']
        if d['casa'] == 'mep': datos['mep'] = d['venta']
        if d['casa'] == 'oficial': datos['oficial'] = d['venta']

    # Obtener Riesgo País
    res_riesgo = requests.get("https://api.argentinadatos.com/v1/finanzas/indices/riesgo-pais/ultimo").json()
    datos['riesgo'] = res_riesgo['valor']

    # ENVIAR A MAKE
    requests.post(MAKE_WEBHOOK_URL, json=datos)
    print("Datos enviados a Make con éxito")

if __name__ == "__main__":
    obtener_y_enviar()
