import random
secret_no = random.randint(1, 10)
no_of_chances = 3
i = 0
while i < no_of_chances:
    guess = int(input("Make guess: "))
    if guess != secret_no:
        print("WRONG GUESS")
        i = i+1
    else:
        print("YOU WON")
        break
else:
    print("YOU LOSE")
    print(f"Secret Number was {secret_no}")
