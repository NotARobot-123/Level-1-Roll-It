

while True:

    want_instructions = input("Do you want the instructions?").lower()
    if want_instructions == "yes"or want_instructions == "y":
        print("you picked yes")
        break

    elif want_instructions == "no"or want_instructions == "n":
        print("you picked no")
        break
    else:
        print("Please select yes or no")

print("We are done here")