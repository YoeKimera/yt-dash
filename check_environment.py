#!/usr/bin/env python3
"""
Script para verificar que el entorno está correctamente configurado para YT-DASH
"""

import sys
import subprocess

def check_python_version():
    """Verifica la versión de Python"""
    version = sys.version_info
    print(f"Python versión: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✓ Python version es compatible (3.8+)")
        return True
    else:
        print("✗ Python version es muy antigua. Se requiere Python 3.8 o superior.")
        return False

def check_module(module_name, package_name=None):
    """Verifica si un módulo está instalado"""
    if package_name is None:
        package_name = module_name
    
    try:
        __import__(module_name)
        print(f"✓ {package_name} está instalado")
        return True
    except ImportError:
        print(f"✗ {package_name} NO está instalado")
        return False

def check_ffmpeg():
    """Verifica si FFmpeg está instalado"""
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"✓ FFmpeg está instalado: {version_line}")
            return True
        else:
            print("✗ FFmpeg está instalado pero hay un problema")
            return False
    except FileNotFoundError:
        print("✗ FFmpeg NO está instalado (necesario para MP3)")
        print("  Instálalo desde: https://ffmpeg.org/")
        return False
    except subprocess.TimeoutExpired:
        print("✗ FFmpeg no responde (timeout)")
        return False
    except Exception as e:
        print(f"✗ Error al verificar FFmpeg: {e}")
        return False

def main():
    print("=" * 70)
    print("YT-DASH - Verificación de Entorno")
    print("=" * 70)
    print()
    
    checks = []
    
    # Verificar Python
    print("1. Verificando Python...")
    checks.append(check_python_version())
    print()
    
    # Verificar módulos esenciales
    print("2. Verificando módulos esenciales...")
    checks.append(check_module('tkinter', 'tkinter (GUI)'))
    checks.append(check_module('threading'))
    checks.append(check_module('pathlib'))
    print()
    
    # Verificar yt-dlp
    print("3. Verificando yt-dlp...")
    if check_module('yt_dlp', 'yt-dlp'):
        try:
            import yt_dlp
            print(f"  Versión de yt-dlp: {yt_dlp.version.__version__}")
        except Exception as e:
            print(f"  No se pudo obtener la versión: {e}")
    else:
        print("  Instala con: pip install -r requirements.txt")
        checks.append(False)
    print()
    
    # Verificar FFmpeg
    print("4. Verificando FFmpeg (opcional para MP3)...")
    ffmpeg_ok = check_ffmpeg()
    print()
    
    # Resumen
    print("=" * 70)
    if all(checks):
        print("✓ ENTORNO CONFIGURADO CORRECTAMENTE")
        print()
        print("Todo está listo para usar YT-DASH!")
        print("Ejecuta: python yt_dash.py")
        
        if not ffmpeg_ok:
            print()
            print("NOTA: FFmpeg no está instalado. Podrás descargar videos (MP4)")
            print("      pero NO podrás convertir a audio (MP3).")
    else:
        print("✗ FALTAN ALGUNAS DEPENDENCIAS")
        print()
        print("Por favor, resuelve los problemas indicados arriba.")
        if not all(checks):
            print()
            print("Para instalar las dependencias de Python:")
            print("  pip install -r requirements.txt")
    print("=" * 70)
    
    return 0 if all(checks) else 1

if __name__ == "__main__":
    sys.exit(main())
