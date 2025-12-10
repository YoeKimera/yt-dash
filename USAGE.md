# Guía de Uso de YT-DASH

## Inicio Rápido

### 1. Instalación

Primero, asegúrate de tener Python 3.8 o superior instalado:

```bash
python --version
```

Luego instala las dependencias:

```bash
pip install -r requirements.txt
```

### 2. Ejecutar la Aplicación

```bash
python yt_dash.py
```

## Ejemplos de Uso

### Descargar Video en MP4

1. Copia la URL del video de YouTube (por ejemplo: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`)
2. Pega la URL en el campo "URL de YouTube"
3. Selecciona "MP4 (Video)"
4. Selecciona la calidad deseada:
   - **Mejor calidad**: Descarga en la mejor resolución disponible (puede ser 4K, 1080p, etc.)
   - **Calidad media (720p)**: Buena calidad, menor tamaño
   - **Calidad baja (480p)**: Para ahorrar espacio
5. Haz clic en "Descargar"

### Descargar Audio en MP3

1. Copia la URL del video de YouTube
2. Pega la URL en el campo "URL de YouTube"
3. Selecciona "MP3 (Audio)"
4. Haz clic en "Descargar"

> **Nota**: Para descargar audio en MP3, necesitas tener **FFmpeg** instalado en tu sistema.

### Cambiar el Directorio de Descarga

Por defecto, los archivos se guardan en la carpeta "Downloads" de tu usuario. Para cambiar esto:

1. Haz clic en el botón "Examinar..."
2. Selecciona la carpeta donde quieres guardar tus descargas
3. La nueva ruta se mostrará en el campo "Guardar en:"

## Requisitos del Sistema

### Requisitos Mínimos

- **Sistema Operativo**: Windows 7+, macOS 10.12+, o Linux (cualquier distribución moderna)
- **Python**: 3.8 o superior
- **RAM**: 512 MB (1 GB recomendado)
- **Espacio en disco**: Depende de los videos que descargues
- **Conexión a Internet**: Requerida

### Dependencias Adicionales

#### FFmpeg (Para MP3)

Para convertir videos a MP3, necesitas instalar FFmpeg:

**Windows:**
1. Descarga FFmpeg desde [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extrae el archivo ZIP
3. Añade la carpeta `bin` a tu PATH del sistema

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**Fedora:**
```bash
sudo dnf install ffmpeg
```

## Características Avanzadas

### Formatos Soportados

La aplicación utiliza yt-dlp, que soporta una amplia variedad de sitios web además de YouTube. Sin embargo, esta GUI está optimizada para YouTube.

### Resolución de Problemas

#### "No se puede conectar al servidor"

- Verifica tu conexión a Internet
- Asegúrate de que YouTube no esté bloqueado en tu red
- Intenta con una URL diferente

#### "Error al convertir a MP3"

- Instala FFmpeg en tu sistema
- Verifica que FFmpeg esté en tu PATH
- En la terminal/cmd, ejecuta: `ffmpeg -version`

#### "Descarga muy lenta"

- Tu velocidad de descarga depende de tu conexión a Internet
- Los videos de mayor calidad tardan más en descargarse
- Intenta con una calidad menor (480p o 720p)

#### "La aplicación no inicia"

- Verifica que Python esté instalado correctamente
- Asegúrate de que tkinter esté instalado (viene con Python en la mayoría de instalaciones)
- En Linux, puede que necesites instalar: `sudo apt-get install python3-tk`

## Consejos y Mejores Prácticas

1. **Calidad vs Tamaño**: Si tienes espacio limitado, usa 720p o 480p
2. **Solo audio**: Si solo quieres la música, descarga en MP3 para ahorrar espacio
3. **Listas de reproducción**: Actualmente la app está diseñada para videos individuales
4. **Conexión estable**: Asegúrate de tener una buena conexión para evitar descargas interrumpidas

## Legalidad y Ética

⚠️ **IMPORTANTE**:

- Solo descarga contenido del que tengas permiso o que esté bajo licencia libre
- Respeta los derechos de autor de los creadores
- No distribuyas contenido protegido por derechos de autor
- Consulta los términos de servicio de YouTube
- Esta herramienta es para uso personal y educativo

## Preguntas Frecuentes

**P: ¿Puedo descargar playlists completas?**  
R: Actualmente la aplicación está diseñada para videos individuales. Puedes descargar videos uno por uno.

**P: ¿Funciona con otros sitios además de YouTube?**  
R: Aunque yt-dlp soporta muchos sitios, esta GUI está optimizada específicamente para YouTube.

**P: ¿Los videos se descargan con subtítulos?**  
R: Actualmente la aplicación descarga solo video y audio. Los subtítulos no están incluidos en esta versión.

**P: ¿Puedo usar la aplicación sin conexión a Internet?**  
R: No, necesitas conexión a Internet para descargar videos de YouTube.

**P: ¿Es seguro usar esta aplicación?**  
R: Sí, el código es open source y puedes revisarlo. Usa librerías oficiales y no contiene malware.

## Soporte

Si encuentras problemas o tienes sugerencias:

1. Revisa la sección de "Resolución de Problemas" arriba
2. Verifica que tienes todas las dependencias instaladas
3. Abre un issue en GitHub con detalles del problema

## Actualizaciones

Para actualizar yt-dlp a la última versión:

```bash
pip install --upgrade yt-dlp
```

Esto asegura compatibilidad con los últimos cambios de YouTube.
