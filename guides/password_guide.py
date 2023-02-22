from hashlib import sha1
from rich.prompt import Prompt


import requests
import rich
import re


class PasswordProtectionGuide:
    """
    An ethical computing guide on protecting and making strong passwords
    """

    PWNED_PASSWORD_API = "https://api.pwnedpasswords.com/range/{password}"

    def __init__(self, console: rich.console.Console):
        self.console = console

    def determine_pwned_password_occurences(self, password: str) -> int:
        """Determine how many times password has been used before"""

        serialized_password = sha1(password.encode()).hexdigest().upper()

        prefix, suffix = serialized_password[:5], serialized_password[5:]

        response = requests.get(
            PasswordProtectionGuide.PWNED_PASSWORD_API.format(password=prefix)
        )

        if response.status_code == 404:
            return 0

        for hash in response.text.splitlines():
            hash_suffix, number_pwned = hash.split(":")

            if hash_suffix == suffix:
                return int(number_pwned)

        return 0

    def test_password_strength(self, password: str) -> bool:
        """Determine if the password is strong"""

        # Checking if the length of the password is greather than or equal to
        if len(password) < 12:
            return False

        # The regex string provided checks if a passowrd has at least
        # two lower case charachters, two upper case, 2 symbols and two numbers

        if not re.search(
            r"(?=^.{12,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$",
            password,
        ):
            return False

        return True

    def describe(self):
        self.console.print("[u]Password Protection Guide 101[/u]")

        self.console.print(
            "[b]This guide teaches the fundamental ethical practices that should be taken into account when dealing with passwords[/b]"
        )

        self.console.print(
            "This guide contains the following tools:\n"
            "\t- Pwned Password detector\n"
            "\t- Password Strength Test\n"
        )

    def pwned_password_guide(self):
        """The guide to check if a password has been breached before"""

        user_input = ""

        while user_input.lower() != "no":
            user_password = self.console.input(
                "\n[b]Enter a password to check if it has been pwned:[/b] "
            )

            if " " in user_password:
                self.console.print("\n[red][r]There cannot be any spaces![/r][red]")
                continue

            self.console.print(
                f"\nThe password [i][b]{user_password}[/b][/i] has been seen {self.determine_pwned_password_occurences(user_password):,} times"
            )

            user_input = Prompt.ask(
                "Do you want to try another password?", choices=["yes", "no"]
            )

    def strong_password_guide(self):
        """The guide to check if a password is strong enough"""

        # Asking for the password and checking if its valid

        user_input = ""

        while user_input.lower() != "no":
            user_password = self.console.input(
                "\nEnter a password to test its strength: "
            )

            if " " in user_password:
                self.console.print("[red][h]The password cannot have spaces![/h][/red]")
                continue

            password_is_strong = self.test_password_strength(user_password)

            # Telling the user if the password is strong or not
            # Also asking if they want to try another password

            self.console.print(
                f"[b]This password {'[green]passes[/green]' if password_is_strong else '[red]fails[/red]'} the test[/b]"
            )

            user_input = Prompt.ask(
                "Do you want to test another password?",
                choices=["yes", "no"],
            )

    def start_guide(self):
        self.console.rule("Password Protection Guide 101")

        # Giving the users knowlegde on passwords and password protection

        self.console.print(
            "\nPasswords are [u]crucial[/u] for protecting personal and sensitive information\n"
            "from unauthorized access as they prevent [red]identity theft[/red] 🥷 and ensure\n"
            "the [b]security[/b] of online accounts. Using strong and unique passwords can greatly\n"
            "reduce the risk of data breaches and cyber attacks.\n"
        )

        self.console.print(
            "Here are a few ways we can create strong passwords and minimize\n"
            "chances of being victims of attack."
        )

        self.console.print(
            "\n 1. [bold]Checking if your password has been used before[/bold]",
            justify="center",
        )

        self.console.print(
            "Due to the vast populous of users growing every day\n"
            "Some passwords are becoming common and have already been breached.\n"
            "This is why it is important to check if your password has been pwned before\n"
        )

        # starting the breached password guide/tool

        self.pwned_password_guide()

        self.console.print(
            "If you've successfully been able to make sure the password is not pwned,\n"
            "You need to verify that it is strong such that it stays hidden.\n"
            "Regularly, a strong password should maintain a length of approximately 12 charachters\n"
            "Two upper case letters, and two numbers\n"
        )

        # Start the password strength test
        self.strong_password_guide()
