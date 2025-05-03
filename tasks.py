from Smtp import send_email
import os

# Lista de tareas
tasks = []

def add_task(task):
    """Agrega una tarea a la lista."""
    tasks.append(task)
    os.system("cls")
    print(f"✅ Tarea agregada: {task}")

def show_tasks():
    """Muestra todas las tareas pendientes."""
    if tasks:
        os.system("cls")
        print("📌 Lista de tareas:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("📭 No hay tareas pendientes.")

def complete_task(user_email):
    """Permite seleccionar una tarea por número y enviará un correo al completarla."""
    if not tasks:
        print("📭 No hay tareas pendientes.")
        return
    
    show_tasks()
    
    try:
        task_number = int(input("\nIngrese el número de la tarea a completar: ")) - 1
        if 0 <= task_number < len(tasks):
            task = tasks.pop(task_number)
            print(f"✅ Tarea completada: {task}")
            send_email(user_email, task)  # Enviar correo de notificación
        else:
            print("❌ Número de tarea inválido.")
    except ValueError:
        print("❌ Debes ingresar un número válido.")