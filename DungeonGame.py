# Simple Text Adventure: Azog in the Dungeon

COMMAND_LIST = ["north", "east", "south", "west", "inventory", "help", "quit"]

# Room graph and item placement
ROOMS = {
    "Great Hall": {"west": "West Tower", "east": "East Tower", "south": "Dungeon"},
    "East Tower": {"west": "Great Hall", "south": "Barracks", "item": "Shield"},
    "Barracks": {"west": "Dungeon", "north": "East Tower", "south": "Library", "item": "Armor"},
    "Library": {"west": "Bedroom", "north": "Barracks"},
    "Bedroom": {"west": "Stables", "east": "Library", "north": "Dungeon", "item": "Sword"},
    "Stables": {"north": "Kitchen", "east": "Bedroom", "item": "Bow"},
    "Kitchen": {"north": "West Tower", "south": "Stables", "east": "Dungeon", "item": "Torch"},
    "West Tower": {"south": "Kitchen", "east": "Great Hall", "item": "Arrows"},
    "Dungeon": {"north": "Great Hall", "east": "Barracks", "south": "Bedroom", "west": "Kitchen"},
}

ALL_ITEMS = {"Shield", "Armor", "Sword", "Bow", "Torch", "Arrows"}


def main_menu():
    while True:
        print("*" * 99)
        print("* Welcome, Hero! The great and terrible spider Azog has infiltrated the dungeon of your castle!   *")
        print("* You must navigate through your castle, finding SIX items to defeat the foul beast.               *")
        print("* Be careful... entering the dungeon before you have all items means certain doom!                 *")
        print("* Please choose an option:                                                                         *")
        print("* 1) Begin game                                                                                     *")
        print("* 2) View list of commands                                                                          *")
        print("* 3) Quit                                                                                           *")
        print("*" * 99)

        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            print(f"\nValid commands: {', '.join(COMMAND_LIST)}\n"
                  "Move with north/east/south/west, type 'inventory' to view items, 'help' to see commands, 'quit' to exit.\n")
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.\n")


def play_game():
    current_room = "Great Hall"
    inventory = []

    print("\nYour quest begins in the Great Hall. Gather all six items before confronting Azog in the Dungeon!")
    print("Type 'help' for commands.\n")

    while True:
        print(f"You are in the {current_room}.")
        # Offer item if present and not already collected
        offer_item_if_present(current_room, inventory)

        # Entering the Dungeon triggers win/lose resolution
        if current_room == "Dungeon":
            if resolve_dungeon(inventory):
                print("Congratulations! The castle is safe once again. Thank you, hero.\n")
            else:
                print("Better luck next time.\n")
            # After outcome, return to main menu
            return

        cmd = input("Your move (north/east/south/west, inventory, help, quit): ").strip().lower()

        if cmd in ("quit", "q"):
            print("Goodbye!")
            return
        elif cmd in ("help", "h"):
            print(f"Commands: {', '.join(COMMAND_LIST)}")
        elif cmd in ("inventory", "i"):
            show_inventory(inventory)
        elif cmd in ("north", "south", "east", "west"):
            next_room = ROOMS[current_room].get(cmd)
            if next_room:
                current_room = next_room
            else:
                print("You can't go that way.\n")
        else:
            print("Invalid command. Type 'help' to see options.\n")


def offer_item_if_present(current_room, inventory):
    """If the room has an item and you don't already have it, prompt to pick it up."""
    room_info = ROOMS.get(current_room, {})
    item = room_info.get("item")
    if item and item not in inventory:
        while True:
            choice = input(f"You see a {item}! Pick it up? (y/n): ").strip().lower()
            if choice == "y":
                inventory.append(item)
                print(f"{item} added to your inventory.")
                show_inventory(inventory)
                print()
                return
            elif choice == "n":
                print(f"You leave the {item} where it lies.\n")
                return
            else:
                print("Please enter 'y' or 'n'.")


def show_inventory(inventory):
    if inventory:
        print(f"Inventory ({len(inventory)}/6): {', '.join(inventory)}")
    else:
        print("Inventory is empty.")


def resolve_dungeon(inventory):
    """Return True if player wins, False if loses, based on inventory."""
    print("\nRumble... Rumble...")
    print("Azog charges you!")

    have_all = set(inventory) >= ALL_ITEMS
    if not have_all:
        print("You failed to collect all the items and are gruesomely eaten!")
        return False

    # Flavor text when fully equipped
    print("You blind him with the Torch and block his attack with your Shield!")
    print("You strike with your Sword; Azog begins to flee!")
    print("You slow him with your Bow and finish the beast with a volley of Arrows!")
    return True


if __name__ == "__main__":
    main_menu()
