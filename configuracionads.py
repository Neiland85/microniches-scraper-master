from google.ads.google_ads.client import GoogleAdsClient

# Define la función para configurar el cliente de Google Ads
def configurar_cliente_google_ads():
    # Reemplaza 'path/to/your/credentials.json' con la ruta al archivo JSON de tus credenciales
    credentials_path = '/path/to/your/credentials.json'
    # Carga el cliente de Google Ads desde el archivo de credenciales
    client = GoogleAdsClient.load_from_storage(credentials_path)
    return client

# Ejemplo de uso
if __name__ == "__main__":
    # Configura el cliente de Google Ads
    client = configurar_cliente_google_ads()

    # Tu código para buscar palabras clave relacionadas con bajo KD aquí...

