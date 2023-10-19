import random

from actions import Actions
from calculations import Calculations
from display import Display

class Feedup:
    """
    Class to represent the character, manage their attributes, and handle life events.
    """

    def __init__(self):
        """
        Initialize a Feedup character.
        """
        self.money = 1000
        self.health = 100
        self.happiness = 100
        self.age = 0
        self.evolution = False
        self.maladies = 0
        self.soins_medicaux = 0

    def check_and_trigger_event(self):
        """
        Check for life events and trigger them.
        """
        if random.random() < 0.2:
            event = self.generate_event()
            self.life_event(event)

    def life_event(self, event):
        """
        Handle a life event and adjust character attributes.

        Args:
            event (str): The life event type (e.g., "promotion", "accident").
        """
        if event == "promotion":
            print("Congratulations! You got a promotion. Your money increases.")
            self.money += 200
            self.happiness += min(self.happiness + random.randint(20, 30), 100)
        elif event == "accident":
            print("Oh no! You had an accident. Your health decreases.")
            self.health -= random.randint(10, 20)
            self.happiness -= random.randint(10, 30)
        elif event == "lottery":
            print("You won the lottery! You're rich!")
            self.money += 500
            self.happiness += min(self.happiness + random.randint(20, 30), 100)

        self.check_health()

    def check_health(self):
        """
        Simulate diseases and affect the character's health.
        """
        if random.random() < 0.05:
            self.maladies += 1
            self.health = max(self.health - random.randint(5, 15), 0)
            print("Your character has contracted a disease!")

    def evolve(self):
        """
        Evaluate if the character should evolve based on age, health, and happiness.
        """
        if self.age in [5, 17, 20] and self.health >= 50 and self.happiness >= 50:
            self.evolution = True
        else:
            self.evolution = False

    def generate_event(self):
        """
        Generate a random life event.

        Returns:
            str: The generated life event (e.g., "promotion", "accident").
        """
        event = random.choice(["promotion", "accident", "lottery"])
        return event

class Main:
    """
    Class to run the main program for character management.
    """

    def run(self):
        """
        Run the main program for character management.
        """
        character = Feedup()
        actions = Actions(character)
        calculations = Calculations(character)
        display = Display(character)

        while True:
            print("=== Feedup ===")
            display.display()
            print("===========================")

            print("What would you like to do?")
            print("1. Feed")
            print("2. Play")
            print("3. Work")
            print("4. Medical Care")
            print("5. Quit")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                actions.feed()
            elif choice == "2":
                actions.play()
            elif choice == "3":
                actions.work()
            elif choice == "4":
                actions.receive_medical_care()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

            calculations.age_one_year()

if __name__ == "__main__":
    app = Main()
    app.run()
