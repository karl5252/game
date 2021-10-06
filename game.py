import world
from player import Player


def play():
    print("escape from blue mountains")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        action_input = get_player_command()
        if action_input in ['N', 'n', '^']:
            player.move_north()
        elif action_input in ['S', 's']:
            player.move_south()
        elif action_input in ['E', 'e', '>']:
            player.move_east()
        elif action_input in ['W', 'w', '<']:
            player.move_west()
        elif action_input in ['I', 'i']:
            player.print_player_inventory()
        elif action_input in ['A', 'a']:
            player.attack()
        elif action_input == "exit":
            break
        else:
            print("Invalid action!")


def get_player_command():
    return input('Action: ')


play()
