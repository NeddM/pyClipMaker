# Resumen del script

Este script recibe una serie de audios (normalmente de un mismo album de música), y también una imagen (sólo funcionará si hay exactamente una imagen).

El script creará un clip de vídeo por cada audio, de la duración del audio, y con la imagen estática.

Es un video parecido a los que sube Youtube Music automáticamente.

# Dependencias

Necesitamos tener instalada la librería `moviepy`.

```python
pip install moviepy
```

# Uso

-   Introduce en la carpeta raíz los audios.
-   Introduce en la carpeta raíz una imagen.
-   Se generará una carpeta llamada _procesado_, donde se guardarán los videos creados.
