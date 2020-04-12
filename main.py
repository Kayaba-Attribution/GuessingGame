guess_count = 0
random_number = random.randint(0, 21)
print("Guess the random number between 1 and 20 to win! You have 5 guesses")
possible_guesses = range(0, 21)
while guess_count <= 5:
    try:
        guess = int(input('> '))
    except ValueError:
        print("Invalid. Try again!")
        continue
    if guess == random_number:
        print('That is correct. You win!')
        break
    elif guess not in possible_guesses:
        print('Number is between 1 and 20. Try again.')
        guess_count += 1
    elif guess < random_number:
        print("Too low. Try again.")
        guess_count += 1
    elif guess > random_number:
        print("Too high. Try again.")
        guess_count += 1
    
if guess != random_number:
    print(f'I am sorry but you lost. The number was {random_number}.')
else:
    pass
