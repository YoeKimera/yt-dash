#!/usr/bin/env python3
"""
YT-DASH CLI - Versión de línea de comandos
Para usuarios que prefieren la terminal o sistemas sin GUI
"""

import sys
import os
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp no está instalado.")
    print("Ejecuta: pip install -r requirements.txt")
    sys.exit(1)


class ProgressLogger:
    """Logger para mostrar el progreso de descarga"""
    
    def __call__(self, d):
        if d['status'] == 'downloading':
            if '_percent_str' in d and '_speed_str' in d:
                print(f"\rDescargando: {d['_percent_str']} a {d['_speed_str']}", end='', flush=True)
        elif d['status'] == 'finished':
            print("\n✓ Descarga completada. Procesando...")


def download_video(url, format_type='mp4', quality='best', output_dir=None):
    """
    Descarga un video de YouTube
    
    Args:
        url: URL del video de YouTube
        format_type: 'mp4' o 'mp3'
        quality: 'best', 'medium' (720p), 'low' (480p)
        output_dir: Directorio de salida (por defecto: Downloads)
    """
    
    if output_dir is None:
        output_dir = str(Path.home() / "Downloads")
    
    # Crear directorio si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\n📥 Iniciando descarga...")
    print(f"URL: {url}")
    print(f"Formato: {format_type.upper()}")
    print(f"Calidad: {quality}")
    print(f"Destino: {output_dir}")
    print("-" * 60)
    
    # Configurar opciones
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'progress_hooks': [ProgressLogger()],
    }
    
    if format_type == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        # MP4
        if quality == 'best':
            format_string = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        elif quality == 'medium':
            format_string = 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best'
        else:  # low
            format_string = 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]/best'
        
        ydl_opts['format'] = format_string
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Video')
            print(f"\n✓ ¡Descarga exitosa!")
            print(f"📁 Archivo: {title}")
            return True
    except yt_dlp.utils.DownloadError as e:
        error_msg = str(e)
        if 'HTTP Error' in error_msg:
            print(f"\n✗ Error de red: No se pudo conectar al servidor")
            print(f"   Verifica tu conexión a Internet")
        elif 'Video unavailable' in error_msg or 'not available' in error_msg.lower():
            print(f"\n✗ Error: El video no está disponible")
            print(f"   Puede ser privado, estar bloqueado en tu región o haber sido eliminado")
        else:
            print(f"\n✗ Error al descargar: {error_msg}")
        return False
    except yt_dlp.utils.ExtractorError as e:
        print(f"\n✗ Error: URL inválida o formato no soportado")
        print(f"   Asegúrate de que la URL sea de YouTube")
        return False
    except PermissionError:
        print(f"\n✗ Error: No tienes permisos para escribir en el directorio")
        print(f"   Verifica los permisos de: {output_dir}")
        return False
    except KeyboardInterrupt:
        print(f"\n✗ Descarga cancelada por el usuario")
        return False
    except Exception as e:
        print(f"\n✗ Error inesperado: {str(e)}")
        print(f"   Si el problema persiste, revisa los logs o reporta el issue")
        return False


def main():
    """Función principal con interfaz CLI"""
    
    print("=" * 60)
    print("YT-DASH CLI - Descargador de YouTube")
    print("=" * 60)
    
    # Obtener URL
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("\nIngresa la URL de YouTube: ").strip()
    
    if not url:
        print("Error: URL no proporcionada")
        return 1
    
    # Validar URL
    if not url.startswith(('http://', 'https://')):
        print("Error: La URL debe comenzar con http:// o https://")
        return 1
    
    # Formato
    print("\nFormato:")
    print("  1. MP4 (Video)")
    print("  2. MP3 (Audio)")
    
    format_choice = input("Selecciona (1 o 2) [1]: ").strip() or "1"
    format_type = 'mp4' if format_choice == '1' else 'mp3'
    
    # Calidad (solo para MP4)
    quality = 'best'
    if format_type == 'mp4':
        print("\nCalidad:")
        print("  1. Mejor calidad")
        print("  2. Calidad media (720p)")
        print("  3. Calidad baja (480p)")
        
        quality_choice = input("Selecciona (1, 2 o 3) [1]: ").strip() or "1"
        quality_map = {'1': 'best', '2': 'medium', '3': 'low'}
        quality = quality_map.get(quality_choice, 'best')
    
    # Directorio de salida
    default_dir = str(Path.home() / "Downloads")
    output_dir = input(f"\nDirectorio de descarga [{default_dir}]: ").strip() or default_dir
    
    # Descargar
    success = download_video(url, format_type, quality, output_dir)
    
    return 0 if success else 1


def print_help():
    """Muestra ayuda"""
    help_text = """
Uso: python yt_dash_cli.py [URL]

Descarga videos de YouTube en formato MP4 o MP3.

Ejemplos:
  python yt_dash_cli.py
  python yt_dash_cli.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

Sin argumentos, el script te pedirá la información de forma interactiva.

Requisitos:
  - Python 3.8+
  - yt-dlp (pip install yt-dlp)
  - FFmpeg (solo para conversión a MP3)

Para la versión con interfaz gráfica, usa: python yt_dash.py
"""
    print(help_text)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print_help()
        sys.exit(0)
    
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n✗ Descarga cancelada por el usuario")
        sys.exit(1)
