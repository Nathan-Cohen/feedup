class Display:
    """
    Class to display the character's attributes and evolution.
    """

    def __init__(self, character):
        """
        Initialize a Display object.

        Args:
            character (Feedup): The character to display.
        """
        self.character = character

    def display(self):
        """
        Display the character's attributes and evolution.
        """
        ascii_art = r"""
           \ V /
           - . -
           /   \ 
        """
        print(ascii_art)
        print(f"Money: {self.character.money}€")
        print(f"Health: {self.character.health}%")
        print(f"Happiness: {self.character.happiness}%")
        print(f"Age: {self.character.age} years")
        if self.character.evolution:
            print("Your character has evolved!")

        print(f"Health: {self.character.health}%")
        print(f"Diseases: {self.character.maladies}")
