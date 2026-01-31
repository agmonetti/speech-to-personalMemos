import requests
from config import Config

class MemosService:
    @staticmethod
    def save_memo(text: str) -> bool:
        """Crea un nuevo memo privado."""
        url = f"{Config.MEMOS_URL}/api/v1/memo"
        
        headers = {
            "Authorization": f"Bearer {Config.MEMOS_TOKEN}",
            "Content-Type": "application/json"
        }
        
        data = {
            "content": f"#audio {text}",
            "visibility": "PRIVATE"
        }
        
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"[MemosService] Error: {e}")
            return False