# Crear un programa python con un menu, con tres opciones. 1 Agregar alumnos a una lista de alumnos, 
# 2. mostrar todos los alumnos, 3 cerrar. El programa debe pedir el nombre del alumno.
# -Validar que los nombres ingresados sean solo letras
# -Agregar al menu la funcion de eliminar un alumno, solicitando su nombre

alumnos = []

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Eliminar alumno")
    print("4. Cerrar")

while True:
    mostrar_menu()
    try:
        # verificamos la opción
        opcion = input("Selecciona una opción (1-3): ")
        if opcion <= 0:
            print("Debe ingresar un número entero positivo.")
            # damos la pasá al resto del programa
            continue
        # cortamos la evaluación del try/if
        break
    # si ingresamos una letra, nos lanza este mensaje
    except:
        print("Debe ingresar un NÚMERO para el menú.")

    if opcion == 1:
        while True:
            nombre = input("Ingresa el nombre del alumno: ")
            if nombre.replace(" ", "").isalpha():
                alumnos.append(nombre)
                print(f"Alumno '{nombre}' agregado con éxito.")
                break
            else:
                print("El nombre solo debe contener letras. Intenta nuevamente.")

    elif opcion == 2:
        if alumnos:
            print("\nLista de alumnos:")
            numero = 1
            for alumno in alumnos:
                print(f"{numero}. {alumno}")
                numero += 1
        else:
            print("No hay alumnos registrados.")

    elif opcion == 3:
        if alumnos:
            nombre = input("Ingresa el nombre del alumno a eliminar: ")
            if nombre in alumnos:
                alumnos.remove(nombre)
                print(f"Alumno '{nombre}' eliminado exitosamente.")
            else:
                print(f"El alumno '{nombre}' no se encuentra en la lista.")
        else:
            print("No hay alumnos para eliminar.")

    elif opcion == 4:
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor selecciona del 1 al 4.")
    