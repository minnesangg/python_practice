class Character:
    max_level = 3

    def __init__(self, *, level: int) -> None:
        self.level = level
        self.update_stats()

    def update_stats(self) -> None:
        self.health = self.base_health * self.level
        self.attack = self.base_attack * self.level

    def attacking(self, *, target: "Character") -> None:
        target.got_damage(damage = self.attack)

    def got_damage(self, *, damage: int) -> None:
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)
        self.health -= damage

    @property
    def defence(self) -> int:
        defence = self.base_defence * self.level
        return defence

    @property
    def max_health(self) -> int:
        return self.level * self.base_health

    def health_precents(self):
        return 100 * self.health / self.max_health

    def is_alive(self):
        return self.health > 0

    def is_not_max_level(self):
        return self.level < self.max_level

    def is_max_level(self):
        return self.level >= self.max_level

    def __str__(self):
        return f"{self.character_name} level: {self.level}, health: {self.health}"


class Orc(Character):
    base_health = 100
    base_attack = 10
    base_defence = 15
    character_name = 'Orc'

    @property
    def defence(self) -> int:
        defence = super().defence
        if self.health < 50:
            defence *= 3
        return defence

class Elf(Character):
    base_health = 650
    base_attack = 15
    base_defence = 10
    character_name = 'Elf'

    def attacking(self, *, target: "Character") -> None:
        attack = self.attack
        if target.health_precents() < 30:
            attack = self.attack * 3
        target.got_damage(damage = attack)


def fight(*, character_1: Character, character_2: Character) -> None:
    base_health1 = character_1.health
    base_health2 = character_2.health
    while True:
        character_1.attacking(target = character_2)
        if character_2.is_alive():
            character_2.attacking(target = character_1)
        else:
            if not character_1.is_max_level():
                character_1.level += 1
                character_1.update_stats()
            character_1.health = base_health1
            break

        if not character_1.is_alive():
            if not character_2.is_max_level():
                character_2.level += 1
                character_2.update_stats()
            character_2.health = base_health2
            break

    print(f"Character 1: {character_1}, is alive: {character_1.is_alive()}")
    print(f"Character 2: {character_2}, is alive: {character_2.is_alive()}")


orc = Orc(level = 1)
elf = Elf(level = 1)
fight(character_1 = orc, character_2 = elf)

