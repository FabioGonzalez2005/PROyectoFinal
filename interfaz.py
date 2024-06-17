from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Footer, DataTable
from textual.binding import Binding
from textual.screen import Screen


class MainMenu(Screen):
    CSS = """
    #menu {
        align: center middle;
        height: 100%;
    }
    """

    BINDINGS = [
        Binding(
            key="n",
            action="show_alumno_screen",
            description="Nuevo"
        ),
        Binding(
            key="e",
            action="help",
            description="Editar"
        ),
        Binding(
            key="b",
            action="help3",
            description="Borrar"
        ),
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

class AlumnoScreen(Screen):

    def compose(self) -> ComposeResult:
        table = DataTable(id="alumno_table")
        table.add_column("ID")
        table.add_column("Nombre")
        table.add_row("1", "Juan")
        table.add_row("2", "Ana")
        
        yield Container(
            table,
            Button("Volver", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.pop_screen()

class NotaScreen(Screen):

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

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.pop_screen()

class ClaseScreen(Screen):

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

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back":
            self.app.pop_screen()

class MainApp(App):
    def on_mount(self) -> None:
        self.push_screen(MainMenu())


if __name__ == "__main__":
    MainApp().run()
