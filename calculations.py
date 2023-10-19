class Calculations:
    """
    Class to perform calculations like aging and evolution of the character.
    """

    def __init__(self, character):
        """
        Initialize a Calculations object.

        Args:
            character (Feedup): The character for which calculations will be performed.
        """
        self.character = character

    def age_one_year(self):
        """
        Age the character by one year. Trigger character evolution and check health.
        """
        self.character.age += 1
        self.character.evolve()
        self.character.check_health()
