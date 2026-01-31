# Speech to Memos

> Convierte notas de voz de Telegram en texto y las guarda automáticamente en una instancia self-hosted de Memos.

![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat&logo=python)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=flat&logo=docker)
![GCP](https://img.shields.io/badge/Google_Cloud-Speech_to_Text-red?style=flat&logo=google-cloud)
![Memos](https://img.shields.io/badge/Memos-Integration-green?style=flat)

### Este bot está diseñado con una **Arquitectura de Microservicios** modular. Recibe audios, los procesa para cumplir con los estándares de Google (16kHz, 16-bit Mono), los transcribe usando IA y los sincroniza con tu cuenta personal de Memos.
<p align="center">
  <img src="public/road.png" width="700" />
</p>

---

## Características

* **Transcripción IA:** Utiliza Google Cloud Speech-to-Text para una precisión de nivel empresarial.
* **Procesamiento de Audio:** Conversión automática de OGA (Telegram) a WAV Lineal PCM optimizado.
* **Privacidad:** Las notas se guardan con visibilidad `PRIVATE` por defecto..
* **Seguridad:** Restringido por `ALLOWED_USER_ID`. Solo la persona definida en el .env puede.

---

## Estructura

```text
voice_bot/
├── src/
│   ├── main.py        # Entrypoint (Manejo de Telegram)
│   ├── config.py      # Gestión de configuración y validación 
│   └── services/      # Lógica de Negocio
│       ├── audio.py   # FFmpeg wrapper (Conversión y normalización de audios)
│       ├── gcp.py     # Cliente Google Cloud STT
│       └── memos.py   # Cliente API Memos
├── Dockerfile         # Imagen base Python + FFmpeg
├── requirements.txt   # Dependencias congeladas
└── .env.template      # Plantilla de variables de entorno
