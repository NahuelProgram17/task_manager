import json

ARCHIVO = "tasks.json"

# --- Funciones de carga y guardado ---
def cargar_tareas():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open(ARCHIVO, "w") as f:
        json.dump(tareas, f, indent=4)

# --- Funciones de manejo de tareas ---
def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas disponibles 📝")
        return
    print("\nTareas:")
    for tarea in tareas:
        estado = "✅" if tarea["completada"] else "❌"
        print(f'{tarea["id"]}. {tarea["descripcion"]} [{estado}]')

def agregar_tarea(tareas):
    descripcion = input("Ingrese la descripción de la tarea: ")
    id_nuevo = max([t["id"] for t in tareas], default=0) + 1
    tareas.append({"id": id_nuevo, "descripcion": descripcion, "completada": False})
    print(f'Tarea "{descripcion}" agregada 🆕')

def completar_tarea(tareas):
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
        for tarea in tareas:
            if tarea["id"] == id_tarea:
                tarea["completada"] = True
                print(f'Tarea "{tarea["descripcion"]}" completada ✅')
                return
        print("Tarea no encontrada ❌")
    except ValueError:
        print("Debe ingresar un número válido.")

def borrar_completadas(tareas):
    tareas_sin_completadas = [t for t in tareas if not t["completada"]]
    print("Tareas completadas borradas 🗑️")
    return tareas_sin_completadas

# --- Menú principal ---
def menu():
    tareas = cargar_tareas()
    while True:
        print("\n--- Administrador de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Borrar tareas completadas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            tareas = borrar_completadas(tareas)
        elif opcion == "5":
            guardar_tareas(tareas)
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción inválida ❌")

        guardar_tareas(tareas)

if __name__ == "__main__":
    menu()
