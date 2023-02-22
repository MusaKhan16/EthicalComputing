from rich.console import Console
from rich.prompt import Prompt

from guides import (
    EthicalGuide,
    PasswordProtectionGuide,
    OperatingSystemGuide,
    StorageGuide,
    EncryptionGuide,
)


def main():
    """Entry point of Ethical Computer Practices guide"""

    # Console object that will be used for rich text logging
    console = Console()

    # The available guides users are able to view
    guides: list[EthicalGuide] = [
        PasswordProtectionGuide(console=console),
        OperatingSystemGuide(console=console),
        StorageGuide(console=console),
        EncryptionGuide(console=console),
    ]

    # Welcoming users

    console.rule("Welcome to ethical computing practices 101")

    console.print(
        "We [u]teach[/u] and [u]encourage ethical[/u] computing practices to keep you safer on your device!"
    )

    user_menu_choice = ""

    # Main loop that closes when the user quits using q
    # Continues looping otherwise

    while user_menu_choice != "q":
        console.print("\n[b]Here are our guides:[/b]\n")

        # Displaying the guides that a user can view
        for idx, guide in enumerate(guides):
            print(f"{idx + 1})")
            guide.describe()

        console.print(
            "[b][u]Menu[/u][/b]\n"
            "[0] To go through the entire course \n"
            "⭐  Or enter any of the guide numbers shown above\n"
            "❌  Or enter q to quit"
        )

        # Asks user for what choice they want to make
        user_menu_choice = Prompt.ask(
            "choice",
            choices=["0", "q", *map(str, range(1, len(guides) + 1))],
            show_choices=False,
        )

        # Deciding which guide to run for the user
        if user_menu_choice == "0":
            for guide in guides:
                guide.start_guide()

        elif user_menu_choice.isdigit():
            guides[int(user_menu_choice) - 1].start_guide()

    console.rule("[red]Bye![/red]")


if __name__ == "__main__":
    main()
