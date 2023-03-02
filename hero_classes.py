"""
Содержит родительский класс Charactor и классы героев, которых может
выбрать игрок.
"""
from dataclasses import dataclass
from random import randint
from typing import Optional

import text


@dataclass
class Charactor:
    name: str = ''
    health: int = 0
    defense: int = 0
    attack: int = 0
    brief_description: str = ''

    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 2)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (1, 2)
    SPECIAL_SKILL: str = 'Ничего'
    SPECIAL_BUFF: int = 0

    def attack_function(self) -> None:
        """Рассчитывают нанесенный урон"""
        raise NotImplementedError(text.NOT_INPL_ATTACK_MSG.format(
            type(self).__name__
        ))

    def defense_function(self) -> None:
        """Увеличивает защиту персонажа."""
        defense_buff: int = randint(*self.RANGE_VALUE_DEFENSE)
        self.defense += defense_buff
        print(text.DEFENSE_DESC_MSG.format(
            self.name, defense_buff, self.defense))

    def special(self) -> Optional[int]:
        """Задает специальный прием персонажа."""
        raise NotImplementedError(text.NOT_INPL_SPECIAL_MSG.format(
            type(self).__name__
        ))

    def is_alive(self) -> bool:
        """Проверяет жив ли персонаж."""
        return self.health > 0


@dataclass
class Hero(Charactor):
    name: str = 'Новичок'
    health: int = 50
    defense: int = 2
    attack: int = 5
    brief_description: str = text.BRIEF_DESCRIPTION_HERO
    special_counter: int = 0
    level: int = 0

    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (1, 5)
    SPECIAL_SKILL: str = 'спеть классную песню'
    DEFAULT_HEALTH: int = 50
    DEFAULT_DEFENSE: int = 2
    DEFAULT_ATTACK: int = 5

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

    def choose_action(self) -> Optional[str]:
        """Возвращает действие игрока в битвах."""
        action_list: list[str] = [
            'attack',
            'defense',
            'special',
            'status',
            'surrender'
        ]
        while True:
            action: str = input(text.SELECT_ACTION_MSG).lower()
            if action not in action_list:
                print(text.CMD_NOT_FOUND.format(action))
            if action == 'status':
                self.status()
                continue
            return action

    def special(self) -> None:
        """Задает специальный прием персонажа."""
        print(text.SPECIAL_MSG_HERO.format(self.name, self.SPECIAL_SKILL))
        if self.special_counter < 1:
            self.special_counter += 1
        else:
            self.health = 100
            self.defense = 15
            self.attack = 35
            print(text.SPECIAL_MSG_HERO_BUFFED.format(self.name))

    def status(self) -> None:
        """Выводит информацию о персонаже."""
        print(text.STATUS_MSG.format(
            self.name, self.brief_description, self.health, self.defense,
            self.attack, self.SPECIAL_SKILL
        ))

    def recovery(self) -> None:
        """Восстанавливает значения характеристик по умолчанию после битвы."""
        self.attack = self.DEFAULT_ATTACK
        self.defense = self.DEFAULT_DEFENSE
        self.health = self.DEFAULT_HEALTH
        self.special_counter = 0

    def level_up(self) -> None:
        """
        Предоставляет игроку выбор по прокачке характерисики при повышении
        уровня.
        """
        self.level += 1
        print(text.LEVEL_UP_MSG.format(self.level))
        attribute_up_list: list[str] = [
            'attack',
            'defense',
            'health'
        ]

        while True:
            attribute_up = input(text.SELECT_ATTRIBUTE_MSG).lower()
            if attribute_up not in attribute_up_list:
                print(text.CMD_NOT_FOUND.format(attribute_up))

            if attribute_up == 'health':
                self.DEFAULT_HEALTH += 5
            elif attribute_up == 'defense':
                self.DEFAULT_DEFENSE += 2
            else:
                self.DEFAULT_ATTACK += 4

            self.status()
            break


@dataclass
class Berserk(Hero):
    name: str = 'Берсерк'
    health: int = 80
    defense: int = 2
    attack: int = 9
    brief_description: str = text.BRIEF_DESCRIPTION_BERSERK

    RANGE_VALUE_ATTACK: tuple[int, int] = (5, 10)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (5, 8)
    SPECIAL_SKILL: str = 'впасть в безумие'
    DEFAULT_HEALTH: int = 80
    DEFAULT_DEFENSE: int = 2
    DEFAULT_ATTACK: int = 9

    def special(self) -> None:
        """Задает специальный прием персонажа."""
        self.health -= 5
        self.attack += 15
        print(text.SPECIAL_MSG_BERSERK.format(self.name, self.SPECIAL_SKILL,
                                              self.health, self.attack))


@dataclass
class Mage(Hero):
    name: str = 'Маг'
    health: int = 70
    defense: int = 2
    attack: int = 10
    brief_description: str = text.BRIEF_DESCRIPTION_MAGE

    RANGE_VALUE_ATTACK: tuple[int, int] = (5, 15)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (5, 10)
    SPECIAL_SKILL: str = 'выпить флакон маны'
    DEFAULT_HEALTH: int = 70
    DEFAULT_DEFENSE: int = 2
    DEFAULT_ATTACK: int = 10

    def special(self) -> None:
        """Задает специальный прием персонажа."""
        self.attack += 10
        print(text.SPECIAL_MSG_MAGE.format(self.name, self.SPECIAL_SKILL,
                                           self.attack))


@dataclass
class Healer(Hero):
    name: str = 'Травница'
    health: int = 75
    defense: int = 4
    attack: int = 8
    brief_description: str = text.BRIEF_DESCRIPTION_HEALER

    RANGE_VALUE_ATTACK: tuple[int, int] = (5, 15)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (5, 10)
    SPECIAL_SKILL: str = 'покурить трубку'
    DEFAULT_HEALTH: int = 75
    DEFAULT_DEFENSE: int = 4
    DEFAULT_ATTACK: int = 8

    def special(self) -> None:
        """Задает специальный прием персонажа."""
        if self.health < 110:
            self.health += 30
            print(text.SPECIAL_MSG_HEALER.format(self.name, self.SPECIAL_SKILL,
                                                 self.health))
        else:
            self.health = 60
            print(text.SPECIAL_MSG_HEALER_BUFFED.format(
                self.name, self.SPECIAL_SKILL, self.health
            ))
