import random


def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    #Roll the dice for the user and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total} ")

    return total, double

    #initialise rounds points
    user_points = 0
    comp_points = 0




    #Roll the dice for the computer
    comp_one = random.randint(1, 6)
    comp_two = random.randint(1, 6)

    user_points += roll_one + roll_two
    comp_points += comp_one + comp_two

    #Update the user / computer points
    print("\nInitial Points")
    print(f"User     - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {user_points} ")
    print(f"Computer - Roll 1: {comp_one} \t| Roll 2: {comp_two} \t| Total: {comp_points} ")

    #output the results
    if double == "yes":
        print("Great news - if you win, you will get double points")
