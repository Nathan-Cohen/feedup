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

    def messages_display(self):
        if len(self.character.messages) > 0:
            msg = [print("===========================\n" + msg) for msg in self.character.messages]
            self.character.messages = []
            return msg

    def display(self):
        """
        Display the character's attributes and evolution.
        """
        ascii_art = r"""
           ¯\_(O_O)_/¯
        """
        print(ascii_art)
        print(f"Money: {self.character.money}€")
        print(f"Health: {self.character.health}%")
        print(f"Happiness: {self.character.happiness}%")
        print(f"Age: {self.character.age} years")
        print(f"Diseases: {self.character.maladies}")
        if self.character.evolution:
            print("Your character has evolved!")
        self.messages_display()