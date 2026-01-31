import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

# Imports limpios gracias al PYTHONPATH
from config import Config
from services.audio import AudioService
from services.gcp import SpeechService
from services.memos import MemosService

# Configuración de Logs
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != Config.ALLOWED_USER_ID:
        await update.message.reply_text("⛔ No te conozco. No puedes usar este bot.")
        return
        
    await update.message.reply_text(
        "¡Hola Agus! Soy tu Asistente de Notas.\n"
        "Mándame un audio y lo guardaré en tu Memos."
    )

async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # 1. Capa de Seguridad
    if user_id != Config.ALLOWED_USER_ID:
        logging.warning(f"Acceso denegado al usuario {user_id}")
        await update.message.reply_text("⛔ Acceso denegado.")
        return

    await update.message.reply_text("🎧 Procesando nota de voz...")

    # Nombres de archivos temporales únicos (por si hay concurrencia futura)
    temp_id = f"audio_{update.message.message_id}"
    oga_file = f"{temp_id}.oga"
    wav_file = f"{temp_id}.wav"

    try:
        # 2. Obtener archivo de Telegram
        new_file = await update.message.voice.get_file()
        await new_file.download_to_drive(oga_file)

        # 3. Conversión de Audio
        if not AudioService.convert_oga_to_wav(oga_file, wav_file):
            raise Exception("Falló la conversión de audio")

        # 4. Transcripción con IA
        texto = SpeechService.transcribe(wav_file)
        
        if not texto:
            await update.message.reply_text("🤷‍♂️ No pude entender el audio o estaba vacío.")
            return

        # 5. Persistencia en Memos
        if MemosService.save_memo(texto):
            await update.message.reply_text(f"✅ Guardado:\n\n_{texto}_", parse_mode='Markdown')
        else:
            await update.message.reply_text(f"⚠️ Transcrito:\n{texto}\n\n❌ Error al guardar en Memos.")

    except Exception as e:
        logging.error(f"Error en el handler: {e}")
        await update.message.reply_text("🔥 Ocurrió un error interno.")
    
    finally:
        # 6. Limpieza (Siempre se ejecuta)
        AudioService.cleanup([oga_file, wav_file])

if __name__ == '__main__':
    # Validación inicial
    try:
        Config.validate()
        print("✅ Configuración cargada correctamente.")
    except ValueError as e:
        print(f"❌ Error de Configuración: {e}")
        exit(1)

    # Iniciar Bot
    application = ApplicationBuilder().token(Config.TELEGRAM_TOKEN).build()

    start_handler_obj = CommandHandler("start", start_handler)
    application.add_handler(start_handler_obj)

    voice_msg_handler = MessageHandler(filters.VOICE, voice_handler)
    application.add_handler(voice_msg_handler)
    
    print("🤖 Bot iniciado - Esperando audios...")
    application.run_polling()