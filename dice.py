'''The aim of Dice Rolling Game is for a player to roll 2-6 dice multiple times in each game. 
Victory is achieved when the median value is the same as the mean value in a result list of the dice rolls for all rounds of the game.
The game starts by letting the player choose a number of dice to play with and also choose the type of dice that they want to use. 
Player’s roll the dice multiple times, and based on the results, either win or lose.
Your task is to write functions to display the main menu, a game menu, as well as other functionalities to check the game history and the win/lose status.'''


# 1. Main menu function

import random

# Global empty list which will store all the result of roll dice function
game_history_results = []


def main_menu():
    """
    Show user the options to play the dice roll game

    This function gives 3 options to user
    Start game
    Game History and
    Exit

    Parameters
    ----------
    No Parameter

    """
    print("________________________________MAIN MENU__________________________________\n")

    # Asked user to input a valid option
    print("Options : \n 1: Start game \n 2: Game History \n 3: EXIT ")


# 2. Game menu function

def game_menu():
    """
        Show user the options after starting the  dice roll game

        This function gives 3 options to user
        Number of dice - user select number of dices between 2 to 6 to roll
        Type of Dice - user select the type of dice 6 , 8 or 9
        Roll Dice - It will give out the result tuple of number of dice and type of dice
        Check win or Lose - Win or lose based on mean and median of tuple
        Exit - exit the round

        NOTE:  If user wants to play multiple round then first he need to start with option 1 then 2 and then 3 . After
        that user has to exit ( option 5) and start with option 1 ,2 and 3 . after only he can choose option 4

        Parameters
        ----------
        No Parameter

        """

    print("\n--------------Game-Menu--------------")

    # Asked user to input a valid option
    print("1. Select the Number of Dice to roll\n2. Select the Type of Dice you want to roll(6,8 or 9)\n3. Roll Dice\n4. Check Win/Lose\n 5.Exit Game")


# 3. Roll dice function

def roll_dice(dice_count, type_of_dice):
    """

    Roll dice function takes 2 parameters .i.e Number of dice and type of dice.
    then it iterate total number of dice and select random values from the type of dice.

    Here we have used ascii art to print the result of each roll

    Parameters
    ----------

    2 parametes

    number of dice : int
        total number of dice selected

    type of dice : int
        choose random value from dice types

    Returns
    --------

    tuple
        contains result of the roll dice func

    Example
    ---------
        number of dice = 2
        type of dice = 6
        roll dice(2,6)
            tuple = (1,2)



    """

    dice_type_6 = [1, 2, 3, 4, 5, 6]
    dice_type_8 = [2, 2, 3, 3, 4, 8]
    dice_type_9 = [1, 1, 1, 1, 5, 9]

    dice_image_dict = {1: ''' 
                ---------
                |       |
                |   o   |
                |       |
                --------- 
         ''', 2: """

        ---------
        |       |
        | o   o |
        |       |
        ---------

        """, 3: """

            ---------
            | o     |
            |   o   |
            |     o |
            ---------

            """, 4: """

            ---------
            | o   o |
            |       |
            | o   o |
            ---------

            """, 5: """

            ---------
            | o   o |
            |   o   |
            | o   o |
            ---------

            """, 6: """

            ---------
            | o   o |
            | o   o |
            | o   o |
            ---------

            """, 8: """

                ---------
                | o o o |
                | o   o |
                | o o o |
                ---------

                """, 9: """

                ---------
                | o o o |
                | o o o |
                | o o o |
                ---------

                """}

    # Empty list to store the random values
    result = []

    for item in range(dice_count):
        if type_of_dice == 6:
            # selecting a random value from type 6 dice and storing
            store = random.choice(dice_type_6)
            if store in dice_image_dict.keys():
                print(dice_image_dict[store])           # printing ascii art
            result.append(store)
        if type_of_dice == 8:
            # selecting a random value from type 8 dice and storing
            store = random.choice(dice_type_8)
            if store in dice_image_dict.keys():
                print(dice_image_dict[store])           # printing ascii art
            result.append(store)
        if type_of_dice == 9:
            # selecting a random value from type 9 dice and storing
            store = random.choice(dice_type_9)
            if store in dice_image_dict.keys():
                print(dice_image_dict[store])           # printing ascii art
            result.append(store)

    # converting result list into a tuple
    dice_result_list = tuple(result)
    print(dice_result_list)

    # appending every value of dice_result_list in global empty list game_history_results
    game_history_results.append(dice_result_list)
    return dice_result_list


