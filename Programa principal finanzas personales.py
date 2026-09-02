#Programa administrador de Finanzas Personales

#Funcion para mostrar gastos en una tabla
#Esta funcion toma el diccionario de gastos como argumento para hacer la tabla
def tabla_gastos(x):
    conceptlong = 0
    for palabra in x:
        if conceptlong < len(palabra):
            conceptlong = len(palabra)
            
    conceptvalue = 0
    for valor in x.values():
        if conceptvalue < len(str(valor)):
            conceptvalue = len(str(valor))

    print("\nEstos son tus gastos:\n")
    print("|-" + "-" * conceptlong + "-|" + "|-" + "-" * conceptvalue + "--|")
    for palabra, valor in x.items():
        #espacio = len(str(palabra))
        #espacio2 = len(str(valor))
        #print("", palabra, " " * abs(int(conceptlong) - int(espacio)), "=>", "$", valor)
        #print(f" {palabra} {" " * abs(int(conceptlong) - int(espacio))} => ${valor:.2f}")
        print(f" {palabra:<{conceptlong}}  => ${valor:.2f}")

    print("|---" + "-" * conceptlong + "-" * conceptvalue + "----|\n")


#Funcion para calcular los gastos en Necesidades Básicas
def necesidades():
    print("\nVamos a comenzar con tus gastos de Necesidades Básicas\n")
    print("Teclea \"fin\" para salir\n")
    basic = ""
    #global basicasdic
    basicasdic = {}
    while basic.lower() != "fin":
        #basic = input("Introduce concepto: ")
        while True:
            try:
                basic = input("Introduce concepto: ")
                if not basic.strip():
                    raise ValueError("El concepto no puede estar vacío")
                break
            except ValueError as e:
                print(f"Error: {e}")
                
        if basic.lower() == "fin":
            break
        
        while True:
            try:
                monto = float(input("Introduce monto: "))

                break
            except ValueError:
                print("Error: Debes ingresar un número entero o decimal")


        basicasdic[basic] = monto
        total_gastos = sum(basicasdic.values())

    restante_bas = sueldo -  total_gastos
    print(basicasdic)
    return restante_bas, basicasdic
    
    #return(sueldo - total_gastos)

#Funcion para calcular los gastos en Estilo de vida/gustos
def estilo():
    print("\nVamos a comenzar con tus gastos de Estilo de vida/gustos\n")
    print("Teclea \"fin\" para salir\n")
    estilo = ""
    #global estilodic
    estilodic = {}
    while estilo.lower() != "fin":
        #estilo = input("Introduce concepto: ")
        while True:
            try:
                estilo = input("Introduce concepto: ")
                if not estilo.strip():
                    raise ValueError("El concepto no puede estar vacío")
                break
            except ValueError as e:
                print(f"Error: {e}")

        if estilo.lower() == "fin":
            break
        
        while True:
            try:
                monto = float(input("Introduce monto: "))

                break
            except ValueError:
                print("Error: Debes ingresar un número entero o decimal")


        estilodic[estilo] = monto
        total_gastos = sum(estilodic.values())
        restante_est = gasto_necesidades - total_gastos

    return restante_est, estilodic
    #return(gasto_necesidades - total_gastos)


#Funcion para el ahorro

def ahorro(x):

    #sueldo = 1000
    ahorro20 = sueldo *.2
    #print(ahorro20)
    #print(remanente_final)
    if ahorro20 > x:
        print(f"\nLamentablemente no puedes ahorrar el 20%, que es ${ahorro20:.2f}")
        print("\nDeberías: Conseguir mas ingresos o reducir tus gustos")
    else:
        print("\nTu si puedes ahorrar eso, ¡felicidades!")

    global ahorrare
    ahorrare = float(input(f"\nDame una cantidad igual o menor a ${remanente_final:.2f}, que es lo que te sobra: $"))
    while ahorrare > remanente_final or ahorrare < 1:
        ahorrare = float(input(f"\nLa cantidad debe ser igual o menor a ${remanente_final:.2f} y no debe ser menor que 1: $"))

    else:
            print(f"\nVamos a ahorrar la módica cantidad de ${ahorrare:.2f}")
     




#Codigo
#Introduce sueldo
print("Bienvenido... ")
sueldo = float()
while True:
            try:
                sueldo = float(input("Introduce tu sueldo: $"))

                break
            except ValueError:
                print("Error: Debes ingresar un número entero o decimal")


#Invoca función de Necesidades básicas
gasto_necesidades, basicasdic = necesidades()
print(f"\nA tu sueldo, restándole estos gastos te queda: ${gasto_necesidades:.2f}")
tabla_gastos(basicasdic)

#Invoca función de Estilo de vida
remanente_final, restante_dic = estilo()
print(f"Esto te queda de tu sueldo sin estos gastos: ${remanente_final:.2f}")
tabla_gastos(restante_dic)

print("De forma mínima y obligada, debes ahorrar el 20% de tu sueldo para:" + "\n"*2 + "Construir un fondo de emergencia\nPagar deudas\nO invertir para tu futuro\n")

ahorro20 = sueldo * .2
print(f"Esto es lo que debes ahorrar de tu sueldo ${ahorro20:.2f}" )

#Invoca funcion de ahorro
ahorro(remanente_final)



#detalles
#hecho#agregarle try except a monto


#manejo de errores
#bucle para que si introduces un monto mayor al restante de tu sueldo no te deje
#que te pregunte si quieres modificar algun monto

#codigo que puedo hacer
#hecho#continuar con el ahorro, que te diga cuanto puedes ahorrar y si es el 20 o mas
#hecho#ademas si quieres ahorrar eso u otra cantidad

#codigo complejo
#agregarle flexibilidad, salario pagado por semana, quincena
#agregarle persistencia de datos
#como hacer para que se muestre cuando sacas dinero para hacer un pago, como yo que lo tengo ahorrado y a veces acumulo mas dinero que loque ncesito
#hacer una base de datos donde tu puedas ingresar usuario y contraseña y recuerde lo que le has dicho
#darle opcion para que puedas agregar no sueldo pero algun ingreso extra que te llego fuera de tiempo esperado
#hacer que se pueda exportar a excel o a una imagen donde se vean tus gastos
 










