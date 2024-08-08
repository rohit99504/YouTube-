import os

API_ID    = os.environ.get("API_ID", "27498866")
API_HASH  = os.environ.get("API_HASH", "96fbb6ad2e11ab04e83ca09ef3f42455")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7335048933:AAFsXWZVJ4_oUHhaox2llmbWEMUcCsdkLR8") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
