import rich

from rich.prompt import Prompt
from utils.file_size_convert import convert_file_size, FileSize


class StorageGuide:
    """Storage guide that encourages how to keep storage safe and maintained"""

    def __init__(self, console: rich.console.Console):
        self.console = console

    def describe(self):
        """Describing the tools and material of the guide"""
        self.console.print("[u]Storage Guide 101[/u]")

        self.console.print(
            "[b]This Guide teaches the fundamental knowlegde and practices[/b]"
            " [b]One should perform in order to keep their storage safe[/b]"
        )

        self.console.print(
            "This guide contains the following tools:\n"
            "\t- Storage size conversion calculator\n"
        )

    def start_guide(self):
        self.console.rule("Storage Guide 101")

        # Educating the user on storage practices

        self.console.print(
            "Storage is a critical component of modern technology,\n"
            "allowing us to store and access vast amounts of data quickly and easily.\n"
            "Whether it's personal photos and documents or critical business information, our storage\n"
            "is the foundation upon which our digital lives are built.\n"
        )

        self.console.print(
            "Protecting this data is crucial, as loss or corruption can have serious\n"
            "consequences, including financial losses, legal repercussions, and emotional distress.\n"
            "Cybersecurity threats, hardware failures, and natural disasters are just a few of the potential\n"
            "dangers that can threaten our storage, making it imperative that we take steps to safeguard our\n"
            "data through regular backups, secure storage methods, and other protective measures.\n"
        )

        self.console.print(
            "Backups can be achieved by storing the data via a hard drive, or utilizing the cloud\n"
            "Some of the top [u]free[/u] cloud storage services can include [blue][link=https://www.google.com/intl/en_ca/drive/]Google Drive[/link][/blue],\n"
            "[blue][link=https://www.apple.com/ca/icloud/]iCloud[/link][/blue] and [blue][link=https://www.microsoft.com/en-us/microsoft-365/onedrive/free-online-cloud-storage/]One Drive[/link][/blue]"
        )

        self.console.print(
            "Go to one of the services and enter the amount of free storage they offer.\n"
            "To put it into perspecitve you can enter the amount in GB and I will convert it to either mb or kb\n"
        )

        # Asking the user to try the file size converter tool

        size_in_gb = ""

        while not size_in_gb.isdigit():
            size_in_gb = Prompt.ask(
                "Size in GB [number]",
            )

            if not size_in_gb.isdigit():
                self.console.print("\n[red][r]The given value isnt a number![/r][/red]")

        convert_to_metric = Prompt.ask(
            "What other unit do you want to convert to", choices=["kb", "mb"]
        )

        self.console.print(
            f"The conversion of {size_in_gb}gb to {convert_to_metric} is {convert_file_size(int(size_in_gb), FileSize.GB, FileSize(convert_to_metric)):,} {convert_to_metric}"
        )
