import random
import time

class Player:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        actual_dmg = max(1, dmg - random.randint(0, self.defense))
        self.hp = max(0, self.hp - actual_dmg)
        return actual_dmg

    def heal(self):
        amount = random.randint(15, 30)
        self.hp = min(self.max_hp, self.hp + amount)
        return amount

def print_status(p1, p2):
    print(f"\n--- STATUS ---")
    print(f"{p1.name}: HP {p1.hp}/{p1.max_hp}")
    print(f"{p2.name}: HP {p2.hp}/{p2.max_hp}")
    print("-" * 14)

def player_turn(player, opponent):
    print(f"\n>> {player.name}'s turn! Choose action:")
    print("1. Attack")
    print("2. Heal")
    
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice in ['1', '2']:
            break
        print("Invalid choice.")
        
    if choice == '1':
        base_dmg = random.randint(10, player.attack)
        dealt = opponent.take_damage(base_dmg)
        print(f"💥 {player.name} attacks {opponent.name} for {dealt} damage!")
    else:
        healed = player.heal()
        print(f"💖 {player.name} heals for {healed} HP!")

def ai_turn(ai, opponent):
    print(f"\n>> {ai.name}'s turn (AI)...")
    time.sleep(1)
    
    if ai.hp < 30 and random.random() < 0.7:
        healed = ai.heal()
        print(f"💖 {ai.name} decides to heal for {healed} HP!")
    else:
        base_dmg = random.randint(10, ai.attack)
        dealt = opponent.take_damage(base_dmg)
        print(f"💥 {ai.name} strikes {opponent.name} for {dealt} damage!")

def main():
    print("====================================")
    print("   WELCOME TO TEXT-BASED RPG DUEL   ")
    print("====================================")
    
    p_name = input("Enter your hero's name: ").strip() or "Hero"
    hero = Player(p_name, hp=100, attack=25, defense=8)
    boss = Player("Shadow Boss", hp=120, attack=22, defense=10)
    
    turn = 1
    while hero.is_alive() and boss.is_alive():
        print(f"\n=== ROUND {turn} ===")
        print_status(hero, boss)
        
        player_turn(hero, boss)
        if not boss.is_alive():
            break
            
        print_status(hero, boss)
        ai_turn(boss, hero)
        turn += 1
        
    print("\n====================================")
    if hero.is_alive():
        print(f"🎉 VICTORY! {hero.name} defeated the {boss.name}!")
    else:
        print(f"💀 DEFEAT! {boss.name} defeated {hero.name}...")
    print("====================================")

if __name__ == "__main__":
    main()
