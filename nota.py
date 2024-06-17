class Nota:
    def __init__(self, descripcion:str) -> None:
        self.descripcion = descripcion

    def read(self):
        return self.id + ", " + self.descripcion

    def __str__(self) -> str:
        return self.descripcion

    def update(self, idNuevo:int, descripcionNuevo:str):
        self.id = idNuevo
        self.descripcion = descripcionNuevo

    def delete(self):
        self.id = None
        self.descripcion = None