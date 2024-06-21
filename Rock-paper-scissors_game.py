import random

def get_user_input():
    while True:
        user_inp = input("Choose from rock, paper, scissors: ").lower()
        if user_inp in ['rock', 'paper', 'scissors']:
            return user_inp
        else:
            print("Invalid input. Please choose from rock, paper, or scissors.")

def determine_winner(user_inp, sys_inp):
    if user_inp == sys_inp:
        return "draw"
    elif (user_inp == 'rock' and sys_inp == 'scissors') or \
         (user_inp == 'paper' and sys_inp == 'rock') or \
         (user_inp == 'scissors' and sys_inp == 'paper'):
        return "win"
    else:
        return "lose"

def play_round():
    options = ['rock', 'paper', 'scissors']
    user_inp = get_user_input()
    sys_inp = random.choice(options)

    result = determine_winner(user_inp, sys_inp)

    print(f"User input: {user_inp}")
    print(f"System input: {sys_inp}")

    if result == "draw":
        print("It's a draw")
    elif result == "win":
        print("You won")
    else:
        print("You lost")
    
    return result

def play_game():
    scores = {"wins": 0, "losses": 0, "draws": 0}
    
    while True:
        result = play_round()
        if result == "win":
            scores["wins"] += 1
        elif result == "lose":
            scores["losses"] += 1
        else:
            scores["draws"] += 1

        while True:
            play_again = input("Enter 'yes' to play again/'no' to end the game and view results: ").lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if play_again != 'yes':
            print("Thanks for playing!")
            print("Game Summary:")
            print(f"Wins: {scores['wins']}")
            print(f"Losses: {scores['losses']}")
            print(f"Draws: {scores['draws']}")
            break

if __name__ == "__main__":
    play_game()
