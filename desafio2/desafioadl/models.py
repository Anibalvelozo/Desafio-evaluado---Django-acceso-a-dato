from django.db import models

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)
    tarea = models.ForeignKey(Tarea, related_name='subtareas', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
