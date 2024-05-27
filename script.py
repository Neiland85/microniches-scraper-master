from google.auth import credentials
from google.analytics.data_v1alpha.services.analytics_data import AnalyticsDataClient
from google.oauth2 import service_account

# Define el ID de tu cuenta de servicio y la ruta al archivo JSON de credenciales
service_account_id = "109468929946556511247"
credentials_file = "/ruta/a/tu/credentials.json"

# Carga las credenciales desde el archivo JSON
credentials = service_account.Credentials.from_service_account_file(credentials_file)

# Crea un cliente de Google Analytics Data
client = AnalyticsDataClient(credentials=credentials)

