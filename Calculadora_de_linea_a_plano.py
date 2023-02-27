import math
import mplstereonet
import matplotlib.pyplot as plt
import tkinter
from tkinter import messagebox

parent = tkinter.Tk()  # Create the object
parent.overrideredirect(1)  # Avoid it appearing and then disappearing quickly
parent.withdraw()  # Hide the window as we do not want to see this one
warn = messagebox.showinfo('Calculadora de línea a plano','¡Bienvenido! Pulsa aceptar para continuar, después, pulsa intro para iniciar la calculadora.'
                                                          '                                                     Una vez realizado el cálculo, cierra la ventana de Stereonet para comenzar de nuevo', parent=parent)

while input("Presiona intro para ejecutar el proceso, o escribe 'salir' para finalizar: ") != "salir":
    print("Martín García Martín 2023 ©")
    print("Bienvenido, esta calculadora te ayudará a encontar el plano que contiene a dos líneas"),
    print('Es importante que introduzcas primero la línea cuyo sentido de buzamiento es menor')

    def true_dip(apparent_dip1, apparent_dip1_direction, apparent_dip2, apparent_dip2_direction):
        #Para pasar de Strike y Dip a Buz y sentido de Buz
        dip1 = 90 - apparent_dip1
        dip2 = 90 - apparent_dip2

        # Para convertir los angulos en cordenadas cartesianas
        x1 = math.cos(math.radians(apparent_dip1_direction)) * math.sin(math.radians(dip1))
        y1 = math.sin(math.radians(apparent_dip1_direction)) * math.sin(math.radians(dip1))
        z1 = math.cos(math.radians(dip1))
        x2 = math.cos(math.radians(apparent_dip2_direction)) * math.sin(math.radians(dip2))
        y2 = math.sin(math.radians(apparent_dip2_direction)) * math.sin(math.radians(dip2))
        z2 = math.cos(math.radians(dip2))

        # Calcula el producto cruzado de los dos vectores para saca el vector normal del plano
        normal_x = y1*z2 - y2*z1
        normal_y = z1*x2 - z2*x1
        normal_z = x1*y2 - x2*y1

        # Calcular el producto escalar del vector normal y el vector vertical para obtener el coseno entre el plano y la horizontal
        cos_angle = normal_z / math.sqrt(normal_x**2 + normal_y**2 + normal_z**2)

        #Convertir el coseno a grados
        true_dip = 180 - math.degrees(math.acos(cos_angle))
        if true_dip>90:
            true_dip = 180 - true_dip
        print("El buzamiento del Plano es:", true_dip)
        return true_dip

    blinea1 = float(input("Introduce el buzamiento de la primera línea: "))
    dblinea1 = float(input("Introduce el sentido de buzamiento de la primera línea: "))
    blinea2 = float(input("Introduce el buzamiento de la segunda línea: "))
    dblinea2 = float(input("Introduce el sentido de Buzamiento de la segunda línea: "))

    if dblinea1 > dblinea2:
        apparent_dip1_direction = dblinea2
        apparent_dip1 = blinea2
        apparent_dip2_direction = dblinea1
        apparent_dip2 = blinea1
    else:
        apparent_dip1_direction = dblinea1
        apparent_dip1 = blinea1
        apparent_dip2_direction = dblinea2
        apparent_dip2 = blinea2

    def true_dip_direction(apparent_dip1, apparent_dip1_direction, apparent_dip2, apparent_dip2_direction):
        #Para pasar de Strike y Dip a Buz y sentido de Buz
        dip1 = 90 - apparent_dip1
        dip2 = 90 - apparent_dip2

        # Para convertir los angulos en cordenadas cartesianas
        x1 = math.cos(math.radians(apparent_dip1_direction)) * math.sin(math.radians(dip1))
        y1 = math.sin(math.radians(apparent_dip1_direction)) * math.sin(math.radians(dip1))
        z1 = math.cos(math.radians(dip1))
        x2 = math.cos(math.radians(apparent_dip2_direction)) * math.sin(math.radians(dip2))
        y2 = math.sin(math.radians(apparent_dip2_direction)) * math.sin(math.radians(dip2))
        z2 = math.cos(math.radians(dip2))

        # Calcula el producto cruzado de los dos vectores para saca el vector normal del plano
        normal_x = y1 * z2 - y2 * z1
        normal_y = z1 * x2 - z2 * x1
        normal_z = x1 * y2 - x2 * y1

        #Para calcular el plano que contiene a ambas lineas
        true_dip_direction = math.degrees(math.atan2(normal_y, normal_x))
        if true_dip_direction < 360 and apparent_dip1_direction<apparent_dip2_direction:
            true_dip_direction +=180
        print("El sentido de Buzamiento del Plano es:", true_dip_direction)
        return true_dip_direction


    true_dip = true_dip(apparent_dip1, apparent_dip1_direction, apparent_dip2, apparent_dip2_direction)
    true_dip_direction = true_dip_direction(apparent_dip1, apparent_dip1_direction, apparent_dip2, apparent_dip2_direction)

    #Para convertir los valores numéricos en cadenas de texto. Para salida numérica en la gráfica.
    tdstr = str(round(true_dip))
    if round(true_dip_direction) >= 100:
        tdpdstr = str(round(true_dip_direction))
    else:
        tdpdstr = "0" + str(round(true_dip_direction))

    #Variable resultado
    resultado = "Solución: " + tdstr + "/"+ tdpdstr + "º"

    # Ventana para fallo
    parent1 = tkinter.Tk()  # Create the object
    parent1.overrideredirect(1)  # Avoid it appearing and then disappearing quickly
    parent1.withdraw()  # Hide the window as we do not want to see this one

    #Crear Gráfico

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='stereonet')
    plt.title(resultado, fontsize=12, loc='center', )

    # Representar las lineas
    ax1.line(apparent_dip1, apparent_dip1_direction, linewidth=2)

    ax1.line(apparent_dip2,apparent_dip2_direction, linewidth=2)

    if true_dip_direction <0:
        warn1 = messagebox.showwarning('¡Error!',  'Has introducido la línea con mayor sentido de buzamiento antes que la segunda', parent=parent1)
    else:
        # Representar el plano obtenido en el Stereo
        ax1.plane(true_dip_direction - 90, true_dip, "b", linewidth=2)
        ax1.grid()
        ax1.text(0, -2, "Martín García Martín 2023 ©")
        plt.show()
