from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Static

class MainMenu(App):
    CSS = """
    #menu {
        align: center middle;
        height: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Container(
            Button("Alumno", id="alumno"),
            Button("Nota", id="nota"),
            Button("Clase", id="clase"),
            id="menu",
        )

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
    CSS = """
    #alumno_menu {
        align: center middle;
        height: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Container(
            Button("Añadir", id="add"),
            Button("Editar", id="edit"),
            Button("Borrar", id="delete"),
            id="alumno_menu",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        print(f"{button_id} button pressed")

if __name__ == "__main__":
    MainMenu().run()
