import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8133374257:AAEfnYnnZPg5DGoDiN1hHZbNTQ04tmG8of0")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27998466"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3b16e1407c1b00c9a76d01f954ee9cd4")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://shortstime1001:vLIvWG5grm8eD7lj@saverestric.eotq9b4.mongodb.net/?retryWrites=true&w=majority&appName=Saverestric") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
