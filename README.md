# Calc-Linea-Plano


Este programa calcula el plano contenido por dos líneas. Puede ser útil para calcular el buzamiento real de un plano a partir de sus buzamientos aparentes.

Para utilizarlo solo tienes que descargar el archivo .exe disponible en la pestaña de "releases" del repositorio: (https://github.com/MGMGXCV/Calc-Linea-Plano)

Cuando lo abras te pedirá que le des a intro para comenzar. Seguidamente te pedirá que introduzcas el buzamiento (o inmersión) de la primera línea, después te pedirá el sentido de buzamiento de la primera línea (Es importante que la primera línea sea la que menor ángulo de sentido de buzamiento tenga, ya que si se introduce primero la de mayor ángulo puede calcular un resultado incorrecto) 
Después te pedirá la segunda línea de la misma forma. 

Cuando hayas introducido la segunda línea se abrirá un gráfico (stereonet), en el que se mostrarán las dos líneas en forma de puntos y el plano que contiene a las dos líneas que has introducido.
 
Si todo ha ido bien la línea del plano calculado pasará por los dos puntos. En la parte de arriba de la estereográfica se mostrará la orientación del plano dada en Buzamiento/Sentido de Buzamiento. 

Para calcular otro plano nuevo cierra el gráfico (no la consola) y el proceso comenzará de nuevo.


Agradecimientos a las librerías mathplotlib y mplstereonet tkinter y pyinstaller. 

Creado por Martín García Martín 2023.


ENGLISH:

This program calculates the plane contained by two lines. It can be useful to calculate the real dip of a plane from its apparent dips.

To use it you only have to download the .exe file available in the releases tab of the repository (https://github.com/MGMGXCV/Calc-Linea-Plano).

When you open it, it will ask you to press enter to start. Next it will ask you to enter the dip (plunge) of the first line, then it will ask you for the dip direction (trend) of the first line (It is important that the first line is the one with the smallest dip direction angle, because if you enter the one with the largest angle first it may calculate an incorrect result). 
Then the program will ask you about the second line with the same format.  

When you have entered the second line, a graph (stereonet) will open, showing the two lines as points and the plane containing the two lines you have entered.
 
If everything went well, the line of the calculated plane will "pass" through the two points. At the top of the stereographic the orientation of the plane given in Dip/Dip Direction will be displayed. 

To calculate another new plane, close the plot (not the console) and the process will start again.


Thanks to the mathplotlib and mplstereonet tkinter pyinstaller libraries. 

Created by Martín García Martín 2023.
