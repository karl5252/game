class Enemy:

    def __init__(self):
        raise NotImplementedError("implement as sub objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class GlassSpider(Enemy):
    def __init__(self):
        self.name = "Glass spider"
        self.hp = 10
        self.damage = 8


class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 15


class GlassBatSwarm(Enemy):
    def __init__(self):
        self.name = "Swarm of Giant Glass bats"
        self.hp = 10
        self.damage = 5


class GlassGolem(Enemy):
    def __init__(self):
        self.name = "Glass golem"
        self.hp = 85
        self.damage = 90