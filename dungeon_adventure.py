import random
import sys

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        player_name = input("What is your name? \n")
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        player_info = {
            "name": player_name, 
            "health": 10, 
            "inventory": []
                    }
        # TODO: Return the dictionary
        return player_info
        print(player_info)


    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        treasures = {
            "green rupee": 1,
            "blue rupee": 5,
            "red rupee": 20,
            "skulltula": random.randint(3, 25),
            "bottled fairy": random.randint(3, 25),
            "master sword": 50
        }
        # TODO: Return the dictionary
        return treasures

    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above
        print(f"You are in room number {room_number}. \n")
        print("What would you like to do? \n")
        print("1. Search for treasure \n ")
        print("2. Move to next room \n")
        print("3. Check health and inventory \n") 
        print("4. Quit the game \n")

    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        outcome_list = ["treasure", "trap"]
        outcome_chosen = random.outcome(outcome_list)

        # TODO: Write an if/else to handle treasure vs trap outcomes
        if outcome_chosen == "treasure":
            random_treasure = setup_player.player_info["inventory"].append(random.treasure(treasures))
            print(f"{setup_player.player_name} found {random_treasure}!")
        else:
            setup_player.player_info["health"] -= 2
            print(f"{setup_player.player_name} loss 2 health!")
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened


    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        print(f"Player {setup_player.player_name} has: \n")
        print(f"Health: {setup_player.player_info["health"]} \n")
        if setup_player.player_info["inventory"] != "":
            inventory_to_print = setup_player.playerinfo["inventory"]
            print(f"Inventory: {'. '.join(inventory_to_print)} \n")
        else:
            print(f"Inventory: You have no items yet.\n")
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        treasures_obtained = setup_player.player_info["inventory"]
        treasure_value = 0
        for treasure_obtained in treasures_obtained:
            if treasures.keys == treasure_obtained:
                sum(treasures.values + treasure_value)
            else:
                continue
        # TODO: Print final health, items, and total value
        print(f"{setup_player.player_name} has:") 
        print(f"{setup_player.player_info["health"]} health")
        if setup_player.player_info["inventory"] != "":
            inventory_to_print = setup_player.playerinfo["inventory"]
            print(f"Inventory: {'. '.join(inventory_to_print)} \n")
        else:
            print(f"Inventory: You collected no items.\n")
        print(f"And total value of items is: {treasure_value}. \n")
        # TODO: End with a message like "Game Over! Thanks for playing."
        print("Thanks for playing!!")

    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        for rooms in range(1, 6):
            player_choice_input = input(display_options(room_number= rooms))
            if player_choice_input == 1:
                search_room(player, treasures)
            elif player_choice_input == 3:
                check_status(player)
            elif player_choice_input == 4:
                sys.exit()
            elif setup_player.player_info["health"] <= 0:
                print("You have died. Please try again.")
                sys.exit()
            elif player_choice_input == 2:
                continue
            else:
                print("Invalid option. ")
                print(display_options(room_number=rooms))
        end_game(player, treasures)
        sys.exit()

        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
