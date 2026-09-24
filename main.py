from gestor_tareas import GestorTareas


def mostrar_menu():
    """Muestra las opciones disponibles al usuario."""

    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Buscar tarea")
    print("5. Salir")


def leer_opcion():
    """Valida que el usuario seleccione una opción correcta."""

    while True:
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion in {"1", "2", "3", "4", "5"}:
            return opcion

        print("Opción inválida. Ingrese un número del 1 al 5.")


def main():
    gestor = GestorTareas()

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == "1":

            titulo = input(
                "Ingrese el título de la tarea: "
            ).strip()

            if gestor.agregar_tarea(titulo):
                print("Tarea agregada correctamente.")
            else:
                print(
                    "No se pudo agregar la tarea. "
                    "El título no puede estar vacío."
                )

        elif opcion == "2":

            tareas = gestor.listar_tareas()

            if not tareas:
                print("No hay tareas registradas.")

            else:
                print("\n--- LISTA DE TAREAS ---")

                for indice, tarea in enumerate(
                    tareas,
                    start=1
                ):

                    estado = (
                        "✓"
                        if tarea["completada"]
                        else " "
                    )

                    print(
                        f"{indice}. "
                        f"[{estado}] "
                        f"{tarea['titulo']}"
                    )

        elif opcion == "3":

            tareas = gestor.listar_tareas()

            if not tareas:
                print(
                    "No hay tareas para completar."
                )
                continue

            try:

                numero = int(
                    input(
                        "Número de la tarea a completar: "
                    )
                )

                if gestor.completar_tarea(numero - 1):

                    print(
                        "Tarea marcada como completada."
                    )

                else:

                    print(
                        "Número de tarea inválido."
                    )

            except ValueError:

                print(
                    "Debe ingresar un número válido."
                )

        elif opcion == "4":

            texto = input(
                "Texto a buscar: "
            ).strip()

            resultados = gestor.buscar_tareas(texto)

            if not resultados:

                print(
                    "No se encontraron coincidencias."
                )

            else:

                print("\n--- RESULTADOS ---")

                for tarea in resultados:

                    estado = (
                        "Completada"
                        if tarea["completada"]
                        else "Pendiente"
                    )

                    print(
                        f"- {tarea['titulo']} "
                        f"({estado})"
                    )

        elif opcion == "5":

            print("Programa finalizado.")
            break


if __name__ == "__main__":
    main()