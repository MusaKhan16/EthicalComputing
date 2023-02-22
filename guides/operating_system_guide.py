import platform
import rich


class OperatingSystemGuide:
    """Operating system guide to help users in regulating their OS"""

    def __init__(self, console: rich.console.Console):
        self.console = console

    def describe(self):
        """Describing the guide and all of its functions"""
        self.console.print("[u]Operating System Guide 101[/u]")

        self.console.print(
            "[b]This guide teaches the fundamental ethical practices that should be taken into account when dealing with your operating system[/b]"
        )

        self.console.print(
            "This guide contains the following tools:\n"
            "\t- Operating System Update tool\n"
        )

    def start_guide(self):
        # Operating system map for OS update guides

        operating_system_update_map = {
            "Windows": "https://support.microsoft.com/en-us/windows/update-windows-3c5ae7fc-9fb6-9af1-1984-b5e0412c556a",
            "Java": "https://support.apple.com/en-us/HT201541",
            "Linux": "https://ubunlog.com/en/como-actualizar-tu-distro-linux-a-la-ultima-version-estable/",
        }

        self.console.rule("Operating System Guide 101")

        self.console.print(
            "\nChecking and updating software is essential to keep safe on your devices\n"
            "Updating your Operating System alone is extremely important due to\n"
            "vulnerabilites attackers discover on old software.\n"
            "New Software comes with fixes of bugs and vulnerability and always keeps you\n"
            "safer."
        )

        # Scanning to see the OS and getting the correct update link for it

        self.console.print(
            "\nScanning your computer, it seems your device is running on",
            platform.system(),
        )

        self.console.print(
            f"Here is guide to installing latest version of your operating system {operating_system_update_map.get(platform.system(), '[red]ERROR[/red]')}"
        )
