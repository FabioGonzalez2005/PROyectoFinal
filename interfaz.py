from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Footer, DataTable, Input
from textual.binding import Binding
from textual.screen import Screen
from coleccionAlumnos import ColeccionAlumnos
from coleccionNotas import ColeccionNotas
from coleccionClases import ColeccionClases

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
            self.app.pop_screen()
        elif button_id == "anadirAlumnoBoton":
            ColeccionAlumnos().insertar()

class AlumnoScreen(Screen):
    BINDINGS = [
        # Binding(
        #     key="n",
        #     action="switch_mode('nuevoAlumno')",
        #     description="Nuevo"
        # ),
        # Binding(
        #     key="e",
        #     action="switch_mode('editarAlumno')",
        #     description="Editar"
        # ),
        # Binding(
        #     key="b",
        #     action="switch_mode('borrarAlumno')",
        #     description="Borrar"
        # ),
        Binding(
            key="q",
            action="quit",
            description="Salir"
        ),
    ]

    # MODES = {
    #     "nuevoAlumno": NuevoAlumnoScreen,
    #     "editarAlumno": EditarAlumnoScreen,
    #     "borrarAlumno": BorrarAlumnoScreen,
    # }

    def compose(self) -> ComposeResult:
        yield DataTable()
        
        yield Container(
            Button("Nuevo", id="nuevoAlumno"),
            Button("Editar", id="editarAlumno"),
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
            self.app.pop_screen()
        elif button_id == "nuevoAlumno":
            self.app.pop_screen()
            self.app.push_screen(NuevoAlumnoScreen())
        elif button_id == "editarAlumno":
            self.app.pop_screen()
            self.app.push_screen()
        elif button_id == "borrarAlumno":
            self.app.pop_screen()
            self.app.push_screen()

class NotaScreen(Screen):
    BINDINGS = [
        # Binding(
        #     key="n",
        #     action="nuevaNota",
        #     description="Nuevo"
        # ),
        # Binding(
        #     key="e",
        #     action="editarNota",
        #     description="Editar"
        # ),
        # Binding(
        #     key="b",
        #     action="borrarNota",
        #     description="Borrar"
        # ),
        Binding(
            key="q",
            action="quit",
            description="Salir"
        ),
    ]
    def compose(self) -> ComposeResult:
        table = DataTable(id="nota_table")
        table.add_column("ID")
        table.add_column("Nota")
        table.add_row("1", "8.8")
        table.add_row("2", "9.6")
        
        yield Container(
            table,
            Button("Volver", id="back"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.pop_screen()

class ClaseScreen(Screen):
    BINDINGS = [
        Binding(
            key="n",
            action="añadirClase",
            description="Nuevo"
        ),
        Binding(
            key="e",
            action="editarClase",
            description="Editar"
        ),
        Binding(
            key="b",
            action="borrarClase",
            description="Borrar"
        ),
        Binding(
            key="q",
            action="quit",
            description="Salir"
        ),
    ]
    def compose(self) -> ComposeResult:
        table = DataTable(id="clase_table")
        table.add_column("ID")
        table.add_column("Clase")
        table.add_row("1", "4ºC")
        table.add_row("2", "1ºA")
        
        yield Container(
            table,
            Button("Volver", id="back"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.pop_screen()

class MainApp(App):
    def on_mount(self) -> None:
        self.push_screen(MainMenu())

if __name__ == "__main__":
    MainApp().run()
