# YT-DASH - Guía de Inicio Rápido

## Instalación Rápida (3 pasos)

### 1. Verificar Python
```bash
python --version
```
Necesitas Python 3.8 o superior.

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la Aplicación

**Interfaz Gráfica:**
```bash
python yt_dash.py
```

**Línea de Comandos:**
```bash
python yt_dash_cli.py
```

## Uso Básico

### Descargar un Video

1. Copia la URL de YouTube
2. Pega en la aplicación
3. Selecciona MP4 (Video) o MP3 (Audio)
4. Click en "Descargar"

### Ejemplo CLI

```bash
# Modo interactivo
python yt_dash_cli.py

# Con URL directa
python yt_dash_cli.py https://www.youtube.com/watch?v=VIDEO_ID
```

## Solución Rápida de Problemas

### Error: "tkinter no está instalado"
**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

**Alternativa:** Usa la versión CLI
```bash
python yt_dash_cli.py
```

### Error: "yt-dlp no está instalado"
```bash
pip install -r requirements.txt
```

### Error al convertir a MP3
Instala FFmpeg:
- **Windows:** https://ffmpeg.org/download.html
- **macOS:** `brew install ffmpeg`
- **Linux:** `sudo apt-get install ffmpeg`

## Verificar Instalación

```bash
python check_environment.py
```

Este script verifica que todo esté correctamente instalado.

## Archivos del Proyecto

- `yt_dash.py` - Aplicación con interfaz gráfica (GUI)
- `yt_dash_cli.py` - Versión de línea de comandos
- `check_environment.py` - Verificador de entorno
- `test_yt_dash.py` - Tests de funcionalidad
- `requirements.txt` - Dependencias de Python
- `README.md` - Documentación completa
- `USAGE.md` - Guía detallada de uso

## Características

✅ Interfaz gráfica intuitiva  
✅ Descarga en MP3 o MP4  
✅ Selección de calidad  
✅ Barra de progreso  
✅ Versión CLI incluida  
✅ Sin publicidad ni malware  

## Soporte

- Documentación completa: Ver `README.md`
- Guía de uso detallada: Ver `USAGE.md`
- Issues en GitHub: https://github.com/YoeKimera/yt-dash/issues

---

**¡Disfruta descargando tus videos favoritos de YouTube!** 🎥🎵
