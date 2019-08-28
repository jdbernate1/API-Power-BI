import adal
from pypowerbi.client import PowerBIClient


authority_url = 'https://login.windows.net/common'
resource_url = 'https://analysis.windows.net/powerbi/api'
api_url = 'https://api.powerbi.com'

# Credenciales propias
client_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
username = 'xxxxxx@xxxxx'
password = 'xxxxxxxx'

# Autenticarse usando adal
context = adal.AuthenticationContext(authority=authority_url,
                                     validate_authority=True,
                                     api_version=None)

# Obtener token autorización
token = context.acquire_token_with_username_password(resource=resource_url,
                                                     client_id=client_id,
                                                     username=username,
                                                     password=password)

# crear cliente power bi
client = PowerBIClient(api_url, token)

# Refrescar dataset (dataset y group IDs se puede tomar del navegador)
client.datasets.refresh_dataset(dataset_id='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
                                notify_option='MailOnCompletion',
                                group_id='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')


