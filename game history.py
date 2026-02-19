# initialise list to hold game history
game_history = []

#get data #base component does this already, code below for testing purpose)


while True:
    rounds_played = input("round? ")
    if rounds_played == "":
        break

    user_points = int(input("how many points you have? "))
    comp_points = int(input("comp points? "))
    winner = input("who won? ")
    user_score = int(input("User Score "))
    comp_score = int(input("Computer Score "))

    game_results = (f"Round {rounds_played}: User Points {user_points} | "
                   f"Computer Points {comp_points}, {winner} wins "
                   f"({user_score} | {comp_score})")

    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)