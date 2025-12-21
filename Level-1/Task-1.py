# Treasure Escape Challenge
import random

def intro():
    print("🏴‍☠️ Welcome to the Treasure Escape Challenge!")
    print("You are trapped inside a mysterious cave with 3 tunnels.")
    print("One tunnel has treasure 💰")
    print("One tunnel has a monster 👹")
    print("One tunnel leads to the exit 🔓")
    print("Choose carefully... your fate depends on it!\n")

def choose_tunnel():
    while True:
        choice = input("Choose a tunnel (1, 2, or 3): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

def reveal_result(player_choice, treasure, monster, exit_tunnel):
    print("\nYou slowly walk inside tunnel", player_choice, "...")
    
    if player_choice == treasure:
        print("💰 Congratulations! You found a huge treasure chest! You win!")
    elif player_choice == monster:
        print("👹 Oh no! A monster appeared! You lost!")
    elif player_choice == exit_tunnel:
        print("🔓 You found the hidden escape route! You safely exit the cave. Well done!")
    print("\nGame Over.\n")

def main():
    while True:
        intro()
        
        # random tunnel positions
        tunnels = [1, 2, 3]
        treasure = random.choice(tunnels)
        monster = random.choice([t for t in tunnels if t != treasure])
        exit_tunnel = [t for t in tunnels if t not in (treasure, monster)][0]

        # player chooses
        player_choice = choose_tunnel()

        # result
        reveal_result(player_choice, treasure, monster, exit_tunnel)

        # replay option
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing the Treasure Escape Challenge! Goodbye 👋")
            break

if __name__ == "__main__":
    main()