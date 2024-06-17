from db import Db
from alumno import Alumno

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS alumnos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	alumno TEXT NOT NULL
)
'''

SQLDDLSELECT = '''
    SELECT * FROM alumnos
'''

SQLDDLINSERT = '''INSERT INTO alumnos (alumno) VALUES '''
                #Hay que concatenar  ('alumno')

SQLDDLUPDATEPART1 = '''UPDATE alumnos SET alumno = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM alumnos WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM alumnos WHERE alumno LIKE '''
                #Hay que concatenar



class ColeccionAlumnos:
    DBNAME = 'alumnos.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, alumno):
        if self.buscar(alumno) == 0:
            elstr = "('" + str(alumno) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldAlumno:str, newAlumno:str):
        id = self.buscar(oldAlumno)
        if id != 0 and self.buscar(newAlumno) == 0:
            elstr = SQLDDLUPDATEPART1 + newAlumno 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, alumno):
        id = self.buscar(alumno) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, alumno:alumno) -> int:
        resultado = 0
        elstr = '"' + str(alumno) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado