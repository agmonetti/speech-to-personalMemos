import requests
from config import Config

class MemosService:
    @staticmethod
    def save_memo(text: str) -> bool:
        # 1. Aseguramos la "s" final
        url = f"{Config.MEMOS_URL}/api/v1/memos"
        
        headers = {
            "Authorization": f"Bearer {Config.MEMOS_TOKEN}",
            "Content-Type": "application/json"
        }
        
        data = {
            "content": f"#to-do {text}",
            "visibility": "PRIVATE"
        }
        
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Error en el servicio de Memos: {e}")
            return False