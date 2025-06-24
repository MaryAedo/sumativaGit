# Caso 1:

alumnos = []

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Cerrar")

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

    if opcion == "1":
        nombre = input("Ingresa el nombre del alumno: ")
        alumnos.append(nombre)
        print(f"Alumno '{nombre}' agregado con éxito.")
    elif opcion == "2":
        if alumnos:
            print("\nLista de alumnos:")
            for i, alumno in enumerate(alumnos, 1):
                print(f"{i}. {alumno}")
        else:
            print("No hay alumnos registrados.")
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor selecciona 1, 2 o 3.")
    