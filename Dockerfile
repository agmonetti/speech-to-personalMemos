FROM python:3.9-slim

# 1. Instalamos FFmpeg y limpiamos caché de apt
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. Copiamos dependencias e instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copiamos todo
COPY . .

# 4.Agregamos /app/src al path de Python
# Esto permite hacer "import config" desde cualquier subcarpeta
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# 5. Ejecutamos el módulo principal
CMD ["python", "src/main.py"]