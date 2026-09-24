class GestorTareas:
    """Administra una colección simple de tareas en memoria."""

    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, titulo):
        """Agrega una tarea nueva si el título es válido."""

        titulo = titulo.strip()

        if not titulo:
            return False

        self._tareas.append(
            {
                "titulo": titulo,
                "completada": False
            }
        )

        return True

    def listar_tareas(self):
        """Devuelve todas las tareas registradas."""

        return self._tareas

    def completar_tarea(self, indice):
        """Marca una tarea como completada."""

        if 0 <= indice < len(self._tareas):
            self._tareas[indice]["completada"] = True
            return True

        return False

    def buscar_tareas(self, texto):
        """Busca tareas que contengan el texto indicado."""

        texto = texto.strip().lower()

        if not texto:
            return []

        return [
            tarea
            for tarea in self._tareas
            if texto in tarea["titulo"].lower()
        ]