import os
import subprocess

# Verifique se o FFmpeg pode ser executado
ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
try:
    subprocess.run([ffmpeg_path, "-version"], check=True)
    print("FFmpeg está acessível!")
except FileNotFoundError:
    print("FFmpeg não foi encontrado no caminho especificado.")
except subprocess.CalledProcessError:
    print("Erro ao tentar executar o FFmpeg.")
