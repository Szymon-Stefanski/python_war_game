import random

class Game(object):


    @staticmethod
    def create_user(username):
        print("Hello " + username)
        return username


    @staticmethod
    def game_interface():
        return input("What do you want to do?:"
                         "\n1.Add soldier to army"
                         "\n2.Sell soldier from army"
                         "\n3.Promote soldier"
                         "\n4.Check army"
                         "\n5.End turn."
                         "\n6.Capitulation.\n")


    @staticmethod
    def army_management():
        return input("\n1. Private - 10 gold"
              "\n2. Corporal - 20 gold"
              "\n3. Captain - 30 gold"
              "\n4. Sergeant - 40 gold"
              "\n5. Major - 50 gold"
              "\nWhat do you want to do?: ")


    @staticmethod
    def clear_screen():
        for i in range(1, 10):
            print("\n")


    def soldier_promote(arr):
        s_number = random.randint(0, len(arr) - 1)
        match arr[s_number]["rank"]:
            case "private":
                arr[s_number]["rank"] = "corporal"
                arr[s_number]["experience"] = 2
                print('Private has been promoted to Corporal!!!')

            case "corporal":
                arr[s_number]["rank"] = "captain"
                arr[s_number]["experience"] = 3
                print('Corporal has been promoted to Captain!!!')

            case "captain":
                arr[s_number]["rank"] = "sergeant"
                arr[s_number]["experience"] = 4
                print('Captain has been promoted to Sergeant!!!')

            case "sergeant":
                arr[s_number]["rank"] = "major"
                arr[s_number]["experience"] = 5
                print('Sergeant has been promoted to Major!!!')

            case "major":
                print("Already have the highest rank")

            case _:
                print("You don't have enough money!!!")


    def create_game(self):
        player1 = input("What is your name? [PLAYER 1]\n")
        self.create_user(player1)

        player2 = input("What is your name? [PLAYER 2]\n")
        self.create_user(player2)

        players = [player1, player2]

        person = 0
        turn = 1

        surrender = False

        soldier = None

        coins_one = 100
        coins_two = 100

        player_one = []
        player_two = []

        while turn < 11:
            print(f'\nTURN: {turn}')

            if person % 2 == 0:
                print("PLAYER:" + players[0])
                print(f'Your coins: {coins_one}')
            else:
                print("PLAYER:" + players[1])
                print(f'Your coins: {coins_two}')

            player_decision = self.game_interface()

            match player_decision:

                case "1":
                    self.clear_screen()
                    print("Add soldier to army:")
                    manage = self.army_management()
                    match manage:
                        case "1":
                            soldier = {"rank": "private", "experience": 1}
                            message = "Private has been added"
                        case "2":
                            soldier = {"rank": "corporal", "experience": 2}
                            message = "Corporal has been added"
                        case "3":
                            soldier = {"rank": "captain", "experience": 3}
                            message = "Captain has been added"
                        case "4":
                            soldier = {"rank": "sergeant", "experience": 4}
                            message = "Sergeant has been added"
                        case "5":
                            soldier = {"rank": "major", "experience": 5}
                            message = "Major has been added"
                        case _:
                            print("Please, choose again.")
                            continue
                    if soldier:
                        if person % 2 == 0:
                            if coins_one >= 10 * int(manage):
                                player_one.append(soldier)
                                print(message)
                                coins_one -= 10 * int(manage)
                            else:
                                print("You don't have enough money!!!")
                        else:
                            if coins_two >= 10 * int(manage):
                                player_two.append(soldier)
                                print(message)
                                coins_two -= 10 * int(manage)
                            else:
                                print("You don't have enough money!!!")
                    continue

                case "2":
                    self.clear_screen()
                    print("Sell soldier from army:")
                    manage = self.army_management()
                    match manage:
                        case "1":
                            soldier = {"rank": "private", "experience": 1}
                            message = "Private has been sold"
                        case "2":
                            soldier = {"rank": "corporal", "experience": 2}
                            message = "Corporal has been sold"
                        case "3":
                            soldier = {"rank": "captain", "experience": 3}
                            message = "Captain has been sold"
                        case "4":
                            soldier = {"rank": "sergeant", "experience": 4}
                            message = "Sergeant has been sold"
                        case "5":
                            soldier = {"rank": "major", "experience": 5}
                            message = "Major has been sold"
                        case _:
                            print("Please, choose again.")
                            continue
                    if soldier:
                        if person % 2 == 0:
                            if soldier in player_one:
                                player_one.remove(soldier)
                                print(message)
                                coins_one += 10 * int(manage)
                            else:
                                print('There isn''t a soldier with that rank in your army!!!')
                        else:
                            if soldier in player_two:
                                player_two.remove(soldier)
                                print(message)
                                coins_two += 10 * int(manage)
                            else:
                                print('There isn''t a soldier with that rank in your army!!!')
                    continue

                case "3":
                    self.clear_screen()
                    print("Promote soldiers")
                    if soldier:
                        if person % 2 == 0 and coins_one >= 50:
                            self.soldier_promote(player_one)
                            coins_one -=50
                        else:
                            self.soldier_promote(player_two)
                            coins_two -=50
                    continue

                case "4":
                    self.clear_screen()
                    print("Check army")
                    if person % 2 == 0:
                        for soldier in player_one:
                            print(f"{soldier['rank']}, Experience: {soldier['experience']}")
                    else:
                        for soldier in player_two:
                            print(f"{soldier['rank']}, Experience: {soldier['experience']}")
                    continue
                case "5":
                    self.clear_screen()
                    person = 1 - person
                    if person == 0:
                        turn += 1
                        coins_one += 10
                        coins_two += 10
                    continue

                case "6":
                    self.clear_screen()
                    print(f"{players[person]} surrenders! {players[1 - person]} wins!")
                    surrender = True
                    break

                case _:
                    print("Please, choose again.")

        save = input("Do you want save your result? [Y/N]")
        self.clear_screen()
        if save in ('Y','y'):
            with open('results.txt', 'a') as fileObj:
                if coins_one > coins_two and surrender == False:
                    fileObj.write(f'Winner is: {player1} , and he wins with score: {coins_one}\n')
                    print("Player 1 wins!")
                elif coins_one < coins_two and surrender == False:
                    fileObj.write(f'Winner is: {player2} , and he wins with score: {coins_two}\n')
                    print("Player 2 wins!")
                elif coins_one == coins_two and surrender == False:
                    print("Draw!")
                    fileObj.write('Nobody wins!\n')
        else:
            if coins_one > coins_two and surrender == False:
                print("Player 1 wins!")
            elif coins_one < coins_two and surrender == False:
                print("Player 2 wins!")
            elif coins_one == coins_two and surrender == False:
                print("Draw!")

        print("Thank you for playing!")


game = Game()
new_game = game.create_game()