import os
import subprocess
from moviepy.editor import AudioFileClip, ImageClip, vfx


def directorios():
    ruta = os.getcwd()
    rutaMusica = os.listdir(ruta)

    rutaProcesado = f"{ruta}/Procesado/"
    if not os.path.isdir(rutaProcesado):
        os.makedirs(rutaProcesado)

    return ruta, rutaMusica


def seleccionarPortada():
    archivo = os.listdir()
    portada = [f for f in archivo if f.endswith((".png", ".jpg", ".jpeg"))]
    if len(portada) != 1:
        raise ValueError(
            "Hay más de un archivo de imagen en la carpeta del script")

    return portada[0]


def crearVideo(ruta, rutaMusica, portada):
    for archivo in rutaMusica:
        if archivo.endswith(".mp3"):
            audio = AudioFileClip(archivo)
            clip = ImageClip(portada).set_duration(audio.duration)
            clip = clip.set_audio(audio)
            purple = (0.8, 0, 0.8)
            clip = clip.fx(vfx.colorx, purple)
            clip.write_videofile(f"{ruta}/Procesado/{archivo}.mp4", fps=24)
            clip.resize((1920, 1080))

            limpiarPantalla()

    print("¡Archivos creados satisfactoriamente!")


def borrarBasura(ruta):
    musicaResiduo = os.listdir(ruta)
    for archivo in musicaResiduo:
        rutaCompleta = os.path.join(ruta, archivo)
        if rutaCompleta.endswith('.mp3'):
            os.remove(rutaCompleta)


def limpiarPantalla():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)


def main():
    limpiarPantalla()
    ruta, rutaMusica = directorios()
    portada = seleccionarPortada()
    crearVideo(ruta, rutaMusica, portada)
    borrarBasura(ruta)


if "__main__" == __name__:
    main()
