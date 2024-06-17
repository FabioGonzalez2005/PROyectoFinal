from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Static, Footer
from textual.binding import Binding

class MainMenu(App):
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
            self.show_alumno_screen()

    def show_alumno_screen(self):
        self.clear_screen()
        self.mount(AlumnoScreen())

    def clear_screen(self):
        self.query_one("#menu").remove()

class AlumnoScreen(Container):


    def compose(self) -> ComposeResult:
        yield Container(
            Button("Volver", id="back"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        print(f"{button_id} button pressed")

if __name__ == "__main__":
    MainMenu().run()
