import random

def roll_dice():
    
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    
    
    print(f"Dice 1: {dice_1}, Dice 2: {dice_2}")
    print(f"Total: {dice_1 + dice_2}")
    print("-" * 20)


while True:
    user_input = input("Press 'r' to roll the dice or 'q' to quit: ").lower()
    
    if user_input == 'r':
        roll_dice()
    elif user_input == 'q':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'r' to roll or 'q' to quit.")

    


for _ in range(5):
    roll_dice()
    print("-" * 20) 