class Alumno:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre

    def read(self):
        return self.id + ", " + self.nombre

    def __str__(self) -> str:
        return self.nombre

    def update(self, idNuevo:int, nombreNuevo:str):
        self.id = idNuevo
        self.nombre = nombreNuevo

    def delete(self):
        self.id = None
        self.nombre = None