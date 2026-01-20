import random


# -------- VARIABLES --------
player_health = 100
player_gold = 20
game_running = True
shield_active = False

# Enemy list (boss is last)
enemies = [
    {"name": "Goblin", "health": 40, "boss": False},
    {"name": "Skeleton", "health": 50, "boss": False},
    {"name": "Orc", "health": 70, "boss": False},
    {"name": "Dragon (BOSS)", "health": 120, "boss": True}
]

# Inventory list
inventory = ["Potion"]

# -------- FUNCTIONS --------
def calculate_damage(min_dmg, max_dmg):
    """
    Returns a random damage value.
    """
    return random.randint(min_dmg, max_dmg)


def heal_player(health, amount):
    """
    Heals the player and returns updated health.
    """
    return min(health + amount, 100)


def show_status(enemy):
    """
    Displays player and enemy status.
    """
    print("\n--- STATUS ---")
    print("Player Health:", player_health)
    print("Gold:", player_gold)
    print("Enemy:", enemy["name"])
    print("Enemy Health:", enemy["health"])
    print("Inventory:", inventory)
    print("----------------\n")


def open_shop():
    """
    Allows the player to buy items between battles.
    """
    global player_gold

    print("\nSHOP OPEN")
    print("1. Potion (20 HP) - 10 gold")
    print("2. Mega Potion (40 HP) - 20 gold")
    print("3. Bomb - 15 gold")
    print("4. Shield - 15 gold")
    print("5. Leave shop")

    while True:
        print(f"\nYour Gold: {player_gold}")
        choice = input("Choose an item (1-5): ")

        if choice == "1":
            if player_gold >= 10:
                inventory.append("Potion")
                player_gold -= 10
                print("Potion purchased.")
            else:
                print("Not enough gold.")

        elif choice == "2":
            if player_gold >= 20:
                inventory.append("Mega Potion")
                player_gold -= 20
                print("Mega Potion purchased.")
            else:
                print("Not enough gold.")

        elif choice == "3":
            if player_gold >= 15:
                inventory.append("Bomb")
                player_gold -= 15
                print("Bomb purchased.")
            else:
                print("Not enough gold.")

        elif choice == "4":
            if player_gold >= 15:
                inventory.append("Shield")
                player_gold -= 15
                print("Shield purchased.")
            else:
                print("Not enough gold.")

        elif choice == "5":
            print("Leaving shop.")
            break

        else:
            print("Invalid choice.")

# -------- GAME INTRO --------
print("Welcome to the Text-Based RPG!")
print("Defeat all enemies and the boss to win.\n")

# -------- MAIN GAME LOOP --------
while game_running and enemies:

    current_enemy = enemies[0]

    # -------- BATTLE LOOP --------
    while current_enemy["health"] > 0 and player_health > 0:

        show_status(current_enemy)

        print("1. Attack")
        print("2. Use Item")
        print("3. Run")

        choice = input("Choose an action: ")

        # ----- PLAYER TURN -----
        if choice == "1":
            dmg = calculate_damage(8, 15)
            current_enemy["health"] -= dmg
            print(f"You dealt {dmg} damage.")

        elif choice == "2":
            print("Inventory:", inventory)
            item = input("Use which item? ").title()

            if item == "Potion" and item in inventory:
                player_health = heal_player(player_health, 20)
                inventory.remove(item)
                print("Healed 20 HP.")

            elif item == "Mega Potion" and item in inventory:
                player_health = heal_player(player_health, 40)
                inventory.remove(item)
                print("Healed 40 HP.")

            elif item == "Bomb" and item in inventory:
                dmg = calculate_damage(20, 35)
                current_enemy["health"] -= dmg
                inventory.remove(item)
                print(f"Bomb dealt {dmg} damage.")

            elif item == "Shield" and item in inventory:
                shield_active = True
                inventory.remove(item)
                print("Shield activated.")

            else:
                print("Invalid item or not in inventory.")

        elif choice == "3":
            print("You fled. Game Over.")
            game_running = False
            break

        else:
            print("Invalid choice.")

        # ----- ENEMY TURN -----
        if current_enemy["health"] > 0:
            enemy_dmg = calculate_damage(6, 16)

            if shield_active:
                enemy_dmg //= 2
                shield_active = False
                print("Shield reduced damage.")

            player_health -= enemy_dmg
            print(f"{current_enemy['name']} hit you for {enemy_dmg} damage.")

    # -------- CHECK PLAYER DEFEAT --------
    if player_health <= 0:
        print("\nYou were defeated. Game Over.")
        break

    # -------- ENEMY DEFEATED --------
    print(f"\nYou defeated {current_enemy['name']}.")
    gold_earned = random.randint(10, 20)
    player_gold += gold_earned
    print(f"You earned {gold_earned} gold.")

    enemies.pop(0)

    # -------- SHOP BETWEEN ENEMIES --------
    if enemies:
        open_shop()

# -------- GAME END --------
if player_health > 0 and not enemies:
    print("\nYOU DEFEATED THE BOSS AND WON THE GAME.")
    print("Final Gold:", player_gold)
    print("Final Inventory:", inventory)

print("\nThanks for playing!")
