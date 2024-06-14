from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    result = []
    for tarea in tareas:
        subtareas = SubTarea.objects.filter(tarea=tarea)
        result.append((tarea, subtareas))
    return result

def crear_nueva_tarea(descripcion, estado):
    tarea = Tarea.objects.create(descripcion=descripcion, estado=estado)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion, estado):
    tarea = Tarea.objects.get(id=tarea_id)
    subtarea = SubTarea.objects.create(tarea=tarea, descripcion=descripcion, estado=estado)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    Tarea.objects.filter(id=tarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    SubTarea.objects.filter(id=subtarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(tareas_y_subtareas):
    for tarea, subtareas in tareas_y_subtareas:
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in subtareas:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")
