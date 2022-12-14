import os
from PIL import Image
from moviepy.editor import AudioFileClip, ImageClip, vfx, ColorClip, VideoFileClip


def directorios():
    ruta = os.getcwd()
    rutaMusica = os.listdir(ruta)

    rutaProcesado = f"{ruta}/Procesado/"
    if not os.path.isdir(rutaProcesado):
        os.makedirs(rutaProcesado)

    return ruta, rutaMusica


def seleccionarPortada():
    files = os.listdir()
    image_files = [f for f in files if f.endswith((".png", ".jpg", ".jpeg"))]
    if len(image_files) != 1:
        raise ValueError(
            "Hay más de un archivo de imagen en la carpeta del script")

    return image_files[0]


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


def borrarBasura(ruta):
    musicaResiduo = os.listdir(ruta)
    for archivo in musicaResiduo:
        rutaCompleta = os.path.join(ruta, archivo)
        if rutaCompleta.endswith('.mp3'):
            os.remove(rutaCompleta)


def main():
    ruta, rutaMusica = directorios()
    portada = seleccionarPortada()
    crearVideo(ruta, rutaMusica, portada)
    borrarBasura(ruta)


if "__main__" == __name__:
    main()
