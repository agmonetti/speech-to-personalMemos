import os
from dotenv import load_dotenv

# Cargar .env solo si estamos en desarrollo local
load_dotenv()

class Config:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    # Convertimos a int de forma segura, default 0 si falla
    try:
        ALLOWED_USER_ID = int(os.getenv("ALLOWED_USER_ID", "0"))
    except ValueError:
        ALLOWED_USER_ID = 0
        
    MEMOS_URL = os.getenv("MEMOS_URL")
    MEMOS_TOKEN = os.getenv("MEMOS_TOKEN")
    GOOGLE_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    @staticmethod
    def validate():
        """Verifica que todas las variables críticas existan."""
        missing = []
        if not Config.TELEGRAM_TOKEN: missing.append("TELEGRAM_TOKEN")
        if Config.ALLOWED_USER_ID == 0: missing.append("ALLOWED_USER_ID")
        if not Config.MEMOS_URL: missing.append("MEMOS_URL")
        if not Config.MEMOS_TOKEN: missing.append("MEMOS_TOKEN")
        
        if missing:
            raise ValueError(f"Faltan variables de entorno: {', '.join(missing)}")