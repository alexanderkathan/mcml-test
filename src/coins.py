"""Coin class that can flip a coin."""


class Coin:
    """Class Coin."""

    def __init__(self, current_side: str = "Kopf") -> None:
        """Initialize the coin class."""
        self.current_side = current_side

    def flip_coin(self) -> None:
        """Flips the coin and therefore changes the current_side parameter."""
        if self.current_side == "Kopf":
            self.current_side = "Zahl"
        else:
            self.current_side = "Kopf"

    def get_side(self) -> str:
        """Return the current coin side."""
        return self.current_side

    def set_side(self, side: str) -> None:
        """Set the coin side to a specific string value."""
        self.current_side = side


if __name__ == "__main__":
    c = Coin(current_side="Kopf")
