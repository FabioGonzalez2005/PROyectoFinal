from db import Db
from clase import Clase

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS clases (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	clase TEXT NOT NULL
)
'''

SQLDDLSELECT = '''
    SELECT * FROM clases
'''

SQLDDLINSERT = '''INSERT INTO clases (clase) VALUES '''
                #Hay que concatenar  ('clase')

SQLDDLUPDATEPART1 = '''UPDATE clases SET clase = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM clases WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM clases WHERE clase LIKE '''
                #Hay que concatenar



class ColeccionClases:
    DBNAME = 'tabla.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, clase):
        if self.buscar(clase) == 0:
            elstr = "('" + str(clase) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldClase:str, newClase:str):
        id = self.buscar(oldClase)
        if id != 0 and self.buscar(newClase) == 0:
            elstr = SQLDDLUPDATEPART1 + newClase 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, clase):
        id = self.buscar(clase) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, clase:Clase) -> int:
        resultado = 0
        elstr = '"' + str(clase) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado