from coleccionAlumnos import ColeccionAlumnos
from alumno import Alumno

cc = ColeccionAlumnos()
#print(cc.leer())
#cc.buscar(Cita('La vida es bella'))

#print(cc.buscar(Alumno('La vida es bella')))
print(cc.insertar(Alumno('Manolo')))
#cc.borrar(Cita('Aguanta ahí'))
#cc.actualizar("Quedan 2 semanas de clase", "Hola qué tal!")
print(cc.leer())