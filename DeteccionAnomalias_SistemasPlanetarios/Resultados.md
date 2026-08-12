![](Images/portada.jpg)
 Detección de anomalías de sistemas planetarios
---
 
- [Detección de anomalías de sistemas planetarios](#detección-de-anomalías-de-sistemas-planetarios)
- [Introducción](#introducción)
- [Preprocesamiento](#preprocesamiento)
- [Análisis exploratorio](#análisis-exploratorio)
  - [Histogramas](#histogramas)
  - [Gráficas de dispersión](#gráficas-de-dispersión)
- [Selección de parámetros](#selección-de-parámetros)
  - [IF y LOF](#if-y-lof)
  - [Autodecodificador](#autodecodificador)
- [Resultados](#resultados)
  - [Autodecodificador](#autodecodificador-1)
  - [IF](#if)
  - [LOF](#lof)
  - [Anomalías detectadas](#anomalías-detectadas)
- [Conclusiones](#conclusiones)

---

## Introducción


Se importan el conjunto de datos proveniente de [https://exoplanetarchive.ipac.caltech.edu/docs/data.html ](https://exoplanetarchive.ipac.caltech.edu/docs/data.html). En este trabajo se realizará una detección de anomalías en las mediciones de los planetas mediante algoritmos de aprendizaje automático, entre los cuales se encuentran: 

1. Isolation Forest (IF):
2. Local Outlier Factor (LOF):
3. Autodecodificadores: 


## Preprocesamiento

En dicha liga nos dirigimos a "planetary systems" y se filtran aquellos datos que no cuenten con información de: 

1. Periodo orbital (pl_orbper)
2. Radio planetario (pl_rade)
3. Excentricidad (pl_orbeccen)
4. Temperatura en equilibrio (pl_eqt)
5. Masa estelar (st_mass)
6. Gravedad estelar en superficie (st_logg)
7. Distancia a la estrella (sy_dist)

Se eliminan aquellos datos que cuenten con valores nulos y se realiza una normalización  para evitar que alguna variable sea dominante respecto a las demás debido a las diferentes escalas. Después de todas estas consideraciones nuestro conjunto de datos consta de 14,037 filas y 7 columnas ya antes descritas. 


## Análisis exploratorio

### Histogramas

Para empezar a trabajar se realizan histogramas de cada una de las variables. En lo que respecta a la masa estelar, gravedad estelar en superficie y distancia a la estrella se notan distribuciones semejantes a la normal, o en dado caso con un cierto sesgo a la izquierda. 

| ![](Imagenes/Histogramas/histograma_st_mass.png) | ![](Imagenes/Histogramas/histograma_st_logg.png) |
| ------------------------------------------------ | ------------------------------------------------ |
| (a)  Masa estelar                                            | (b) Gravedad estelar en superficie                                              |

| ![](Imagenes/Histogramas/histograma_pl_eqt.png) | ![](Imagenes/Histogramas/histograma_sy_dist.png) |
| ----------------------------------------------- | ------------------------------------------------ |
| (c) Temperatura de equilibrio                                          | (d) Distancia a la estrella                                            |

---

Por otro lado, en las siguientes figuras se muestran el resto de las variables, donde se nota claramente que hay exoplanetas que se alejan mucho del promedio, ya que cuentan con valores significativamente mayores si los comparas con el resto de los datos. A continuación se realizarán gráficos de dispersión para ver mas a detalle estas diferencias. 



| ![](Imagenes/Histogramas/histograma_pl_orbeccen.png) | ![](Imagenes/Histogramas/histograma_pl_orbper.png) |
| ---------------------------------------------------- | -------------------------------------------------- |
| (a) Excentricidad                                          | (b)Periodo orbital                                           |

|   | ![](Imagenes/Histogramas/histograma_pl_rade.png) |   |
| - | ------------------------------------------------ | - |
|   | (c) Radio planetario                                         |   |

---

### Gráficas de dispersión
Para tener mejor visualización de los variables restantes se opta por usar gráficas de dispersión. En ella los índices se muestran sobre el eje x mientras que en las abscisas indicamos el valor de la variable a utilizar. Seleccionamos un umbral donde se ubiquen el 95% de los datos y a partir de ellos iremos identificando exoplanetas fuera de lo común. 



| ![](Imagenes/Dispersion/dispersion_pl_orbper.png_general.png) | ![](Imagenes/Dispersion/dispersion_pl_orbper.png) |
| ------------------------------------------------------------- | ------------------------------------------------- |
| (a) Periodo Orbital                                                     | (b)  Explanetas fuera del umbral                                            |

| ![](Imagenes/Dispersion/dispersion_pl_rade.png_general.png) | ![](Imagenes/Dispersion/dispersion_pl_rade.png) |
| ----------------------------------------------------------- | ----------------------------------------------- |
| (c) Radio Planetario                                                    | (d) Exoplanetas fuera del umbral                                          |

| ![](Imagenes/Dispersion/dispersion_pl_orbeccen.png_general.png) | ![](Imagenes/Dispersion/dispersion_pl_orbeccen.png) |
| --------------------------------------------------------------- | --------------------------------------------------- |
| (e)   
Excentrecidad                                                          | (f) Exoplanteas fuera del umbral                                                |

En lo que respecta al periodo orbital se muestra que el exoplaneta EPIC 248847494 b tiene el valor más alto registrado, consultando el dataset corresponde a un periodo orbital de 10 años. Esto resulta relevante debido a que los métodos de observación requieren que el exoplaneta realice varios giros a la orbita para ser detectado, por lo que periodos largos necesitarían un mayor tiempo de seguimiento. 

---

## Selección de parámetros

### IF y LOF

Los parámetros a escoger para trabajar con IF y LOF son el número de árboles de decisión y el número de vecinos respectivamente. Para determinar los valores adecuados se realizan las siguientes gráficas, dónde se muestran como varia el número de anomalías respecto al valor del variable a analizar, se espera determinar si existe alguna convergencia. 

| ![](Imagenes/SeleccionParametros/Anomalias_vs_Trees.png) | ![](Imagenes/SeleccionParametros/Anomalias_vs_Vecinos.png) |
| -------------------------------------------------------- | ---------------------------------------------------------- |
| (a) Convergencia IF                                                 | (b)   Convergencia LOF                                                     |

Al analizar la gráficas de convergencia se decide seleccionar 100 árboles de decisión y 10 vecinos para trabajar con nuestros datos, puesto que aparenta que existe estabilidad alrededor de esos valores. 



---

### Autodecodificador

Una red autocodificadora recibe de entrada los datos a analizar, pasa por una serie de capas, las cuales van disminuyendo gradualmente el número de neuronas para poder comprimir la información en un espacio latente, para luego descomprimirla en un proceso inverso. En la siguiente figura se esquematiza la arquitectura empleada para este trabajo, las capas son representadas mediante rectángulos azules dónde la parte superior indica el número de neuronas que poseen. Se emplearon funciones de activación *tanh* en las capas ocultas. Se usa MSE como función de pérdida. El espacio latente lo podemos emplear para la representación en dos dimensiones de nuestros datos.

Podemos usar una red autodecodificadora para detectar anomalías si consideramos que aquellos datos que resulten más difícil de reconstruir, es decir los que cuenten con un alto valor de MSE, son anormales, es decir, a la red le costará más trabajo decodificar aquellos exoplanetas que no sean tan comunes, pues el conjunto de sus características no se presentan a menudo. 

<p align="center">
  <img src="Imagenes/SeleccionParametros/Autoencoder.jpg" width="50%">
</p>
Para el entrenamiento:

* 80 % de los datos se emplean para el entrenamiento y 20% para pruebas.
* 100 épocas y un tamaño de batch de 32.


---

## Resultados

### Autodecodificador
Se nota el decremento del MSE con el
pasar de las épocas.El modelo pudo superar
2 mínimos locales de la función de
pérdida.


![](Imagenes/SeleccionParametros/AutocodificadorEntrenamiento.png)

El 95% de los datos se encuentran por debajo de un umbral de 0.0017, por lo que consideraremos como anomalos aquellos que superen este umbral. 

![](Imagenes/SeleccionParametros/MSE_Dispersionpng.png)

Para poder representar nuestros datos se utilizaran 2 métodos de reducción de dimensionalidad. El primero de ellos consiste en representar los datos mediante la salida del espacio latente del modelo (recordemos que este consta de 2 dimensiones). El segundo método para visualizar sera por componentes principales (PCA). 



| ![](Imagenes/ReduccionDimensional/Autoencoder_Bottleneck.png) | ![](Imagenes/ReduccionDimensional/PCA_Test_Autoencoder.png) |
| ------------------------------------------------------------- | ----------------------------------------------------------- |
| (a) Espacio latente del autodecodificador                                                        | (b) PCA                                              |



### IF
En este caso el valores bajos de scoreIF indican que el dato es más anómalo. IF parece bien representado en ambos algoritmos de reducción de dimensionalidad. A pesar de no ser entrenado explícitamente con estos pares de coordenadas parece indicar que
se fija en las regiones menos densas para seleccionar anomalías.


| ![](Imagenes/ReduccionDimensional/Autoencoder_Test_scoreIF.png) | ![](Imagenes/ReduccionDimensional/PCA_Test_scoreIF.png) |
| ------------------------------------------------------------- | ----------------------------------------------------------- |
| (a) Espacio latente del autodecodificador                                                           | (b) PCA                                                       |


### LOF

Debido a que este algoritmo se basa en densidad y al existir 7 dimensiones en este conjunto de datos, las representaciones bidimensionales presentadas no parece mostrarse regiones preferenciales para las anomalias. Recordemos que cualquier algortimo de reducción de dimensionalidad, en ultima instancia, es una proyección de la realidad, por lo que es posible que los patrones que encontremos solo sean posibles notarlos en mayores dimensiones o desde una proyección distinta. Más sin embargo este método tambien encontró a EPIC 248847494 b como una anomalía. 


| ![](Imagenes/ReduccionDimensional/Autoencoder_Test_scoreLOF.png) | ![](Imagenes/ReduccionDimensional/PCA_Test_scoreLOF.png) |
| ------------------------------------------------------------- | ----------------------------------------------------------- |
| (a) Espacio latente del autodecodificador                                                           | (b) PCA                                                        |


### Anomalías detectadas

A continuación se muestra una gráfica de barras con el conteo de las anomalias por cada método empleado. Podemos observar que IF fue el sensible, mientras que el menor conteo tuvo fue LOF. El autodecodificador se quedo en un rango intermedio. 

<p align="center">
  <img src="Imagenes/ReduccionDimensional/AnomaliasDetectadas.png" width="50%">
</p>

Los 3 métodos detectaron tuvieron coincidencia en 79 planetas, entre los cuales se encuentran: Kepler-39 b, KELT-9 b, EPIC 248847494 b, KIC 9663113 b,HD 224018 d, Kepler-141 c, entre otros. A continuación se muestran las anomalías comunes de los 3 métodos representados en los espacios bidimensionales de PCA y el autodecodificador. 

| ![](Imagenes/ReduccionDimensional/PCA_Comunes.png) | ![](Imagenes/ReduccionDimensional/Autoencoder_Comunes.png) |
| ------------------------------------------------------------- | ----------------------------------------------------------- |
| (a)                                                           | (b)                                                         |

## Conclusiones
Los análisis exploratorios nos pueden ayudar a darnos una idea si algún dato se encuentra fuera de lo común.
Se pueden emplear los autocodificadores para detectar anomalías si nos enfocamos a analizar que tan bien se reconstruyen los datos. Mayores errores podría indicarnos la presencia de un dato extraño. Escoger la arquitectura lleva su reto, ya que no parece existir una “receta” que nos indique como armar un modelo. Se recomienda primero revisar en la literatura si existen redes empleadas para el fenómeno que se este analizando y no empezar desde cero.
Los algoritmos de reducción de dimensionalidad parecen ser muy atractivos para representar datos pero siempre hay que tener en consideración que la
salida de estos son una “sombra” de la realidad.