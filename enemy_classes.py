"""
Содержит родительский классы врагов, которых можно встретить в игре.
"""
from dataclasses import dataclass
from hero_classes import Charactor


@dataclass
class Enemy(Charactor):
    name: str = 'Гоблин'
    health: int = 80
    defense: int = 2
    attack: int = 5
    brief_description: str = ('мерзкий гоблин')

    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (1, 5)
    SPECIAL_SKILL: str = 'оскалить зубы'

    def special(self) -> int:
        """Задает специальный прием персонажа.""" 
        print(f'{self.name} использовал навык "{self.SPECIAL_SKILL}". '
              'Неприятно, но что поделать')
        damage: int = 1
        return damage


@dataclass
class HeadCrab(Enemy):
    name: str = 'Хед краб'
    health: int = 110
    defense: int = 3
    attack: int = 9
    brief_description: str = ('представитель инопланетной фауны')

    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 5)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (1, 3)
    SPECIAL_SKILL: str = 'отравляющий плевок в лицо'

    def special(self) -> int:
        """Задает специальный прием персонажа.""" 
        print(f'{self.name} использовал навык "{self.SPECIAL_SKILL}" '
              'и нанес тебе 15 урона')
        poison_split: int = 15
        return poison_split
