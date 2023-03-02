"""
Содержит родительский классы врагов, которых можно встретить в игре.
"""
from dataclasses import dataclass
from typing import Optional
from random import randint


from hero_classes import Charactor
import text


@dataclass
class Enemy(Charactor):
    name: str = 'Гоблин'
    health: int = 80
    defense: int = 5
    attack: int = 5
    brief_description: str = text.BRIEF_DESCRIPTION_ENEMY

    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (1, 5)
    SPECIAL_SKILL: str = 'оскалить зубы'

    def attack_function(self, other: Optional[Charactor] = None) -> None:
        """Рассчитывают нанесенный урон"""
        value_attack: int = self.attack + randint(*self.RANGE_VALUE_ATTACK)
        print(text.ATTACK_DESC_MSG.format(self.name, value_attack))

        if other:
            damage_value: int = value_attack - other.defense
            defense_value: int = value_attack - damage_value

            if damage_value >= other.health:
                other.health = 0
                print('{} погиб.'.format(other.name))
                return

            if damage_value <= 0:
                print(text.TAKE_ZERO_DMG_MSG.format(other.name))
                return

            other.health -= damage_value
            print(text.TAKE_DMG_MSG.format(other.name, damage_value,
                                           defense_value))

    def special(self) -> int:
        """Задает специальный прием персонажа."""
        print(text.SPECIAL_MSG_ENEMY.format(self.name, self.SPECIAL_SKILL))
        damage: int = 1
        return damage


@dataclass
class HeadCrab(Enemy):
    name: str = 'Хед краб'
    health: int = 110
    defense: int = 8
    attack: int = 9
    brief_description: str = text.BRIEF_DESCRIPTION_HEADCRAB

    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 5)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (1, 3)
    SPECIAL_SKILL: str = 'отравляющий плевок в лицо'

    def special(self) -> int:
        """Задает специальный прием персонажа."""
        print(text.SPECIAL_MSG_HEADCRAB.format(self.name, self.SPECIAL_SKILL))
        poison_split: int = 15
        return poison_split


ENEMY_LIST = [Enemy, HeadCrab]
