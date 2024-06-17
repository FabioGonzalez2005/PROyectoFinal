from db import Db
from nota import Nota

SQLMDLCREATE = '''
    CREATE TABLE IF NOT EXISTS notas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	nota TEXT NOT NULL
)
'''

SQLDDLSELECT = '''
    SELECT * FROM notas
'''

SQLDDLINSERT = '''INSERT INTO notas (nota) VALUES '''
                #Hay que concatenar  ('nota')

SQLDDLUPDATEPART1 = '''UPDATE notas SET nota = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''

SQLDDLDELETE = '''DELETE FROM notas WHERE id = '''

SQLDDLSELECT1 = '''SELECT id FROM notas WHERE nota LIKE '''
                #Hay que concatenar



class ColeccionNotas:
    DBNAME = 'notas.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)

        self.con.execute(SQLMDLCREATE)

    def leer(self)->str:
        return self.con.execute(SQLDDLSELECT).fetchall()
    
    def insertar(self, nota):
        if self.buscar(nota) == 0:
            elstr = "('" + str(nota) + "')"
            self.con.execute(SQLDDLINSERT + elstr)

    def actualizar(self, oldNota:str, newNota:str):
        id = self.buscar(oldNota)
        if id != 0 and self.buscar(newNota) == 0:
            elstr = SQLDDLUPDATEPART1 + newNota 
            elstr += SQLDDLUPDATEPART2 + str(id)
            self.con.execute(elstr)

    def borrar(self, nota):
        id = self.buscar(nota) 
        if id != 0:
            self.con.execute(SQLDDLDELETE + str(id))

    def buscar(self, nota:nota) -> int:
        resultado = 0
        elstr = '"' + str(nota) + '"'
        res = self.con.execute(SQLDDLSELECT1 + elstr)
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]

        return resultado