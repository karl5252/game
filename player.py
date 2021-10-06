import items
import world


class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.BronzeAxe(),
                          "Gold(5)",
                          "Crusty bread"]
        self.x = 1
        self.y = 1
        self.hp = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("YOu use {} against {}!".
              format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy hits you! Received {} damage! {} remaining...".format(self.enemy.damage, player.hp))


    def print_player_inventory(self):
        print(f"Inventory: \n")
        for item in enumerate(self.inventory):
            print(f" {chr(149)} {str(item)}")
        most_weapon = self.most_powerful_weapon()
        print(f"\n your best weapon you have is {most_weapon}")

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon
