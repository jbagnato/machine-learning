# Object tracking con Yolo v8 y algoritmo ByteTrack

## Instalación del ambiente de desarrollo

Instala un environment de python 3.9. Si tienes Anaconda instalado puedes hacerlo ejecutando:

```sh
    conda create -n tracking python=3.9 numpy
```

Y luego activa el ambiente con

```sh
    conda activate tracking
```


> NOTA: En Windows, será necesario que instales las librerias de C++. Para ello deberás descargar e instalarlas mediante este enlace:
Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

luego instalamos los requerimientos para el proyecto:

```sh
    pip install -r requirements.txt
```

# Si vas a usar la version Jupyter Notebook

Si vas a ejecutar desde una notebook deberás instalar:

```sh
conda install -n tracking ipykernel --update-deps --force-reinstall
```

## Uso del Script

Al ejecutar por primera vez, se descargará el modelo de Yolo solicitado, por ejemplo yolov8n.pt de 6MB

```sh
python detectar.py
```
