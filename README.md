# YT-DASH

**Interfaz Gráfica de Escritorio para YT-DLP**

Una aplicación de escritorio desarrollada en Python que proporciona una interfaz gráfica amigable para descargar videos de YouTube en formato MP3 (audio) o MP4 (video) utilizando yt-dlp.

![YT-DASH](https://img.shields.io/badge/Python-3.8+-blue.svg)
![YT-DASH](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Características

- ✅ **Interfaz gráfica intuitiva** - Fácil de usar con tkinter
- 🎵 **Descarga MP3** - Extrae audio de videos de YouTube
- 🎬 **Descarga MP4** - Descarga videos en formato MP4
- 🎚️ **Selección de calidad** - Elige entre mejor calidad, 720p o 480p
- 📁 **Directorio personalizable** - Selecciona dónde guardar tus descargas
- 📊 **Barra de progreso** - Visualiza el progreso de la descarga
- 📝 **Registro de actividad** - Mantiene un log de todas las operaciones

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/YoeKimera/yt-dash.git
   cd yt-dash
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

   > **Nota:** En algunos sistemas Linux, puede que necesites instalar ffmpeg para la conversión de audio:
   > ```bash
   > # Ubuntu/Debian
   > sudo apt-get install ffmpeg
   > 
   > # macOS (con Homebrew)
   > brew install ffmpeg
   > 
   > # Windows: Descarga desde https://ffmpeg.org/download.html
   > ```

## 💻 Uso

**Ejecuta la aplicación:**
```bash
python yt_dash.py
```

O en sistemas Unix/Linux:
```bash
chmod +x yt_dash.py
./yt_dash.py
```

### Pasos para descargar:

1. **Copia la URL** del video de YouTube que deseas descargar
2. **Pega la URL** en el campo correspondiente
3. **Selecciona el formato**:
   - **MP4 (Video)** - Descarga el video completo
   - **MP3 (Audio)** - Solo descarga el audio
4. **Selecciona la calidad** (solo para MP4):
   - **Mejor calidad** - Máxima resolución disponible
   - **Calidad media (720p)** - Balance entre calidad y tamaño
   - **Calidad baja (480p)** - Menor tamaño de archivo
5. **Elige el directorio** donde guardar el archivo (por defecto: carpeta Descargas)
6. **Haz clic en "Descargar"** y espera a que termine

## 🖼️ Interfaz

La aplicación incluye:
- Campo de entrada para URL
- Selección de formato (MP3/MP4)
- Selección de calidad
- Selector de directorio de descarga
- Barra de progreso
- Área de registro de actividad

## 🛠️ Tecnologías

- **Python 3** - Lenguaje de programación
- **tkinter** - Framework para la interfaz gráfica (incluido con Python)
- **yt-dlp** - Librería para descargar videos de YouTube
- **threading** - Para operaciones asíncronas

## ⚠️ Notas Importantes

- Asegúrate de tener una conexión a Internet estable
- Respeta los derechos de autor del contenido que descargas
- Usa esta herramienta solo para contenido que tengas permiso de descargar
- Para descargas de audio (MP3), ffmpeg debe estar instalado en tu sistema

## 🐛 Solución de Problemas

**Error: "yt-dlp no está instalado"**
- Ejecuta: `pip install -r requirements.txt`

**Error al convertir a MP3**
- Instala ffmpeg en tu sistema

**La descarga es muy lenta**
- Verifica tu conexión a Internet
- Intenta con una calidad menor

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**YoeKimera**

## 🤝 Contribuciones

Las contribuciones, issues y solicitudes de características son bienvenidas.

---

**Descargo de responsabilidad:** Esta herramienta es para uso educativo y personal. Asegúrate de cumplir con los términos de servicio de YouTube y las leyes de derechos de autor aplicables.
