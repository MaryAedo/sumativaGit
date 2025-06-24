# Programa para gestionar alumnos

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
        opcion = int(input("Selecciona una opción (1-4): "))

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

    except:
        print("Debe ingresar un NÚMERO válido para el menú.")