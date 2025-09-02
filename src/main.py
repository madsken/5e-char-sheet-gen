from rich.console import Console, Group
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
import time

console = Console()

def render_menu(selection: int = 0, user_input: str = ""):
    menu_items = ["View Temperature", "View Pressure", "Exit"]
    menu_render = ""

    for i, item in enumerate(menu_items):
        prefix = "👉 " if i == selection else "   "
        if i == selection:
            menu_render += f"{prefix}[bold green]{item}[/bold green]\n"
        else:
            menu_render += f"{prefix}{item}\n"

    # Combine menu and input
    group = Group(
        Panel(menu_render.strip(), title="Main Menu", subtitle="Use numbers to select"),
        Panel(f"Last input: [bold cyan]{user_input}[/bold cyan]", title="Input")
    )
    return group

def handle_selection(choice: int):
    if choice == 0:
        return Panel("Current temperature is 24°C", title="Temperature")
    elif choice == 1:
        return Panel("Current pressure is 1013 hPa", title="Pressure")
    elif choice == 2:
        raise KeyboardInterrupt
    else:
        return Panel("Invalid choice. Try 0, 1 or 2.", style="bold red", title="Error")

def main():
    selection = 0
    last_input = ""

    with Live(render_menu(selection, last_input), refresh_per_second=10, screen=True) as live:
        while True:
            live.update(render_menu(selection, last_input))
            console.print("\nEnter choice [0-2]: ", end="")
            try:
                last_input = console.input()
                choice = int(last_input)
            except ValueError:
                live.update(Panel("Please enter a number.", style="bold red", title="Error"))
                time.sleep(1.5)
                continue

            live.update(handle_selection(choice))
            time.sleep(2)

if __name__ == "__main__": 
    main()