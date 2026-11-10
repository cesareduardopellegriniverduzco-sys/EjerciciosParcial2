name = ""
cantidad = ""
precio = ""
caducidad = ""
opción = 0

while True:
    print("Bienvenido al sistema de registro de productos")
print("------------Menú principal------------")
print("1. Registrar producto")
print("2. ver información del producto")
print("3. borrar información del producto")
print("4. modificar información del producto")
print("5. salir")
print("------------------------")
opcion = int(input("Ingrese una opción: "))

match opcion:

    case 1:
        name.append = input("Ingrese el nombre del producto: ")
        cantidad.append = input("Ingrese la cantidad del producto: ")
        precio.append = input("Ingrese el precio del producto: ")
        caducidad.append = input("Ingrese la fecha de caducidad del producto: ")
        print("Usuario registrado exitosamente, con el ID: " + str(le))
    case 2:
        print("Nombre:", name, "Cantidad:", cantidad, "Precio:", precio, "Fecha de caducidad:", caducidad)
    case 3:
        name = ""
        cantidad = ""
        precio = ""
        caducidad = ""
    case 4:
        name = input("Ingrese el nombre del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        precio = input("Ingrese el precio del producto: ")
        caducidad = input("Ingrese la fecha de caducidad del producto: ")
    case 5:
        print("¡Hasta luego!")
        break
    case _:
        print("Opción no válida")   