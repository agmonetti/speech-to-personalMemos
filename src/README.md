# 🎙️ Voice to Memos Bot

Bot de Telegram diseñado con arquitectura de microservicio. Recibe notas de voz, las convierte (FFmpeg), las transcribe (Google Cloud STT) y las guarda automáticamente en una instancia de Memos.
Siempre buscando no salirse de la capa gratuita que ofrece GCP

## Stack
* **Lenguaje:** Python 3.9
* **Infra:** Docker
* **Servicios:**
    * `AudioService`: Conversión OGA -> WAV (16kHz Mono).
    * `SpeechService`: Google Cloud Speech-to-Text (Modelo V1 Default).
    * `MemosService`: Memos API.

## (.env)

| Variable | Descripción |
| :--- | :--- |
| `TELEGRAM_TOKEN` | Token del bot (@BotFather) |
| `ALLOWED_USER_ID` | Tu ID de Telegram (@userinfobot) para seguridad |
| `MEMOS_URL` | URL de Memos (Ej: `http://memos:5230` en Docker o IP pública en local) |
| `MEMOS_TOKEN` | Token de acceso de Memos (Settings > Access Tokens) |
| `GOOGLE_APPLICATION_CREDENTIALS` | Ruta interna al JSON (`/app/credentials.json`) |
