import requests

def obtener_precios_dolar():
    # Esta URL nos da los precios de todos los tipos de dólar en Argentina
    url = "https://dolarapi.com/v1/dolares"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        
        print("--- PRECIOS DEL DÓLAR HOY ---")
        for dolar in datos:
            nombre = dolar['nombre']
            compra = dolar['compra']
            venta = dolar['venta']
            print(f"{nombre}: Compra ${compra} | Venta ${venta}")
            
    except Exception as e:
        print(f"Error al obtener datos: {e}")

if __name__ == "__main__":
    obtener_precios_dolar()
