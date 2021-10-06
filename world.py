import random

import enemies


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("raise a subclass instead")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
        You wake up on a glassy, uneven floor. \n Distant lights are flickering on semi- opaque walls made 
        of the same glass like material.\n Once your eyes adjust to the surrounding darkness you notice four dank 
        corridors\n stretching in four different directions. WHhich path you will take...
        """


class BoringTile(MapTile):
    def intro_text(self):
        return """
        Boring! Nothing to see here! Go away!\n
        (was that squeaky voice in your mind or somebody said this from under your feet?)
        """


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You feel fresh breeze on your face so refreshing after dull and stale air of the caves\n
        you run with outstretched hands for freedom is so painfully near\n
        does it get lighter with every step or this is just an illusion?\n
        you turn after the corner and you have to close your eyes\n for the light of setting sun is too much for your
        hungry for brightness eyes\n after so long time spent in the dull underground caverns of the Dimberg,
         the Blue Mountain. 
        """


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GlassSpider()
            self.alive_text = "You heard a scratching noise for some time " \
                              " but now you are certain... It is a giant spider but it body is covered in glassy armor!"
            self.dead_text = "Spider body cracks and crumbles into fine glass powder... " \
                             "Was there anything organic about that monster?"
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = "With a terrifying roar half crazed ogre rushes at you! Watch out for his sharp teeth! " \
                              "And...is it a stalagmite he has in his hand?"
            self.dead_text = "Ogre finally falls to his knees and you fell tremor of his fall. Beast`s eyes in last" \
                             " moments of live flash with hidden intelligence. " \
                             "And you wonder how long that monster spent in those dungeons?"
        elif r < 0.95:
            self.enemy = enemies.GlassBatSwarm()
            self.alive_text = "A sound can be heard like leaves rushing on the wind or maybe" \
                              " tiny icicles tossed on stone? THen you hear shrilling squeaks... Bats!"
            self.dead_text = "Last of the beasts finally falls to the ground only to break into tiny pieces" \
                             " like piece of precious crystal"
        else:
            self.enemy = enemies.GlassGolem()
            self.alive_text = "This lumbering form you passed by just moments ago was one giant piece of glassy rock..." \
                              " Not anymore! Giant made of glassy rock with arms and legs thick enough" \
                              " to serve as a column of some ancient temple"
            self.dead_text = "Sound of cracking thick ice is what gave it up. Giant is still trying to fight " \
                             "but his form slowly crumbles to pieces. " \
                             "Seems the glassy form resembled more of a geode..."

        super().__init__(x, y)ąą

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return "A {} awaits!.".format(self.enemy.name)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP left".format(self.enemy.damage, player.hp))

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None


world_map = [
    [None, VictoryTile(1, 0), None],
    [None, BoringTile(1, 1), None],
    [EnemyTile(0, 2), StartTile(1, 2), EnemyTile(2, 2)],
    [None, EnemyTile(1, 3), None]
]
