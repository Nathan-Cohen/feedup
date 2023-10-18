
# Feedup

`Feedup` is a Python class that simulates the financial and well-being aspects of a character's life. This character's life is influenced by various events, actions, and random occurrences. The class helps you track your character's money, health, happiness, age, and evolution over time.

## Specifications

### Initial State

-   Initial Money: 1000€
-   Initial Health: 100% (represents physical health)
-   Initial Happiness: 100% (represents emotional well-being)
-   Initial Age: 0 years
-   Initial Evolution State: False
-   Initial Number of Diseases (Maladies): 0
-   Initial Number of Medical Treatments (Soins Médicaux): 0
-   Initial Turns (number of actions taken): 0


### Life Events

-   Events can be one of three types: "promotion," "accident," or "lottery."
-   **Promotion:**
    -   Increases money.
    -   Increases happiness (20-30%).
-   **Accident:**
    -   Decreases health (10-20%).
    -   Decreases happiness (10-30%).
-   **Lottery:**
    -   Increases money.
    -   Increases happiness (20-30%).

### Health and Diseases

-   Health is influenced by random diseases that can occur.
-   Diseases reduce health and are randomly contracted.
-   Diseases are rare, with a 5% chance of occurring.


### Actions

-   Actions available to the character include working, feeding, and playing.
-   **Working:**
    -   Increases money.
    -   Decreases health (5-20%).
    -   Decreases happiness (3-10%).
-   **Feeding:**
    -   Costs 50€.
    -   Increases health (5-20%).
    -   Increases happiness (5-10%).
-   **Playing:**
    -   Costs 20€.
    -   Decreases health (1-10%).
    -   Increases happiness (10-30%).
-   Actions can trigger life events and affect health.

### Evolution

-   Evolution is possible at ages 5, 17, and 20.
-   Evolution depends on having good health and high happiness.
-   Evolution state is toggled between True and False.

### Aging

-   The character ages one year with each turn.
-   Aging affects evolution and health.

### Medical Care

-   Medical treatments cost 50€.
-   They can improve health, and reduce the number of diseases.

### Status Checking

-   The status is checked regularly.
-   The character can die if health or happiness reach zero, resulting in a game over.
-   Bankruptcy is possible if money falls below zero.
-   Retirement occurs at age 30.
-   The game continues until a game-over condition is met.

## Usage

1.  Import the `Feedup` class.
2.  Create an instance of the class.
3.  Interact with the character by choosing actions:
    -   1 for feeding
    -   2 for playing
    -   3 for working
    -   4 for medical care
    -   5 to quit the game
4.  The character will age one year with each action.
5.  The game continues until a game-over condition is met.

## Example

pythonCopy code

`if __name__ == "__main__":
    main()` 

## Acknowledgments

This class is a simple simulation of financial and well-being aspects of a character's life. Feel free to use and modify it for your own projects and experiments.

`Don't hesitate to make pull requests to improve the project.`