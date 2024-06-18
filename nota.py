class Nota:
    def __init__(self, nota:str) -> None:
        self.nota = nota

    def read(self):
        return self.id + ", " + self.nota

    def __str__(self) -> str:
        return self.nota

    def update(self, idNuevo:int, notaNueva:str):
        self.id = idNuevo
        self.nota = notaNueva

    def delete(self):
        self.id = None
        self.nota = None