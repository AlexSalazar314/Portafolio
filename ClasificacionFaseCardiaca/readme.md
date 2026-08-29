# Detección de fase cardíaca en ecocardiogramas de murinos

### Clasificador de sístole y diástole

Este proyecto presenta la implementación de una **red neuronal convolucional (CNN)** para la clasificación de fases cardíacas —**sístole y diástole**— en imágenes de ecocardiogramas de corazones de ratones de laboratorio.

El objetivo es desarrollar un modelo capaz de identificar automáticamente la fase del ciclo cardíaco a partir de imágenes ecocardiográficas.

## Contenido del repositorio

El repositorio contiene tres notebooks correspondientes a las principales etapas del desarrollo y evaluación del modelo:

* **Entrenamiento y validación con imágenes phantom:** entrenamiento inicial y evaluación de la red utilizando imágenes phantom.
* **Validación cruzada K-Fold:** evaluación del desempeño del modelo mediante validación cruzada.
* **Modelo final:** entrenamiento y evaluación de la arquitectura seleccionada como modelo final.

La descripción detallada de la metodología, experimentos y resultados se encuentra en el documento [proyecto](/ClasificacionFaseCardiaca/Proyecto.pdf). 


## Estructura del repositorio

```text
├── notebooks/
│   ├── EntreamientoSpeckles.ipynb
│   ├── EntrenamientoGrupoControlKfolds.ipynb
│   └── EntrenamientoFinal.ipynb
│
├── datasets/
│   ├── GrupoControl
│   └── phantomsSpeckle.ipynb
│
├── resultados/
│   └── ...
│
├── proyecto.pdf
│   
│
└── README.md
```

### Datasets

La carpeta [datasets](/ClasificacionFaseCardiaca/datasets/) contiene los conjuntos de datos utilizados durante los experimentos.

### Resultados

La carpeta [results](/ClasificacionFaseCardiaca/results/)contiene las imágenes generadas durante los experimentos y los pesos correspondientes a los modelos entrenados.

## Librerías

* **Python**
* **TensorFlow / Keras** — construcción y entrenamiento de la red neuronal convolucional (CNN).
* **NumPy** — manipulación y procesamiento de datos numéricos.
* **OpenCV (cv2)** — procesamiento y manipulación de imágenes.
* **Pandas** — manejo y análisis de datos.
* **Matplotlib** — visualización de resultados y métricas.
* **Scikit-learn** — evaluación del modelo y generación de la matriz de confusión.


