class Monster:

    def __init__(self, health, energy, name = 'The Monster', **kwargs):
        # print(kwargs)
        self.health = health
        self.energy = energy
        self.name = name
        super().__init__(**kwargs)

    def update_energy(self, amount):
        self.energy += amount

    def get_damage(self, amount):
        self.health -= amount

    def attack(self, amount):
        print(f'The {self.name} has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print(f'The {self.name} has moved')
        print(f'It has a speed of {speed}')

class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        # print(kwargs)
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)


    def swim(self):
        print(f'The fish is swimming at speed of {self.speed}')



class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales, **kwargs):
        self.bite_strength = bite_strength
        super().__init__(
            health = health,
            energy = energy,
            name = 'Shark',
            speed = speed,
            has_scales = has_scales,
            **kwargs)


    def bite(self):
        print(f'The {self.name} has bitten')

    def attack(self):
        print(f'The {self.name} has attacked!')
        print(f'{self.bite_strength} damage was dealt')
        self.energy -= 20

class Scorpion(Monster):
    def __init__(self, health, energy, poison_damage, **kwargs):
        self.poison_damage = poison_damage
        super().__init__(
            health = health,
            energy = energy,
            name = 'Scorpion', **kwargs)

    def attack(self):
        print(f'The {self.name} has attacked!')
        print(f'{self.poison_damage} poison damage was dealt')
        self.energy -= 20


class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)


monster = Monster(health = 100, energy = 50)
print(monster.energy)
monster.attack(10)

# hero = Hero(2, monster)
# hero.attack()
# print(monster.health)


shark = Shark(
    bite_strength = 30,
    health = 100,
    energy = 80,
    speed = 120,
    has_scales = True)
print(shark.speed)
shark.attack()
shark.move(40)

scorpion = Scorpion(health = 60, energy = 120, poison_damage = 8)
scorpion.attack()
scorpion.move(5)