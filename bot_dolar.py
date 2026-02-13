import requests

def extraer_datos_directos():
    # Esta es la URL de la API interna de Dolarito que tiene los bancos
    url = "https://api.dolarito.ar/api/v1/quotations/banks"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Referer': 'https://www.dolarito.ar/'
    }
    
    try:
        print("Consultando base de datos de Dolarito...")
        response = requests.get(url, headers=headers)
        
        # Si la respuesta es 200, es que entramos con éxito
        if response.status_code == 200:
            datos = response.json()
            
            print(f"{'BANCO':<25} | {'COMPRA':<10} | {'VENTA':<10}")
            print("-" * 50)
            
            for entidad in datos:
                nombre = entidad.get('name', 'N/A')
                # Buscamos los valores de compra y venta dentro del JSON
                compra = entidad.get('buy', 0)
                venta = entidad.get('sell', 0)
                
                print(f"{nombre:<25} | ${compra:<10} | ${venta:<10}")
        else:
            print(f"Error: No se pudo acceder (Código {response.status_code})")

    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    extraer_datos_directos()
