from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer


class FooterApp(App):
    BINDINGS = [
        Binding(
            key="n",
            action="help2",
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
            description="Salir"),

    ]

    def compose(self) -> ComposeResult:
        yield Footer()


if __name__ == "__main__":
    app = FooterApp()
    app.run()