# 4. Check win/lose function


def check_win_lose(item):
    """

    Check_win_lose function checks user won the game or lost the game based on the mean and median of the tuple values
    if mean == median then its a win or else its a loss

    Prameter
    ---------
    take one input parameter global empty list x
         x : list

    :returns
    ---------

    return win or loss
    """

    # if number of round is greater than 10 then loss
    if len(item) > 10:
        return "Loss"
    else:
        # unpacking the list of tuple game_history_results
        y = []
        for x in item:
            for sun in x:
                y.append(sun)
        dice = sorted(y)
        print(dice)
        sum = 0
        n = len(dice) // 2
        for i in dice:
            sum = sum + i
        print(sum)

        # mean value
        mean = sum / len(dice)

        # median of the unpacked list . CREDIT : took help from GeeksforGeeks regarding this code line 227
        # used negation or ~ (tilda) operator
        median = (dice[n] + dice[~n]) / 2
        print(median)
        print(mean)

        if mean == median:
            print("WIN")
            return "WIN"
        else:
            print("LOSS")
            return "Loss"


# 5. Game history function


def game_history(num1, num2, num3):
    """

     Game History function return about the number of dice , rounds count and Win or Lose result from check win or
     lose function
    """

    print(f"Number of dice {num1} round {num2} result {num3}")


# 6. Main function

def main():
    """

    Main function where all control structure and functions calling is implemented

    """
    print("\n                         Welcome to ROLL DICE GAME                       \n")
    count = 0                       # Will count how many round has been played
    while True:
        main_menu()                 # main_menu function has been called
        # variable to take option
        selected_option = int(input(" Please choose an option : "))
        if selected_option == 1:
            # initially number of dice are 0
            number_of_dices = 0
            # initially dice type is 0
            select_dice_type = 0
            while True:
                game_menu()         # game_menu function has been called
                # variable to take option
                options = int(input("Please select option : "))
                if options == 1:
                    # input for number of dice
                    number_of_dices = int(
                        input("Please enter the number of dices you want to roll : "))
                    while number_of_dices not in range(2, 7):
                        print(
                            "\nThe number you entered is not within the allowed range.")
                        number_of_dices = int(
                            input("Please enter the number of dices ( in range ) you want to roll : "))
                    print(
                        "\nNumber of Dice has been selected. Please choose option 2 to select dice type")
                elif options == 2:
                    # input for dice type
                    select_dice_type = int(
                        input("Enter the Type of Dice ( 6,8 or 9): "))
                    while (not (select_dice_type == 6 or select_dice_type == 8 or select_dice_type == 9)):
                        print(
                            "\nThe number you entered is not among the allowed choices.")
                        select_dice_type = int(
                            input("Please input the valid choice:"))
                    print(
                        "\nDice type has been selected. Please choose option 3 to roll dice")
                elif options == 3:
                    if (number_of_dices != 0 and select_dice_type != 0):
                        # Roll Dice function has been called
                        roll_dice(number_of_dices, select_dice_type)
                    else:
                        print(
                            "Please enter the number and type of dice before rolling the dice.")
                    print("\nDice has been rolled. If you want to roll another round select option 5 exit and start again. If ou done rolling select option 4")
                elif options == 4:
                    print(game_history_results)

                    # Check win lose function has been called and store in variable z
                    z = check_win_lose(game_history_results)
                elif options == 5:
                    count += 1                          # If user exit then counter value is increased by one
                    print("Thank you for playing!!")
                    break
                else:
                    print("Wrong value entered, Please Choose Again!")
        elif selected_option == 2:
            # Game history function has been called, took 3 parameters
            return game_history(number_of_dices, count, z)
        elif selected_option == 3:
            print("Goodbye")
            # If user exit the game then game exit
            break
        else:
            print("PLease enter a valid choice")
            return main_menu()


main()
