def create_user(username):
    print("Hello " + username)


def game_interface():
    return input("What do you want to do?:"
                     "\n1.Add soldier to army"
                     "\n2.Sell soldier from army"
                     "\n3.Order maneuvers"
                     "\n4.Check army"
                     "\n5.Do you want to end turn?: [Y / N / Q]\n")


def army_management():
    return input("\n1. Private - 10 gold"
          "\n2. Corporal - 20 gold"
          "\n3. Captain - 30 gold"
          "\n4. Sergeant - 40 gold"
          "\n5. Major - 50 gold"
          "\nWhat do you want to do?: ")


def create_game():
    player1 = input("What is your name? [PLAYER 1]\n")
    create_user(player1)

    player2 = input("What is your name? [PLAYER 2]\n")
    create_user(player2)

    players = [player1, player2]

    p = 0
    i = 1

    surrender = False

    soldier = None

    coins_one = 100
    coins_two = 100

    player_one = []
    player_two = []

    while i < 11:
        print("\nTURN: ")
        print(i)

        if p % 2 == 0:
            print("PLAYER:" + players[0])
            print(coins_one)
        else:
            print("PLAYER:" + players[1])
            print(coins_two)

        player_decision = game_interface()

        match player_decision:
            case "1":
                print("Add soldier to army:")
                manage = army_management()
                match manage:
                    case "1":
                        soldier = {"rank": "private", "experience": 1}
                        print("Private was added")
                    case "2":
                        soldier = {"rank": "corporal", "experience": 2}
                        print("Corporal was added")
                    case "3":
                        soldier = {"rank": "captain", "experience": 3}
                        print("Captain was added")
                    case "4":
                        soldier = {"rank": "sergeant", "experience": 4}
                        print("Sergeant was added")
                    case "5":
                        soldier = {"rank": "major", "experience": 5}
                        print("Major was added")
                    case _:
                        print("Please, choose again.")
                        continue
                if soldier:
                    if p % 2 == 0:
                        player_one.append(soldier)
                        coins_one -= 10 * int(manage)
                    else:
                        player_two.append(soldier)
                        coins_two -= 10 * int(manage)
                continue
            case "2":
                print("Sell soldier from army:")
                manage = army_management()
                match manage:
                    case "1":
                        soldier = {"rank": "private", "experience": 1}
                    case "2":
                        soldier = {"rank": "corporal", "experience": 2}
                    case "3":
                        soldier = {"rank": "captain", "experience": 3}
                    case "4":
                        soldier = {"rank": "sergeant", "experience": 4}
                    case "5":
                        soldier = {"rank": "major", "experience": 5}
                    case _:
                        print("Please, choose again.")
                        continue
                if soldier:
                    if p % 2 == 0:
                        player_one.remove(soldier)
                    else:
                        player_two.remove(soldier)
                continue
            case "3":
                print("Order maneuvers")
                continue
            case "4":
                print("Check army")
                if p % 2 == 0:
                    for soldier in player_one:
                        print(f"Rank: {soldier['rank']}, Experience: {soldier['experience']}")
                else:
                    for soldier in player_two:
                        print(f"Rank: {soldier['rank']}, Experience: {soldier['experience']}")
                continue
            case "Y" | "y":
                p = 1 - p
                if p == 0:
                    i += 1
                    coins_one += 10
                    coins_two += 10
                continue
            case "N" | "n":
                print("You can make another choice.")
                continue
            case "Q" | "q":
                print(f"{players[p]} surrenders! {players[1 - p]} wins!")
                surrender = True
                break
            case _:
                print("Please, choose again.")

    print("Thank you for playing!")

    if coins_one > coins_two and surrender == False:
        print("Player 1 wins!")
    elif coins_one < coins_two and surrender == False:
        print("Player 2 wins!")
    elif coins_one == coins_two and surrender == False:
        print("Draw!")

new_game = create_game()
