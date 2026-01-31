import os
from pydub import AudioSegment

class AudioService:
    @staticmethod
    def convert_oga_to_wav(input_path: str, output_path: str) -> bool:
        """Convierte OGA (Opus) a WAV 16kHz Mono 16-bit (Requisito estricto de Google)."""
        try:
            audio = AudioSegment.from_file(input_path)
            
            # --- TRANSFORMACIÓN DE AUDIO ---
            # 1. set_channels(1): Mono
            # 2. set_frame_rate(16000): 16kHz
            # 3. set_sample_width(2): 2 bytes = 16 bits 
            audio = audio.set_channels(1).set_frame_rate(16000).set_sample_width(2)
            
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