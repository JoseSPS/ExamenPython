from datetime import date

#Funcion calcula inmuebles por zona y presupuesto
def calculaZona():

    inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

    #Input que recibira como parametro el presupusto
    presupuesto = "{0:.2f}".format(int(input("Ingresa presupuesto: ")))

    #Arreglo para obtener inmuebles disponibles de acuerdo a presupuesto
    inmueblesDisponiblesPresupuesto = []

    #Obtener año actual
    today = date.today()
    anio = today.year

    precio = 0

    for inmueble in inmuebles:
        if inmueble['zona'] == 'A':
            precio = "{0:.2f}".format(((inmueble['metros'] * 1000) + (inmueble['habitaciones'] * 5000) + (inmueble['garaje'] * 15000)) * (1 - (anio-inmueble['año'])/100))
            if precio <= presupuesto:
                inmueblesDisponiblesPresupuesto.append(inmueble)


        elif inmueble['zona'] == 'B':
            precio = "{0:.2f}".format(((inmueble['metros']) * 1000 + (inmueble['habitaciones'] * 5000) + (inmueble['garaje'] * 15000)) * (1 - (anio-inmueble['año'])/100) * 1.5)

            if precio <= presupuesto:
                inmueblesDisponiblesPresupuesto.append(inmueble)

    if len(inmueblesDisponiblesPresupuesto) == 0:
        print("No hay inmuebles disponibles por " + str(presupuesto))
    else:
        print("*****Inmuebles disponibles***********")
        print(inmueblesDisponiblesPresupuesto)


calculaZona()
