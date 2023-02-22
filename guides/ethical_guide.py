from typing import Protocol


class EthicalGuide(Protocol):
    """An interface for ethical guides"""

    def start_guide(self):
        """
        The entrypoint to the guide, main logic and points
        as well as interactions with user occur here
        """

    def describe(self):
        """
        The method that describes the overall guide, and what it offers
        """
