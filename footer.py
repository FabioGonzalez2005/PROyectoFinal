from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer


class FooterApp(App):
    BINDINGS = [
        Binding(key="q", action="quit", description="Salir"),
        Binding(
            key="e",
            action="help",
            description="Editar"
        ),
        Binding(
            key="n",
            action="help2",
            description="Nuevo"
        ),
        Binding(
            key="b",
            action="help3",
            description="Borrar"
        ),

    ]

    def compose(self) -> ComposeResult:
        yield Footer()


if __name__ == "__main__":
    app = FooterApp()
    app.run()