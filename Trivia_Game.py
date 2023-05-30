print("Welcome to Game of Thrones Trivia!")

playing = input("Would you like to play?")

if playing != "yes":
    quit()

print("Awesome! Let the Games Begin!")
score = 0

answer = input("Who pushed Bran out of the window in the first episode? ")
if answer == "Jaime Lannister":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many direwolves were given to the Stark kids? ")
if answer == "6":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many direwolves died in the show? ")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Jaime Lannisters nickname? ")
if answer == "Kingslayer":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who built the wall? ")
if answer == "Castle Black":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 5) * 100) + "%.")
