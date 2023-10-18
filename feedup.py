import random

class Feedup:
    def __init__(self):
        self.money = 1000
        self.health = 100
        self.happiness = 100
        self.age = 0
        self.evolution = False
        self.maladies = 0
        self.soins_medicaux = 0
        self.turns = 0

    def life_event(self):
        # Simuler des événements de vie aléatoires
        event = random.choice(["promotion", "accident", "loterie"])

        if event == "promotion":
            print("Félicitations ! Vous avez obtenu une promotion. Votre argent augmente.")
            self.money += 200
            self.happiness += min(self.happiness + random.randint(20, 30), 100)
        elif event == "accident":
            print("Oh non ! Vous avez eu un accident. Votre santé diminue.")
            self.health -= random.randint(10, 20)
            self.happiness -= random.randint(10, 30)
        elif event == "loterie":
            print("Vous avez gagné à la loterie ! Vous êtes riche !")
            self.money += 500
            self.happiness += min(self.happiness + random.randint(20, 30), 100)

        self.check_health()

    def check_and_trigger_event(self):
        if random.random() < 0.2:
            self.life_event()

    def receive_medical_care(self):
        cost = 50  # Coût des soins médicaux
        if self.money >= cost:
            self.money -= cost
            self.soins_medicaux += 1
            # Les soins médicaux améliorent la santé
            self.health = min(self.health + random.randint(10, 20), 100)
        else:
            print("Vous n'avez pas assez d'argent pour les soins médicaux.")

    def check_health(self):
        # Simuler les maladies
        if random.random() < 0.05:
            self.maladies += 1
            # Les maladies réduisent la santé
            self.health = max(self.health - random.randint(5, 15), 0)
            print("Votre personnage a contracté une maladie !")

    def work(self):
        # Influence de la santé sur la capacité de travail
        work_efficiency = self.health / 100
        earnings = random.randint(50, 200) * work_efficiency
        self.money += earnings
        self.health -= random.randint(5, 20)
        self.happiness -= random.randint(3, 10)
        self.check_health()
        self.check_and_trigger_event()
        self.evolve()

    def display_health(self):
        print(f"Santé: {self.health}%")
        print(f"Maladies: {self.maladies}")

    def receive_medical_care(self):
        cost = 50  # Coût des soins médicaux
        if self.money >= cost:
            self.money -= cost
            self.soins_medicaux += 1
            # Les soins médicaux améliorent la santé
            self.health = min(self.health + random.randint(10, 20), 100)
            self.maladies = max(self.maladies - 1, 0)  # Réduire le nombre de maladies
        else:
            print("Vous n'avez pas assez d'argent pour les soins médicaux.")

    def feed(self):
        self.money -= 50
        self.health = min(self.health + random.randint(5, 20), 100)
        self.happiness = min(self.happiness + random.randint(5, 10), 100)
        self.check_health()
        self.check_and_trigger_event()
        self.evolve()

    def play(self):
        self.money -= 20
        self.health -= random.randint(1, 10)
        self.happiness = min(self.happiness + random.randint(10, 30), 100)
        self.check_health()
        self.check_and_trigger_event()
        self.evolve()

    def check_status(self):
        if self.health <= 0 or self.happiness <= 0:
            return "Votre feedup est décédé :("
        elif self.money <= 0:
            return "Vous êtes en faillite !"
        elif self.age >= 30:
            return "Votre feedup a pris sa retraite."
        return "En bonne santé et prospère."

    def age_one_year(self):
        self.age += 1
        self.evolve()
        self.check_health()

    def evolve(self):
        if self.age in [5, 17, 20] and self.health >= 50 and self.happiness >= 50:
            self.evolution = True
        else:
            self.evolution = False

def display_feedup(feedup):
    ascii_art = """
       \ V /
       - . -
       /   \ 
     """
    print(ascii_art)
    print(f"Argent: {feedup.money}€")
    print(f"Santé: {feedup.health}%")
    print(f"Bonheur: {feedup.happiness}%")
    print(f"Âge: {feedup.age} ans")
    if feedup.evolution:
        print("Votre feedup a évolué!")

def main():
    feedup = Feedup()

    while True:
        print("=== Feedup ===")
        display_feedup(feedup)
        print("===========================")

        print("Que voulez-vous faire ?")
        print("1. Nourrir")
        print("2. Jouer")
        print("3. Travailler")
        print("4. Soins médicaux")
        print("5. Quitter")
        choice = input("Entrez le numéro de votre choix: ")

        if choice == "1":
            feedup.feed()
        elif choice == "2":
            feedup.play()
        elif choice == "3":
            feedup.work()
        elif choice == "4":
            feedup.receive_medical_care()
        elif choice == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

        feedup.age_one_year()

        status = feedup.check_status()
        if status != "En bonne santé et prospère.":
            print(status)
            break
        feedup.display_health()

if __name__ == "__main__":
    main()
