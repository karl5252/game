class Weapon:
    def __init__(self):
        raise NotImplementedError("Do nor create raw objects")

    def __repr__(self):
        return f"{self.name}- {self.description}"


class Rock(Weapon):
    def __init__(self):
        self.name = "Fistful of Rock"
        self.description = "Fist sized chunk of ordinary, grey rock perfect to bash brains through ears"
        self.damage = 5
        self.durability = 8


class Dagger(Weapon):
    def __init__(self):
        self.name = "Simple Shiv"
        self.description = "A small dagger made out of a bashed flat metal rod or sharpened spoon"
        self.damage = 10
        self.durability = 10


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "This blade has seen better days"
        self.damage = 20
        self.durability = 16


class BronzeAxe(Weapon):
    def __init__(self):
        self.name = "Bronze axe"
        self.description = "Crude axe made from bronze with darker spots on the blade..."
        self.damage = 24
        self.durability = 20
