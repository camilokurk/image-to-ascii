from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button, Digits
from textual.containers import HorizontalGroup, VerticalScroll

class TimeDisplay(Digits):
    def compose(self) -> ComposeResult:
        yield Button

class Stopwatch(HorizontalGroup):

    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.0")

class StopwatchApp(App):

    BINDINGS = [("c", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch())

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = StopwatchApp()
    app.run()