import math
import mplstereonet
import matplotlib.pyplot as plt
while input("Presiona intro para ejecutar el proceso, o escribe 'salir' para finalizar: ") != "salir":
    print("Bienvenido, esta calculadora te ayudará a encontar el plano que contiene a dos líneas"),
    print("Es importante que introduzcas primero la línea cuyo sentido de buzamiento es menor")
    print("Martín García Martín 2023 ©")
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

    apparent_dip1 = float(input("Introduce el buzamiento de la primera línea: "))
    apparent_dip1_direction = float(input("Introduce el sentido de buzamiento de la primera línea: "))
    apparent_dip2 = float(input("Introduce el buzamiento de la segunda línea: "))
    apparent_dip2_direction = float(input("Introduce el sentido de Buzamiento de la segunda línea: "))


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

    #Crear Gráfico

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='stereonet')
    plt.title(resultado, fontsize=12, loc='center', )

    # Representar las lineas
    ax1.line(apparent_dip1, apparent_dip1_direction, linewidth=2)

    ax1.line(apparent_dip2,apparent_dip2_direction, linewidth=2)

    # Representar el plano obtenido en el Stereo
    ax1.plane(true_dip_direction -90 , true_dip, "b" , linewidth=2)
    ax1.grid()
    ax1.text(0,-2,"Martín García Martín 2023 ©")
    plt.show()

