def create_user(username):
    print("Hello " + username)

def decision():
    return input("What do you want to do?:"
                     "\n1.Add soldier to army"
                     "\n2.Sell soldier from army"
                     "\n3.Order maneuvers"
                     "\n4.Check army"
                     "\n5.Do you want to end turn?: [Y / N / Q]\n")

soldiers = [
    {"rank": "private", "experience": 1},
    {"rank": "corporal", "experience": 2},
    {"rank": "captain", "experience": 3},
    {"rank": "sergeant", "experience": 4},
    {"rank": "major", "experience": 5}
]

def game():
    player1 = input("What is your name? [PLAYER 1]\n")
    create_user(player1)

    player2 = input("What is your name? [PLAYER 2]\n")
    create_user(player2)

    players = [player1, player2]

    p = 0
    i = 1

    while i < 11:
        print("\nTURN: ")
        print(i)

        if p % 2 == 0:
            print("PLAYER:" + players[0])
        else:
            print("PLAYER:" + players[1])

        player_decision = decision()

        match player_decision:
            case "1":
                print("Add soldier to army: ")
                continue
            case "2":
                print("Option 2")
                continue
            case "3":
                print("Option 3")
                continue
            case "4":
                print("Option 4")
                continue
            case "Y" | "y":
                p = 1 - p
                if p == 0:
                    i += 1
                continue
            case "N" | "n":
                print("You can make another choice.")
                continue
            case "Q" | "q":
                print(f"{players[p]} surrenders! {players[1 - p]} wins!")
                break
            case _:
                print("Please, choose again.")

    print("Thank you for playing!")

new_game = game()