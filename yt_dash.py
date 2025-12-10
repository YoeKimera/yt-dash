#!/usr/bin/env python3
"""
YT-DASH - Interfaz Gráfica de Escritorio para YT-DLP
Descarga videos de YouTube en formato MP3 o MP4
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
from pathlib import Path
import sys

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp no está instalado. Por favor ejecuta: pip install -r requirements.txt")
    sys.exit(1)


class YTDashGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YT-DASH - Descargador de YouTube")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Variables
        self.download_path = tk.StringVar(value=str(Path.home() / "Downloads"))
        self.url_var = tk.StringVar()
        self.format_var = tk.StringVar(value="mp4")
        self.quality_var = tk.StringVar(value="best")
        self.is_downloading = False
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="YT-DASH - Descargador de YouTube", 
                                font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # URL Input
        ttk.Label(main_frame, text="URL de YouTube:").grid(row=1, column=0, sticky=tk.W, pady=5)
        url_entry = ttk.Entry(main_frame, textvariable=self.url_var, width=50)
        url_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Formato Selection
        format_frame = ttk.LabelFrame(main_frame, text="Formato", padding="10")
        format_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Radiobutton(format_frame, text="MP4 (Video)", variable=self.format_var, 
                       value="mp4").grid(row=0, column=0, padx=10)
        ttk.Radiobutton(format_frame, text="MP3 (Audio)", variable=self.format_var, 
                       value="mp3").grid(row=0, column=1, padx=10)
        
        # Calidad Selection
        quality_frame = ttk.LabelFrame(main_frame, text="Calidad", padding="10")
        quality_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Radiobutton(quality_frame, text="Mejor calidad", variable=self.quality_var, 
                       value="best").grid(row=0, column=0, padx=10)
        ttk.Radiobutton(quality_frame, text="Calidad media (720p)", variable=self.quality_var, 
                       value="medium").grid(row=0, column=1, padx=10)
        ttk.Radiobutton(quality_frame, text="Calidad baja (480p)", variable=self.quality_var, 
                       value="low").grid(row=0, column=2, padx=10)
        
        # Directorio de descarga
        dir_frame = ttk.Frame(main_frame)
        dir_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        dir_frame.columnconfigure(1, weight=1)
        
        ttk.Label(dir_frame, text="Guardar en:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(dir_frame, textvariable=self.download_path, state="readonly").grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(dir_frame, text="Examinar...", command=self.browse_directory).grid(
            row=0, column=2)
        
        # Botón de descarga
        self.download_btn = ttk.Button(main_frame, text="Descargar", 
                                       command=self.start_download, 
                                       style="Accent.TButton")
        self.download_btn.grid(row=5, column=0, columnspan=3, pady=20)
        
        # Barra de progreso
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # Área de log/status
        log_frame = ttk.LabelFrame(main_frame, text="Estado", padding="5")
        log_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(7, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=10, wrap=tk.WORD)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Mensaje inicial
        self.log("¡Bienvenido a YT-DASH!")
        self.log("Pega la URL de YouTube y selecciona el formato para descargar.")
        
    def browse_directory(self):
        """Abre un diálogo para seleccionar el directorio de descarga"""
        directory = filedialog.askdirectory(initialdir=self.download_path.get())
        if directory:
            self.download_path.set(directory)
            self.log(f"Directorio de descarga cambiado a: {directory}")
    
    def log(self, message):
        """Añade un mensaje al área de log"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def progress_hook(self, d):
        """Hook para actualizar el progreso de la descarga"""
        if d['status'] == 'downloading':
            # Extraer información de progreso
            if 'downloaded_bytes' in d and 'total_bytes' in d:
                percent = d['downloaded_bytes'] / d['total_bytes'] * 100
                speed = d.get('speed', 0)
                eta = d.get('eta', 0)
                
                speed_str = f"{speed / 1024 / 1024:.2f} MB/s" if speed else "N/A"
                self.log(f"Descargando... {percent:.1f}% - Velocidad: {speed_str}")
            elif '_percent_str' in d:
                self.log(f"Descargando... {d['_percent_str']}")
        elif d['status'] == 'finished':
            self.log("Descarga completada. Procesando archivo...")
    
    def download_video(self):
        """Función que realiza la descarga en un hilo separado"""
        url = self.url_var.get().strip()
        
        if not url:
            self.log("Error: Por favor ingresa una URL válida")
            return
        
        if not url.startswith(('http://', 'https://')):
            self.log("Error: La URL debe comenzar con http:// o https://")
            return
        
        try:
            # Configurar opciones de yt-dlp
            ydl_opts = {
                'outtmpl': os.path.join(self.download_path.get(), '%(title)s.%(ext)s'),
                'progress_hooks': [self.progress_hook],
                'quiet': False,
                'no_warnings': False,
            }
            
            # Configurar según el formato seleccionado
            if self.format_var.get() == "mp3":
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                })
                self.log("Formato: MP3 (Audio)")
            else:
                # MP4 Video
                quality = self.quality_var.get()
                if quality == "best":
                    format_string = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
                elif quality == "medium":
                    format_string = 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best'
                else:  # low
                    format_string = 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]/best'
                
                ydl_opts['format'] = format_string
                self.log(f"Formato: MP4 (Video) - Calidad: {quality}")
            
            self.log(f"Iniciando descarga de: {url}")
            self.log(f"Guardando en: {self.download_path.get()}")
            
            # Realizar la descarga
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', 'Video')
                self.log(f"✓ Descarga completada exitosamente: {title}")
                
        except yt_dlp.utils.DownloadError as e:
            error_msg = str(e)
            if 'HTTP Error' in error_msg:
                self.log("✗ Error de red: No se pudo conectar al servidor")
                self.log("  Verifica tu conexión a Internet")
            elif 'Video unavailable' in error_msg or 'not available' in error_msg.lower():
                self.log("✗ Error: El video no está disponible")
                self.log("  Puede ser privado, estar bloqueado o haber sido eliminado")
            else:
                self.log(f"✗ Error al descargar: {error_msg}")
        except yt_dlp.utils.ExtractorError:
            self.log("✗ Error: URL inválida o formato no soportado")
            self.log("  Asegúrate de que la URL sea de YouTube")
        except PermissionError:
            self.log(f"✗ Error: No tienes permisos para escribir en el directorio")
            self.log(f"  Verifica los permisos de: {self.download_path.get()}")
        except Exception as e:
            self.log(f"✗ Error inesperado: {str(e)}")
            self.log("  Si el problema persiste, revisa la configuración")
        finally:
            self.is_downloading = False
            self.download_btn.config(state="normal", text="Descargar")
            self.progress.stop()
    
    def start_download(self):
        """Inicia la descarga en un hilo separado"""
        if self.is_downloading:
            self.log("Ya hay una descarga en progreso...")
            return
        
        self.is_downloading = True
        self.download_btn.config(state="disabled", text="Descargando...")
        self.progress.start()
        
        # Ejecutar descarga en un hilo separado para no bloquear la UI
        download_thread = threading.Thread(target=self.download_video, daemon=True)
        download_thread.start()


def main():
    """Función principal"""
    root = tk.Tk()
    app = YTDashGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
