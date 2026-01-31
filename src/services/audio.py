import os
from pydub import AudioSegment

class AudioService:
    @staticmethod
    def convert_oga_to_wav(input_path: str, output_path: str) -> bool:
        """Convierte OGA (Opus) a WAV 16kHz Mono (Requisito de Google)."""
        try:
            audio = AudioSegment.from_file(input_path)
            # Normalización para Google STT
            audio = audio.set_channels(1).set_frame_rate(16000)
            audio.export(output_path, format="wav")
            return True
        except Exception as e:
            print(f"[AudioService] Error: {e}")
            return False
            
    @staticmethod
    def cleanup(files: list):
        """Borra archivos temporales para no llenar el disco."""
        for f in files:
            if os.path.exists(f):
                try:
                    os.remove(f)
                except OSError:
                    pass