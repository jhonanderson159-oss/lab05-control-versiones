def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")


def main():
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            tarea = input("Ingrese una nueva tarea: ").strip()

            if tarea:
                tareas.append(tarea)
                print("Tarea agregada correctamente.")
            else:
                print("La tarea no puede estar vacía.")

        elif opcion == "2":
            if not tareas:
                print("No hay tareas registradas.")
            else:
                print("\n--- LISTA DE TAREAS ---")

                for numero, tarea in enumerate(tareas, start=1):
                    print(f"{numero}. {tarea}")

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()