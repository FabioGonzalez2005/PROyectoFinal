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

if __name__ == "__main__":
    MainMenu().run()
