import sqlite3

class Db:
    @staticmethod
    def conectar(name: str)->sqlite3.Connection:
        return sqlite3.connect(name, isolation_level=None)

    @staticmethod
    def cerrar(con: sqlite3.Connection):
        con.close()