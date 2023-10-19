import random

class Actions:
    """
    Class to handle character actions like feeding, playing, working, and medical care.
    """

    def __init__(self, character):
        """
        Initialize an Actions object.

        Args:
            character (Feedup): The character on which actions will be performed.
        """
        self.character = character

    def feed(self):
        """
        Feed the character. Increase health and happiness while deducting money. Check health and trigger events.
        """
        cost = 50
        if self.character.money >= cost:
            self.character.money -= cost
            self.character.health = min(self.character.health + random.randint(5, 20), 100)
            self.character.happiness = min(self.character.happiness + random.randint(5, 10), 100)
            self.character.update_status
        else:
            self.character.messages.append("You don't have enough money to feed your character.")

    def play(self):
        """
        Play with the character. Affect health, happiness, and money. Check health and trigger events.
        """
        cost = 20
        if self.character.money >= cost:
            self.character.money -= cost
            self.character.health -= random.randint(1, 10)
            self.character.happiness = min(self.character.happiness + random.randint(10, 30), 100)
            self.character.update_status
        else:
            self.character.messages.append("You don't have enough money to play with your character.")

    def work(self):
        """
        Make the character work. Affect money, health, and happiness. Check health and trigger events.
        """
        earnings = random.randint(50, 200)
        self.character.money += earnings
        self.character.health -= random.randint(5, 20)
        self.character.happiness -= random.randint(3, 10)
        self.character.update_status

    def receive_medical_care(self):
        """
        Provide medical care to the character. Improve health and reduce diseases.
        """
        cost = 50
        if self.character.money >= cost:
            self.character.money -= cost
            self.character.soins_medicaux += 1
            self.character.health = min(self.character.health + random.randint(10, 20), 100)
            self.character.maladies = max(self.character.maladies - 1, 0)
        else:
            self.character.messages.append("You don't have enough money for medical care.")

