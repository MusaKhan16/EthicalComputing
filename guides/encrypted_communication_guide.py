import rich
from rich.prompt import Prompt


class EncryptionGuide:
    """An encryption guide to teach users fundamental encryption practices"""

    def __init__(self, console: rich.console.Console):
        self.console = console

    def describe(self):
        """A description of the guide"""
        self.console.print("[u]Encryption Guide 101[/u]")

        self.console.print(
            "[b]This guide will help you with understanding the fundamental ethical"
            " practices that should be taken into account when dealing with [u]data[/u] through encryption.[/b]"
        )

        self.console.print(
            "This guide comes with the following tools:\n"
            "\t- Data encryption and decryption tool"
        )

    def encryption_algorithm(self, text: str, decrypt=False) -> str:
        """Encryption algorithm to encode and decode a piece of text"""

        # Getting the unicode values of each charachter

        unicode_text = map(ord, text)

        # Performing the encoding with each unicode charachter, shifting values
        if decrypt:
            mathematical_encoding = (
                char + (4 + 6 * (char % 2 == 0)) for char in unicode_text
            )
        else:
            mathematical_encoding = (
                char + (-4 - 6 * (char % 2 == 0)) for char in unicode_text
            )

        # Returning the encoding as a string

        return "".join(map(chr, mathematical_encoding))

    def valid_secret(self, text: str) -> bool:
        """Simple function to check if the text is valid for encoding"""
        return text.isalpha() and not (" " in text) and len(text) > 0

    def start_guide(self):
        self.console.rule("Encryption Guide 101")

        # Sharing practices and knowledge to the user

        self.console.print(
            "\nIn today's digital age, the importance of using encrypted communication and apps cannot be overstated.\n"
            "Encryption ensures that our private and sensitive information remains secure and inaccessible to\n"
            "unauthorized parties. With the rise of cybercrime, using apps that encrypt our data is more critical than ever.\n"
            "Additionally, it is important to use HTTPS, a secure form of communication, when browsing websites to prevent\n"
            "eavesdropping and hacking attempts. Moreover, clicking on suspicious links can lead to malware infections, data\n"
            "breaches, and identity theft. It is crucial to exercise caution while using the internet and to take necessary\n"
            "precautions to protect ourselves and our valuable data.\n"
        )

        self.console.print(
            "An amazing tool that can help encrypt your internet activity is a VPN.\n"
            "A VPN or a Virtual Private Network is a tool that helps encrypt your internet connection\n"
            "and network activity.\n"
        )

        # Starting the little encryption activity

        self.console.print(
            f"Encryption methods are vast and complex and however {self.encryption_algorithm('EncryptionIsFun')}\n"
            "Enter the last piece of jibberish to decrypt\n"
        )

        user_decryption_input = Prompt.ask(
            "The text to decrypt",
            choices=[self.encryption_algorithm("EncryptionIsFun")],
            show_choices=False,
        )

        # Decrypting the jibberish and allowing the user to encrypt their own text

        self.console.print(
            self.encryption_algorithm(user_decryption_input, decrypt=True)
        )

        self.console.print(
            "You can enter your own string to encrypt and send messages to your friends\n"
        )

        user_secret = ""

        while not self.valid_secret(user_secret):
            user_secret = self.console.input(
                "Enter your secret without spaces and numbers: "
            )

            if not self.valid_secret(user_secret):
                self.console.print("[red][r]Error Invalid Secret[/r][/red]")
                continue

            self.console.print(self.encryption_algorithm(user_secret))
