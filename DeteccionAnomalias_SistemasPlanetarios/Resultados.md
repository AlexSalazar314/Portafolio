![](Images/portada.jpg)
# Detección de anomalías de sistemas planetarios

!Hola! Bienvenido a mi portafolio de proyectos. En este espacio encontrarás algunos trabajos que he realizado en materias relacionadas a ciencias de datos, visión computacional, aprendizaje automático, entre otros.


- [Detección de anomalías de sistemas planetarios](#detección-de-anomalías-de-sistemas-planetarios)
  - [Preprocesamiento](#preprocesamiento)
  - [Análisis exploratorio](#análisis-exploratorio)
  - [Selección de parámetros](#selección-de-parámetros)
    - [IF y LOF](#if-y-lof)
    - [Autodecodificador](#autodecodificador)
  - [Resultados](#resultados)
    - [Autodecodificador](#autodecodificador-1)
  - [Conclusiones](#conclusiones)


## Preprocesamiento 
## Análisis exploratorio

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">

  <div style="text-align: center;">
    <img src="Imagenes/Histogramas/histograma_st_mass.png" width="100%">
    <p>(a) Imagen 1</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes/Histogramas/histograma_st_logg.png" width="100%">
    <p>(b) Imagen 2</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes/Histogramas/histograma_pl_eqt.png" width="100%">
    <p>(c) Imagen 3</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes/Histogramas/histograma_sy_dist.png" width="100%">
    <p>(d) Imagen 4</p>
  </div>

</div>


Las siguientes 3 figuras muestran una distribucion rara que se revisará mas a detalle. 


<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">

  <div style="text-align: center;">
    <img src="Imagenes/Histogramas/histograma_pl_orbeccen.png" width="100%">
    <p>(a) Imagen 1</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes/Histogramas/histograma_pl_orbper.png" width="100%">
    <p>(b) Imagen 2</p>
  </div>

  <div style="grid-column: span 2; text-align: center;">
    <img src="Imagenes/Histogramas/histograma_pl_rade.png" width="50%">
    <p>(c) Imagen 3</p>
  </div>


  </div>

</div>



<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">

  <div style="text-align: center;">
    <img src="Imagenes/Dispersion/dispersion_pl_orbper.png_general.png" width="100%">
    <p>(a) Imagen 1</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes/Dispersion/dispersion_pl_orbper.png" width="100%">
    <p>(b) Imagen 2</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes/Dispersion/dispersion_pl_rade.png_general.png" width="100%">
    <p>(c) Imagen 3</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes/Dispersion/dispersion_pl_rade.png" width="100%">
    <p>(d) Imagen 4</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes/Dispersion/dispersion_pl_orbeccen.png_general.png" width="100%">
    <p>(c) Imagen 3</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes/Dispersion/dispersion_pl_orbeccen.png" width="100%">
    <p>(d) Imagen 4</p>
  </div>

  

</div>

## Selección de parámetros
### IF y LOF
Para detectar las anomalías se decide trabajar con los algoritmos Isolation Forest (IF) y Local Outlier Factor (LOF).




<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">

  <div style="text-align: center;">
    <img src="Imagenes\SeleccionParametros\Anomalias_vs_Trees.png" width="100%">
    <p>(a) Imagen 1</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes\SeleccionParametros\Anomalias_vs_Vecinos.png" width="100%">
    <p>(b) Imagen 2</p>
  </div>



  </div>

</div>


### Autodecodificador

Se emplea autocodificador para detectar las anomalías. La arquitectura se esquematiza en la figura de la izquierda. Se emplearon funciones de activación tanh⁡  en las capas ocultas.
Se usa MSE como función de pérdida. El espacio latente lo podemos emplear para la representación en dos dimensiones de nuestros datos. 

* 80 % de los datos se emplea para entrenamiento y 20% para pruebas.
* 100 épocas y un tamaño de bache de 32.    

<div style="text-align: center;">
  <img src="Imagenes/SeleccionParametros/Autoencoder.png" width="50%">
  <p>Arquitectura empleada </p>
</div>


## Resultados

### Autodecodificador

![Imagen](Imagenes/SeleccionParametros/AutocodificadorEntrenamiento.png)

![alt text](Imagenes/SeleccionParametros/MSE_Dispersionpng.png)


Se representan los datos mediante el espacio latente del autocodificador y también con PCA. 
Se anotan algunas de las anomalías con MSE más alto. 
Las estructuras de PCA y el espacio latente parecen tener semejanza.
EPIC 248847494 b aparece nuevamente. 

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">

  <div style="text-align: center;">
    <img src="Imagenes/ReduccionDimensional/Autoencoder_Bottleneck.png" width="100%">
    <p>(a) Imagen 1</p>
  </div>

  <div style="text-align: center;">
    <img src="Imagenes/ReduccionDimensional/PCA_Test_Autoencoder.png" width="100%">
    <p>(b) Imagen 2</p>
  </div>



  </div>

</div>

## Conclusiones

