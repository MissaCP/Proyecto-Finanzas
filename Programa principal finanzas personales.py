#Programa administrador de Finanzas Personales

#Funcion para mostrar gastos en una tabla
#Esta funcion toma el diccionario de gastos como argumento para hacer la tabla-------------
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





#Funcion generadora de diccionario--------------------------------------------------------

def diccionario_gastos():
    print("\nVamos a comenzar, me dices tus gastos\n")
    print("Teclea \"fin\" para salir\n")
    clave = ""
    diccionario = {}
    while clave.lower() != "fin":
        while True:
            try:
                clave = input("Introduce concepto: ")
                if not clave.strip():
                    raise ValueError("El concepto no puede estar vacío")
                break
            except ValueError as e:
                print(f"Error: {e}")
        if clave.lower() in diccionario:
            print(f"El concepto '{clave}' ya está en tus gastos, pon otro nombre")
            continue            
        if clave.lower() == "fin":
            break
        
        while True:
            try:
                monto = float(input("Introduce monto: "))
                if monto <= 0:
                    raise ValueError

                break
            
            except ValueError:
                print("Error: Debes ingresar un número entero o decimal y mayor a 1")

        diccionario[clave.lower()] = monto
       
    return diccionario

    
#Funcion para el ahorro------------------------------------------------------------------------

def ahorro(x):

    ahorro_20 = sueldo *.2
    if ahorro_20 > x:
        print(f"\nLamentablemente no puedes ahorrar el 20%, que es ${ahorro_20:.2f}")
        print("\nDeberías: Conseguir mas ingresos o reducir tus gustos")
    else:
        print("\nTu si puedes ahorrar eso, ¡felicidades!")

    ahorrare = float(input(f"\nDame una cantidad igual o menor a ${x:.2f}, que es lo que te sobra: $"))
    while ahorrare > x or ahorrare < 1:
        ahorrare = float(input(f"\nLa cantidad debe ser igual o menor a ${x:.2f} y no debe ser menor que 1: $"))

    else:
            print(f"\nVamos a ahorrar la módica cantidad de ${ahorrare:.2f}")

    return ahorrare     

#Funcion para editar o eliminar gastos--------------------------------------------------------
def editar(x):
    print("Tus gastos son correctos o quieres eliminar/editar algun concepto?\n")
    
    while True:
            print("1. Continuar \n2. Editar/Agregar \n3. Eliminar\n")
            try:
                opciones1 = int(input("Introduce opción: "))
                if opciones1 not in [1, 2, 3]:
                    raise ValueError
                
            
            except ValueError:
                print("\nIntroduce un número de opción válido: ")
                continue

            if opciones1 == 1:
                print("\nGenial, vamos allá!\n")
                break

             
            elif opciones1 == 2:
                while True:
                    try:
                        concepto = str(input("Introduce concepto existente o nuevo: "))
                        if not concepto.strip():
                            raise ValueError("El concepto no puede estar vacío")
                        break
                    except ValueError as e:
                        print(f"Error: {e}")
                
                while True:
                    try:
                        monto = float(input("Introduce monto: "))
                        if monto <= 0:
                            raise ValueError
                        
                        break
                    except ValueError:
                        print("Error: Debes ingresar un número entero o decimal y mayor a 1")
                
                x[concepto] = monto
                print("exito")
                
            elif opciones1 == 3:
                concepto = input("Dame el nombre del concepto a eliminar: ")
                if concepto in x:
                    del x[concepto]
                    print(f"\nEl concepto '{concepto}' ha sido eliminado\n")
                else:
                    print("\nEse concepto no existe en tus gastos\n")

                    
            tabla_gastos(x)
            continue


#Funcion para sacar el porcentaje------------------------------------------------------
def porcentaje(x):
    porciento = int(x * 100 / sueldo)
    
    return porciento
                           
            
#----------------------------------------------------------------------------------#

#Codigo
#Introduce sueldo
print("Bienvenido... ")
sueldo = float()

while True:
        try:
            sueldo = float(input("Introduce tu sueldo: $"))
            if sueldo < 1:
                    raise ValueError
            break
        
        except ValueError:
            print("Error: Debes ingresar un número entero o decimal, y mayor a 1")
#Invoca funciones, genera diccionario---------
nb = "NECESITADES BASICAS"
print(f"\n{nb}")
dc_gastos = diccionario_gastos()

#Muestra en forma de tabla
tabla_gastos(dc_gastos)

#Edita diccionario
editar(dc_gastos)

#Muestra suma de valores de diccionario
suma_gastos = sum(dc_gastos.values())
print(f"Tus gastos de {nb} son de ${suma_gastos:.2f}")

#Invoca funciones, genera diccionario---------
ev = "GUSTOS / ESTILO DE VIDA"
print(f"\n{ev}")
dc_estilo = diccionario_gastos()

#Muestra en forma de tabla
tabla_gastos(dc_estilo)

#Edita diccionario
editar(dc_estilo)

#Muestra suma de valores de diccionario
suma_estilo = sum(dc_estilo.values())
print(f"Tus gastos de {ev} son de ${suma_estilo:.2f}")

#Cuanto queda libre
remanente = sueldo - suma_gastos - suma_estilo
ahorro_v = ahorro(remanente)

#Imprime porcentajes
print("Así se ven tus finanzas")
gastos_porcentaje = porcentaje(suma_gastos)
print(f"Tus Necesidades Básicas: {gastos_porcentaje}%")

estilo_porcentaje = porcentaje(suma_estilo)
print(f"Tus Gustos / Estilo de vida: {estilo_porcentaje}%")

ahorro_porcentaje = porcentaje(ahorro_v)
print(f"Tu ahorro: {ahorro_porcentaje}%")

#Guardar datos en un diccionario----------------------------
perfil_financiero = {"suedo": sueldo, "necesidades": dc_gastos, "estilo": dc_estilo}


###Invoca función de Necesidades básicas------------------------------
##gasto_necesidades, basicasdic = necesidades()
##print(f"\nA tu sueldo, restándole estos gastos te queda: ${gasto_necesidades:.2f}")
##tabla_gastos(basicasdic)
##
###Invocar funcion de preguntar si continuar o editar-----------------
##editar(basicasdic)
##
##
###Invoca función de Estilo de vida------------------------------------
##remanente_final, restante_dic = estilo()
##print(f"Esto te queda de tu sueldo sin estos gastos: ${remanente_final:.2f}")
##tabla_gastos(restante_dic)
##
###Invocar funcion de preguntar si continuar o editar-------------------
##editar(restante_dic)
##
##print("De forma mínima y obligada, debes ahorrar el 20% de tu sueldo para:" + "\n"*2 + "Construir un fondo de emergencia\nPagar deudas\nO invertir para tu futuro\n")
##
##ahorro20 = sueldo * .2
##print(f"Esto es lo que debes ahorrar de tu sueldo ${ahorro20:.2f}" )
##
###Invoca funcion de ahorro
##ahorro(remanente_final)



#detalles
#HECHO agregarle try except a monto


#manejo de errores
#bucle para que si introduces un monto mayor al restante de tu sueldo no te deje
#HECHO que te pregunte si quieres modificar algun monto

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
 










