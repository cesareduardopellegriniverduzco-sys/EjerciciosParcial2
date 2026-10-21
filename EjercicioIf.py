nombre = ""
edad = 0
nacionalidad = ""
#//////////////////////////////////////////////#
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
nacionalidad = input("Ingresa tu nacionalidad: ")
#//////////////////////////////////////////////#
if edad >= 18:# el if va seguido de la condicion y 2 puntos
    print("Eres mayor de edad.")
else:# el else va seguido de 2 puntos para decir que se hace si no se cumple la condicion del if
    print("Esta persona no es mayor de edad.")
#//////////////////////////////////////////////#
if nacionalidad == "Mexicana":
    print("Esta persona es de nacionalidad mexicana.")
else:
    print("Esta persona no es de nacionalidad mexicana.")