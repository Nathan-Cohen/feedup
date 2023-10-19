import random

class Feedup:
    def __init__(self):
        """
        Initialize a Feedup instance with initial attributes.
        """
        self.money = 1000
        self.health = 100
        self.happiness = 100
        self.age = 0
        self.evolution = False
        self.diseases = 0
        self.medical_care = 0
        self.turns = 0

    def life_event(self):
        """
        Simulate random life events that affect the character's attributes.
        """
        event = random.choice(["promotion", "accident", "loterie"])

        if event == "promotion":
            print("Congratulations! You got a promotion. Your money increases.")
            self.money += 200
            self.happiness = min(self.happiness + random.randint(20, 30), 100)
        elif event == "accident":
            print("Oh no! You had an accident. Your health decreases.")
            self.health -= random.randint(10, 20)
            self.happiness -= random.randint(10, 30)
        elif event == "loterie":
            print("You won the lottery! You are rich!")
            self.money += 500
            self.happiness = min(self.happiness + random.randint(20, 30), 100)

        self.check_health()

    def check_and_trigger_event(self):
        """
        Check and trigger random life events based on a probability.
        """
        if random.random() < 0.2:
            self.life_event()

    def receive_medical_care(self):
        """
        Receive medical care to improve health and reduce the number of diseases.
        """
        cost = 50  # Cost of medical care
        if self.money >= cost:
            self.money -= cost
            self.medical_care += 1
            self.health = min(self.health + random.randint(10, 20), 100)
            self.diseases = max(self.diseases - 1, 0)  # Reduce the number of diseases
        else:
            print("You don't have enough money for medical care.")

    def check_health(self):
        """
        Simulate diseases and their effects on health.
        """
        if random.random() < 0.05:
            self.diseases += 1
            self.health = max(self.health - random.randint(5, 15), 0)
            print("Your character has contracted a disease!")

    def work(self):
        """
        Simulate working, considering health's impact on work efficiency.
        """
        work_efficiency = self.health / 100
        earnings = random.randint(50, 200) * work_efficiency
        self.money += earnings
        self.health -= random.randint(5, 20)
        self.happiness -= random.randint(3, 10)
        self.check_health()
        self.check_and_trigger_event()
        self.evolve()

    def display_health(self):
        """
        Display health and the number of diseases.
        """
        print(f"Health: {self.health}%")
        print(f"Diseases: {self.diseases}")

    def feed(self):
        """
        Simulate feeding, affecting health and happiness.
        """
        self.money -= 50
        self.health = min(self.health + random.randint(5, 20), 100)
        self.happiness = min(self.happiness + random.randint(5, 10), 100)
        self.check_health()
        self.check_and_trigger_event()
        self.evolve()

    def play(self):
        """
        Simulate playing, affecting health and happiness.
        """
        self.money -= 20
        self.health -= random.randint(1, 10)
        self.happiness = min(self.happiness + random.randint(10, 30), 100)
        self.check_health()
        self.check_and_trigger_event()
        self.evolve()

    def check_status(self):
        """
        Check the character's status, including life and financial conditions.
        """
        if self.health <= 0 or self.happiness <= 0:
            return "Your Feedup has passed away :("
        if self.money <= 0:
            return "You've gone bankrupt!"
        if self.age >= 30:
            return "Your Feedup has retired."
        return "In good health and prosperous."

    def age_one_year(self):
        """
        Simulate character aging and its effects on attributes.
        """
        self.age += 1
        self.evolve()
        self.check_health()

    def evolve(self):
        """
        Simulate character evolution under specific conditions.
        """
        if self.age in [5, 17, 20] and self.health >= 50 and self.happiness >= 50:
            self.evolution = True
        else:
            self.evolution = False

def display_feedup(feedup):
    """
    Display the attributes and status of the character.
    """
    ascii_art = """
       \ V /
       - . -
       /   \ 
     """
    print(ascii_art)
    print(f"Money: {feedup.money}€")
    print(f"Health: {feedup.health}%")
    print(f"Happiness: {feedup.happiness}%")
    print(f"Age: {feedup.age} years")
    if feedup.evolution:
        print("Your Feedup has evolved!")

def main():
    """
    Main game loop to interact with the Feedup character.
    """
    feedup = Feedup()

    while True:
        print("=== Feedup ===")
        display_feedup(feedup)
        print("===========================")

        print("What do you want to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Work")
        print("4. Receive Medical Care")
        print("5. Quit")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            feedup.feed()
        elif choice == "2":
            feedup.play()
        elif choice == "3":
            feedup.work()
        elif choice == "4":
            feedup.receive_medical_care()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

        feedup.age_one_year()

        status = feedup.check_status()
        if status != "In good health and prosperous.":
            print(status)
            break
        feedup.display_health()

if __name__ == "__main__":
    main()
