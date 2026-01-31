from google.cloud import speech

class SpeechService:
    @staticmethod
    def transcribe(wav_path: str) -> str:
        """Envía el audio a Google y devuelve el texto."""
        try:
            client = speech.SpeechClient()

            with open(wav_path, "rb") as audio_file:
                content = audio_file.read()

            audio = speech.RecognitionAudio(content=content)
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code="es-AR", 
                model="default"        # modelo Free Tier
            )

            # Usamos recognize (síncrono) para audios cortos
            response = client.recognize(config=config, audio=audio)

            if not response.results:
                return None

            # Concatenar resultados si hay pausas
            texto_final = " ".join([result.alternatives[0].transcript for result in response.results])
            return texto_final.strip()

        except Exception as e:
            print(f"[SpeechService] Error: {e}")
            return None