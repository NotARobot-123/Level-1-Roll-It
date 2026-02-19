#At the start of the game, the computer / user score are both zero
comp_score = 0
user_score = 0

game_goal = int(input("game goal")) # should be a function call

# play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    #start of round loop
    #for testing purposes, ask the user what the points for the user n/ computer were
    comp_points = int(input("enter comp points at round end"))
    user_points = int(input("enter user points at round end"))

    #outside rounds loop - update score with round points, only add points to the score of the winner
    comp_score += comp_points
    user_score += user_points

    # show overall scores (add this to rounds loop)
    print("*** Game Update ***") # replace with call to statement generator
    print(f"User Score: {user_score} | Computer Score: {comp_score}")


#end of entire game, output final results
print()
if user_score > comp_score:
    print("*** You win! ***") # replace this with statement generator call
else:
    print("*** You lose! ***")
