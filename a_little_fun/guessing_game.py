import random
import requests

"""WARNING if you are extremely bad at following instruction rules, responces may get insulting"""
url = "https://insult.mattbas.org/api/en/insult.json"
number = random.randrange(1, 11)
guess = int(input('Guess my number between 1 - 10\n'))
if 1 <= guess <= 10:
    not_again = False
    while number != guess:
        if 1 > guess or guess > 10:
            if not_again:
                r = requests.get(url)
                r_dict = r.json()
                print(f"{r_dict['insult']}!!! 1 to 10!!!")
            else:
                print('Your not good at this. Remember a number in the range 1 to 10! Now try again!')
                not_again = True
            guess = int(input())
        elif guess < number:
            guess = int(input('To low try again.\n'))
        elif guess > number:
            guess = int(input('To high try again.\n'))
    print('You nailed it!')
else:
    print('Your guess was not in the range.\n')