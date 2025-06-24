# Crear un programa python con un menu, con tres opciones. 1 Agregar alumnos a una lista de alumnos, 
# 2. mostrar todos los alumnos, 3 cerrar. El programa debe pedir el nombre del alumno.
# -Validar que los nombres ingresados sean solo letras
# -Agregar al menu la funcion de eliminar un alumno, solicitando su nombre

# lista inicial de alumnos
alumnos = []

# menú inicial
def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Eliminar alumno")
    print("4. Cerrar")

while True:
    # mostramos función
    mostrar_menu()
    try:
        # verificamos la opción
        opcion = int(input("Selecciona una opción (1-4): "))

        # "verificamos" que sea número positivo
        if opcion <= 0:
            print("Debe ingresar un número entero positivo.")
            continue  # vuelve al inicio del while para pedir otra entrada
        
        # si marcan opción 1, ingresa el nombre
        if opcion == 1:
            while True:
                nombre = input("Ingresa el nombre del alumno: ")
                # verificación de nombre con letras
                if nombre.replace(" ", "").isalpha():
                    alumnos.append(nombre)
                    print(f"Alumno '{nombre}' agregado con éxito.")
                    break
                # si el nombre tenía números: 
                else:
                    print("El nombre solo debe contener letras. Intenta nuevamente.")
        # si opción es 2, de mostrar alumnos
        elif opcion == 2:
            if alumnos:
                print("\nLista de alumnos:")
                numero = 1
                for alumno in alumnos:
                    print(f"{numero}. {alumno}")
                    numero += 1
            # si no hay alumnos registrados:
            else:
                print("No hay alumnos registrados.")

        # si marcan 3 para eliminar
        elif opcion == 3:
            if alumnos:
                # pedimos nombre
                nombre = input("Ingresa el nombre del alumno a eliminar: ")
                # comprobamos si existe el nombre en la lista
                if nombre in alumnos:
                    # si está, se elimina
                    alumnos.remove(nombre)
                    print(f"Alumno '{nombre}' eliminado exitosamente.")
                # sino, avisamos
                else:
                    print(f"El alumno '{nombre}' no se encuentra en la lista.")
            # si no hay nadie...
            else:
                print("No hay alumnos para eliminar.")

        # si elegimos 4 pa salir
        elif opcion == 4:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        # si está la opción fuera del rango 1-4
        else:
            print("Opción inválida. Por favor selecciona del 1 al 4.")
    # si ingresamos una letra, nos lanza este mensaje
    except:
        print("Debe ingresar un NÚMERO válido para el menú.")