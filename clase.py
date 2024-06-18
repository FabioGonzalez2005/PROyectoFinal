class Nota:
    def __init__(self, clase:str) -> None:
        self.clase = clase

    def read(self):
        return self.id + ", " + self.clase

    def __str__(self) -> str:
        return self.clase

    def update(self, idNuevo:int, claseNueva:str):
        self.id = idNuevo
        self.clase = claseNueva

    def delete(self):
        self.id = None
        self.clase = None