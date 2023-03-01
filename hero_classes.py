"""
Содержит родительский класс Charactor и классы героев, которых может 
выбрать игрок.
"""


from dataclasses import dataclass
from random import randint
from typing import Optional


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

    def attack_function(self) -> int:
        """Выводит значение нанесенного урона."""
        value_attack: int = self.attack + randint(*self.RANGE_VALUE_ATTACK)
        print(f'{self.name} нанёс урон, равный {value_attack}')
        return value_attack

    def defense_function(self) -> None:
        defense_buff: int = randint(*self.RANGE_VALUE_DEFENSE)
        self.defense += defense_buff
        print(
            f'<{self.name} увеличил защиту на {defense_buff}. '
            f'теперь он может заблокировать {self.defense} урона.>'
        )

    def take_damage(self, damage) -> None:
        """
        Принимает урон, нанесенный противником и рассчитывает повреждения.
        """
        damage_value: int = damage - self.defense
        defense_value: int = damage - damage_value
        if damage_value > 0:
            if self.health > damage_value:
                self.health -= damage_value
            else:
                self.health = 0
                print('{} погиб.'.format(self.name))
            print(
                f'<{self.name} получил урон в размере '
                '{}. Заблокировано {} урона.>'.format(
                    damage_value,  defense_value)
            )
        else:
            print(f'<Заблокирован весь урон. '
                  f'{self.name} не получил повреждений.>')

    def special(self) -> Optional[int]:
        """Задает специальный прием персонажа."""
        raise NotImplementedError('Задайте метод special в классе '
                                  f'{type(self).__name__}')

    def is_alive(self) -> bool:
        """Проверяет жив ли персонаж."""
        return self.health > 0


@dataclass
class Hero(Charactor):
    name: str = 'Новичок'
    health: int = 50
    defense: int = 2
    attack: int = 5
    brief_description: str = ('отважный искатель приключений, ходят слухи, '
                              'что неплохо поет')
    special_counter: int = 0
    level: int = 0

    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (1, 5)
    SPECIAL_SKILL: str = 'спеть классную песню'
    DEFAULT_HEALTH: int = 50
    DEFAULT_DEFENSE: int = 2
    DEFAULT_ATTACK: int = 5

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
            action: str = input('Твой ход.\n' 'Тебе доступны действия:\n'
                                'attack — чтобы атаковать противника, \n'
                                'defense — чтобы увеличить защиту, \n'
                                'special — чтобы использовать свою суперсилу,  \n'
                                'status — чтобы увидеть информацию о '
                                'персонаже.\n'
                                'surrender — чтобы сдаться. : ').lower()
            if action in action_list:
                selected_action = action
                if selected_action == 'status':
                    self.status()
                else:
                    return selected_action
            else:
                print(f'Действие {action} не найдено, повтори ввод.')

    def special(self) -> None:
        """Задает специальный прием персонажа."""      
        print(f'{self.name} использовал навык "{self.SPECIAL_SKILL}". '
              'Как красиво!')
        if self.special_counter < 1:
            self.special_counter += 1
        else:
            self.health = 100
            self.defense = 15
            self.attack = 35
            print(f'{self.name} впадает в экстаз от пения.\n'
                  'Здоровье увеличено до 100\n'
                  'Защита увеличена до 15\n'
                  'Атака увеличена до 25')

    def status(self) -> None:
        """Выводит информацию о персонаже."""
        print(f'\n{self.name} - {self.brief_description}.\n'
              f'Здоровье - {self.health}\n'
              f'Защита - {self.defense}\n'
              f'Атака - {self.attack}\n'
              f'Специальный навык - {self.SPECIAL_SKILL}')

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
        print('Уровень повышен!\n'
              'Текущий уровень {}\n'.format(self.level))
        attribute_up_list: list[str] = [
            'attack',
            'defense',
            'health'
        ]
        level_up_result: bool = False
        while not level_up_result:
            attribute_up = input('Выбери атрибут для улучшения:\n'
                                 'Здоровье +5 - команда health\n'
                                 'Защита +2 - команда defense\n'
                                 'Атака + 4 - команда Attack\n'
                                 ).lower()
            if attribute_up in attribute_up_list:
                if attribute_up == 'health':
                    self.DEFAULT_HEALTH += 5
                    level_up_result = True
                elif attribute_up == 'defense':
                    self.DEFAULT_DEFENSE += 2
                    level_up_result = True
                else:
                    self.DEFAULT_ATTACK += 4
                    level_up_result = True
            else:
                print(f'Команда {attribute_up} не найдена, повтори ввод.')
            self.status


@dataclass
class Berserk(Hero):
    name: str = 'Берсерк'
    health: int = 80
    defense: int = 2
    attack: int = 9
    brief_description: str = ('кровавый клинок (но вот чья кровь?), '
                              'способен нанести себе урон и увеличить атаку')

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
        print(f'{self.name} использовал навык "{self.SPECIAL_SKILL}".\n'
              f'Здоровье уменьшено на 5 ({self.health}), '
              f'Атака увеличена на 15 ({self.attack}).')


@dataclass
class Mage(Hero):
    name: str = 'Маг'
    health: int = 70
    defense: int = 2
    attack: int = 10
    brief_description: str = ('ученик Дамблдора, в университете подсел на '
                              'зелье, повышающее атаку')

    RANGE_VALUE_ATTACK: tuple[int, int] = (5, 15)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (5, 10)
    SPECIAL_SKILL: str = 'выпить флакон маны'
    DEFAULT_HEALTH: int = 70
    DEFAULT_DEFENSE: int = 2
    DEFAULT_ATTACK: int = 10

    def special(self) -> None:
        """Задает специальный прием персонажа.""" 
        self.attack += 10
        print(f'{self.name} использовал навык "{self.SPECIAL_SKILL}".\n'
              f'Атака увеличена на 10 ({self.attack}).')


@dataclass
class Healer(Hero):
    name: str = 'Травница'
    health: int = 75
    defense: int = 4
    attack: int = 8
    brief_description: str = 'знаток травки, способна пополнять здоровье'

    RANGE_VALUE_ATTACK: tuple[int, int] = (5, 15)
    RANGE_VALUE_DEFENSE: tuple[int, int] = (5, 10)
    SPECIAL_SKILL: str = 'покурить трубку'
    DEFAULT_HEALTH: int = 75
    DEFAULT_DEFENSE: int = 4
    DEFAULT_ATTACK: int = 8

    def special(self) -> None:
        """Задает специальный прием персонажа.""" 
        if self.health < 110:
            self.health += 15
            print(f'{self.name} использовала навык "{self.SPECIAL_SKILL}".\n'
                  f'Здоровье увеличено на 15 ({self.health}).\n'
                  '(Вы не сможете пополнять здоровье, если оно больше '
                  ' или равно 110)')
        else:
            self.health = 60
            print(f'{self.name} использовала навык "{self.SPECIAL_SKILL}".\n'
                  'Минздрав предупреждал, а ты не слушал и словил передоз. '
                  f'Здоровье уменьшено до ({self.health}).')
