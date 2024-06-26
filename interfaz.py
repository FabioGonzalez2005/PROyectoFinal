from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Footer, DataTable, Input
from textual.binding import Binding
from textual.screen import Screen
from coleccionAlumnos import ColeccionAlumnos
from coleccionNotas import ColeccionNotas
from coleccionClases import ColeccionClases
from alumno import Alumno
from nota import Nota
from clase import Clase

class MainMenu(Screen):
    CSS = """
    #menu {
        align: center middle;
        height: 100%;
    }
    """

    BINDINGS = [
        Binding(
            key="q",
            action="quit",
            description="Salir"
        ),
    ]

    def compose(self) -> ComposeResult:
        yield Container(
            Button("Alumno", id="alumno"),
            Button("Nota", id="nota"),
            Button("Clase", id="clase"),
            id="menu",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "alumno":
            self.app.push_screen(AlumnoScreen())
        elif button_id == "nota":
            self.app.push_screen(NotaScreen())
        elif button_id == "clase":
            self.app.push_screen(ClaseScreen())

class NuevoAlumnoScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre")

        yield Container(
            Button("Añadir", id="anadirAlumnoBoton"),
            Button("Volver", id="back"),
        )
        yield Footer()


    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.switch_to_alumnos()
        elif button_id == "anadirAlumnoBoton":
            self.app.ca.insertar(Alumno(self.query_one(Input).value))
            self.app.switch_to_alumnos()

class BorrarAlumnoScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre")

        yield Container(
            Button("Borrar", id="borrarAlumnoBoton"),
            Button("Volver", id="back"),
        )
        yield Footer()


    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.switch_to_alumnos()
        elif button_id == "borrarAlumnoBoton":
            self.app.ca.borrar(Alumno(self.query_one(Input).value))
            self.app.switch_to_alumnos()

class AlumnoScreen(Screen):
    BINDINGS = [
        Binding(
            key="q",
            action="quit",
            description="Salir"
        ),
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()
        
        yield Container(
            Button("Nuevo", id="nuevoAlumno"),
            Button("Borrar", id="borrarAlumno"),
            Button("Volver", id="back"),
        )
        yield Footer()
    
    def _on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type =  "row"
        table.zebra_stripes = True
        alumnos = [("ID", "Nombre")]
        alumnos += ColeccionAlumnos().leer()
        table.add_columns(*alumnos[0])
        table.add_rows(alumnos[1:])


    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.switch_to_main()
        elif button_id == "nuevoAlumno":
            self.app.pop_screen()
            self.app.push_screen(NuevoAlumnoScreen())
        elif button_id == "editarAlumno":
            self.app.pop_screen()
            self.app.push_screen()
        elif button_id == "borrarAlumno":
            self.app.pop_screen()
            self.app.push_screen(BorrarAlumnoScreen())

class NuevaNotaScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nota")

        yield Container(
            Button("Añadir", id="anadirNotaBoton"),
            Button("Volver", id="back"),
        )
        yield Footer()


    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.switch_to_notas()
        elif button_id == "anadirNotaBoton":
            self.app.cn.insertar(Nota(self.query_one(Input).value))
            self.app.switch_to_notas()

class BorrarNotaScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre")

        yield Container(
            Button("Borrar", id="borrarNotaBoton"),
            Button("Volver", id="back"),
        )
        yield Footer()


    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.switch_to_notas()
        elif button_id == "borrarNotaBoton":
            self.app.cn.borrar(Nota(self.query_one(Input).value))
            self.app.switch_to_notas()

class NotaScreen(Screen):
    BINDINGS = [
        Binding(
            key="q",
            action="quit",
            description="Salir"
        ),
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()
        
        yield Container(
            Button("Nuevo", id="nuevaNota"),
            Button("Borrar", id="borrarNota"),
            Button("Volver", id="back"),
        )
        yield Footer()
    
    def _on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type =  "row"
        table.zebra_stripes = True
        notas = [("ID", "Nota")]
        notas += ColeccionNotas().leer()
        table.add_columns(*notas[0])
        table.add_rows(notas[1:])


    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.switch_to_main()
        elif button_id == "nuevaNota":
            self.app.pop_screen()
            self.app.push_screen(NuevaNotaScreen())
        elif button_id == "editarNota":
            self.app.pop_screen()
            self.app.push_screen()
        elif button_id == "borrarNota":
            self.app.pop_screen()
            self.app.push_screen(BorrarNotaScreen())

class NuevaClaseScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Clase")

        yield Container(
            Button("Añadir", id="anadirClaseBoton"),
            Button("Volver", id="back"),
        )
        yield Footer()


    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.switch_to_clases()
        elif button_id == "anadirClaseBoton":
            self.app.cc.insertar(Clase(self.query_one(Input).value))
            self.app.switch_to_clases()

class BorrarClaseScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Clase")

        yield Container(
            Button("Borrar", id="borrarClaseBoton"),
            Button("Volver", id="back"),
        )
        yield Footer()


    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.switch_to_clases()
        elif button_id == "borrarClaseBoton":
            self.app.cc.borrar(Clase(self.query_one(Input).value))
            self.app.switch_to_clases()
            

class ClaseScreen(Screen):
    BINDINGS = [
        Binding(
            key="q",
            action="quit",
            description="Salir"
        ),
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()
        
        yield Container(
            Button("Nuevo", id="nuevaClase"),
            Button("Borrar", id="borrarClase"),
            Button("Volver", id="back"),
        )
        yield Footer()
    
    def _on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type =  "row"
        table.zebra_stripes = True
        clases = [("ID", "Clase")]
        clases += ColeccionClases().leer()
        table.add_columns(*clases[0])
        table.add_rows(clases[1:])


    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.switch_to_main()
        elif button_id == "nuevaClase":
            self.app.pop_screen()
            self.app.push_screen(NuevaClaseScreen())
        elif button_id == "editarClase":
            self.app.pop_screen()
            self.app.push_screen()
        elif button_id == "borrarClase":
            self.app.pop_screen()
            self.app.push_screen(BorrarClaseScreen())

class MainApp(App):
    def on_mount(self) -> None:
        self.push_screen(MainMenu())
        self.ca = ColeccionAlumnos()
        self.cn = ColeccionNotas()
        self.cc = ColeccionClases()

    def switch_to_alumnos(self) -> None:
        self.push_screen(AlumnoScreen())

    def switch_to_notas(self) -> None:
        self.push_screen(NotaScreen())

    def switch_to_clases(self) -> None:
        self.push_screen(ClaseScreen())

    def switch_to_main(self) -> None:
        self.push_screen(MainMenu())

        

if __name__ == "__main__":
    app = MainApp()
    app.run()
