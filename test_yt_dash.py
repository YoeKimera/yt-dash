#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad de descarga de YT-DASH
Este script NO requiere GUI y puede ejecutarse en entornos sin interfaz gráfica
"""

import sys
import os

try:
    import yt_dlp
    print("✓ yt-dlp está instalado correctamente")
    print(f"  Versión: {yt_dlp.version.__version__}")
except ImportError:
    print("✗ Error: yt-dlp no está instalado")
    print("  Ejecuta: pip install -r requirements.txt")
    sys.exit(1)

def test_ytdlp_config():
    """Prueba las configuraciones de yt-dlp sin descargar"""
    print("\n--- Probando configuraciones de yt-dlp ---")
    
    # Configuración para MP4
    mp4_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
    }
    print("✓ Configuración MP4 (video):")
    print(f"  Format: {mp4_opts['format']}")
    
    # Configuración para MP3
    mp3_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
    }
    print("✓ Configuración MP3 (audio):")
    print(f"  Format: {mp3_opts['format']}")
    print(f"  Postprocessor: FFmpegExtractAudio -> MP3")
    
    # Verificar que se puede instanciar YoutubeDL
    try:
        with yt_dlp.YoutubeDL(mp4_opts) as ydl:
            print("✓ YoutubeDL se puede instanciar con config MP4")
        
        with yt_dlp.YoutubeDL(mp3_opts) as ydl:
            print("✓ YoutubeDL se puede instanciar con config MP3")
    except Exception as e:
        print(f"✗ Error al instanciar YoutubeDL: {e}")
        return False
    
    return True

def main():
    print("=" * 60)
    print("YT-DASH - Test de Funcionalidad")
    print("=" * 60)
    
    # Verificar Python
    print(f"\n✓ Python version: {sys.version.split()[0]}")
    
    # Test de configuraciones
    if test_ytdlp_config():
        print("\n" + "=" * 60)
        print("✓ TODAS LAS PRUEBAS PASARON")
        print("=" * 60)
        print("\nLa aplicación YT-DASH está lista para usar.")
        print("Ejecuta 'python yt_dash.py' para iniciar la interfaz gráfica.")
        print("\nNOTA: La GUI requiere tkinter, que viene con Python en la")
        print("      mayoría de instalaciones de escritorio.")
        return 0
    else:
        print("\n✗ ALGUNAS PRUEBAS FALLARON")
        return 1

if __name__ == "__main__":
    sys.exit(main())
