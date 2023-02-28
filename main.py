from dataclasses import dataclass
from random import randint, choice
from graphic_arts.start_game_banner import run_screensaver


@dataclass
class Charactor:
    name: str = ''
    health: int = 0
    defense: int = 0
    attack: int = 0
    brief_description: str = ''

    RANGE_VALUE_ATTACK: tuple = (1, 2)
    RANGE_VALUE_DEFENSE: tuple = (1, 2)
    SPECIAL_SKILL: str = 'Ничего'
    SPECIAL_BUFF: int = 0

    def attack_function(self):
        value_attack = self.attack + randint(*self.RANGE_VALUE_ATTACK)
        print(f'{self.name} нанёс урон, равный {value_attack}')
        return value_attack

    def defense_function(self):
        defense_buff = randint(*self.RANGE_VALUE_DEFENSE)
        self.defense += defense_buff
        print(
            f'<{self.name} увеличил защиту на {defense_buff}. '
            f'теперь он может заблокировать {self.defense} урона.>'
        )

    def take_damage(self, damage):
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
            print(f'<Заблокировано {defense_value} урона '
                  f'{self.name} не получил урон.>')

    def special(self):
        raise NotImplementedError('Задайте метод special в классе '
                                  f'{type(self).__name__}')

    def is_alive(self) -> bool:
        return self.health > 0


@dataclass
class Hero(Charactor):
    name: str = 'Новичок'
    health: int = 25
    defense: int = 2
    attack: int = 5
    brief_description: str = ('отважный искатель приключений, ходят слухи, '
                              'что неплохо поет')
    special_counter: int = 0

    RANGE_VALUE_ATTACK: tuple = (1, 3)
    RANGE_VALUE_DEFENSE: tuple = (1, 5)
    SPECIAL_SKILL: str = 'спеть классную песню'
    DEFAULT_HEALTH = 20
    DEFAULT_DEFENSE = 2
    DEFAULT_ATTACK = 5

    def choose_action(self) -> str:
        action_list = {
            'attack': 'attack',
            'defense': 'defense',
            'special': 'special',
            'status': 'status',
            'surrender': 'surrender'
        }
        while True:
            action = input('Твой ход.\n' 'Тебе доступны действия:\n'
                           'attack — чтобы атаковать противника, \n'
                           'defense — чтобы увеличить защиту, \n'
                           'special — чтобы использовать свою суперсилу,  \n'
                           'status — чтобы увидеть информацию о '
                           'персонаже.\n'
                           'surrender — чтобы сдаться. : ').lower()
            if action in action_list:
                selected_action = action_list[action]
                if selected_action == 'status':
                    print(self.status())
                else:
                    return selected_action
            else:
                print(f'Действие {action} не найдено, повтори ввод.')

    def special(self) -> None:
        print(f'{self.name} использовал навык "{self.SPECIAL_SKILL}". '
              'Как красиво!')
        if self.special_counter < 1:
            self.special_counter += 1
        else:
            self.health = 100
            self.defense = 15
            self.attack = 25
            print(f'{self.name} впадает в экстаз от пения.\n'
                  'Здоровье увеличено до 100\n'
                  'Защита увеличена до 15\n'
                  'Атака увеличена до 25')

    def status(self):
        print('')
        print(f'{self.name} - {self.brief_description}.\n'
              f'Здоровье - {self.health}\n'
              f'Защита - {self.defense}\n'
              f'Атака - {self.attack}\n'
              f'Специальный навык - {self.SPECIAL_SKILL}')


@dataclass
class Berserk(Hero):
    name: str = 'Берсерк'
    health: int = 60
    defense: int = 2
    attack: int = 10
    brief_description: str = ('кровавый клинок (но вот чья кровь?), '
                              'способен нанести себе урон и увеличить атаку')

    RANGE_VALUE_ATTACK: tuple = (5, 10)
    RANGE_VALUE_DEFENSE: tuple = (5, 8)
    SPECIAL_SKILL: str = 'впасть в безумие'

    def special(self) -> str:
        self.health -= 5
        self.attack += 15
        print(f'{self.name} использовал навык "{self.SPECIAL_SKILL}".\n'
              f'Здоровье уменьшено на 5 ({self.health}), '
              f'Атака увеличена на 15 ({self.attack}).')
        return self.health, self.attack


@dataclass
class Mage(Hero):
    name: str = 'Маг'
    health: int = 50
    defense: int = 2
    attack: int = 12
    brief_description: str = ('ученик Дамблдора, в университете подсел на '
                              'зелье, повышающее атаку')

    RANGE_VALUE_ATTACK: tuple = (5, 15)
    RANGE_VALUE_DEFENSE: tuple = (5, 10)
    SPECIAL_SKILL: str = 'выпить флакон маны'

    def special(self) -> str:
        self.attack += 10
        print(f'{self.name} использовал навык "{self.SPECIAL_SKILL}".\n'
              f'Атака увеличена на 10 ({self.attack}).')
        return self.attack


@dataclass
class Healer(Hero):
    name: str = 'Травница'
    health: int = 40
    defense: int = 4
    attack: int = 8
    brief_description: str = 'знаток травки, способна пополнять здоровье'

    RANGE_VALUE_ATTACK: tuple = (5, 15)
    RANGE_VALUE_DEFENSE: tuple = (5, 10)
    SPECIAL_SKILL: str = 'покурить трубку'

    def special(self) -> str:
        if self.health < 70:
            self.health += 15
            print(f'{self.name} использовала навык "{self.SPECIAL_SKILL}".\n'
                  f'Здоровье увеличено на 15 ({self.health}).\n'
                  '(Вы не сможете пополнять здоровье, если оно больше '
                  ' или равно 70)')
        else:
            self.health = 40
            print(f'{self.name} использовала навык "{self.SPECIAL_SKILL}".\n'
                  'Минздрав предупреждал, а ты не слушал и словил передоз. '
                  f'Здоровье уменьшено до ({self.health}).')
        return self.health


@dataclass
class Enemy(Charactor):
    name: str = 'Гоблин'
    health: int = 40
    defense: int = 2
    attack: int = 5
    brief_description: str = ('мерзкий гоблин')

    RANGE_VALUE_ATTACK: tuple = (1, 3)
    RANGE_VALUE_DEFENSE: tuple = (1, 5)
    SPECIAL_SKILL: str = 'оскалить зубы'

    def special(self) -> int:
        print(f'{self.name} использовал навык "{self.SPECIAL_SKILL}". '
              'Неприятно, но что поделать')
        damage = 1
        return damage


@dataclass
class HeadCrab(Enemy):
    name: str = 'Хед краб'
    health: int = 45
    defense: int = 3
    attack: int = 9
    brief_description: str = ('представитель инопланетной фауны')

    RANGE_VALUE_ATTACK: tuple = (1, 3)
    RANGE_VALUE_DEFENSE: tuple = (1, 5)
    SPECIAL_SKILL: str = 'отравляющий плевок в лицо'

    def special(self):
        print(f'{self.name} использовал навык "{self.SPECIAL_SKILL}" '
              'и нанес тебе 15 урона')
        poison_split: int = 15
        return poison_split


def choice_char_class() -> Hero:
    """
    Возвращает
    класс персонажа.
    """
    game_classes = {'berserk': Berserk,
                    'mage': Mage,
                    'healer': Healer,
                    'skip': Hero}
    approve_choice: str = ''

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Берсерк — berserk, '
                               'Маг — mage, Травница — healer.\n'
                               'Или введи skip, чтобы продолжить играть '
                               'за стандартного персонажа: ')
        char_class = None
        while not char_class:
            try:
                char_class: Hero = game_classes[selected_class]()
                char_class.status()
                approve_choice = input('Нажми (Y), чтобы подтвердить '
                                       'выбор, или любую другую кнопку, '
                                       'чтобы выбрать другого '
                                       'персонажа. : ').lower()
            except KeyError:
                selected_class = input(f'Класс {selected_class} не найден, '
                                       'повтори ввод: ')
    return char_class


def start_training(hero):
    """
    Принимает на вход класс персонажа из функции choice_char_class.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    print('')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: '
          'attack — чтобы атаковать противника, \n'
          'defense — чтобы блокировать атаку противника, \n'
          'special — чтобы использовать свою суперсилу,  \n'
          'status — чтобы увидеть информацию о персонаже.\n')
    print('Если не хочешь тренироваться, введи команду skip: ')
    cmd: str = ''
    commands: dict = {
        'attack': hero.attack_function,
        'defense': hero.defense_function,
        'special': hero.special,
        'status': hero.status
    }
    while cmd != 'skip':

        cmd = input('Введи команду: ')
        if cmd in commands:
            result = commands[cmd]()
            print(result)
        elif cmd == 'skip':
            pass
        else:
            print('<Неизвестная комманда. Попробуй еще раз>')
    return 'Тренировка окончена.'


def meet_enemy(enemy_list: list[Enemy] = [Enemy, HeadCrab]) -> Enemy:
    """Выберает врога из списка классов Enemy."""
    print('')
    enemy = choice(enemy_list)()
    print(f'Вы встретили врага - {enemy.name}!')
    return enemy


def battle(hero, enemy):
    """Запускает бой между игроком и врагом."""
    print('Эпичная битва между {} и {}!'.format(hero.name, enemy.name))

    while hero.is_alive() and enemy.is_alive():

        # Ход игрока
        print('')
        hero_action = hero.choose_action()
        if hero_action == 'attack':
            damage = hero.attack_function()
            enemy.take_damage(damage)
        elif hero_action == 'defense':
            hero.defense_function()
        elif hero_action == "special":
            hero.special()
            print('{} использует специальный навык'.format(
                hero.name))
        elif hero_action == 'surrender':
            hero.health = 0

        # Ход врага
        print('')
        enemy_action = choice(['attack', 'defense', 'special'])
        if enemy_action == 'attack':
            damage = enemy.attack_function()
            hero.take_damage(damage)
        elif enemy_action == 'defense':
            enemy.defense_function()
        elif enemy_action == 'special':
            damage = enemy.special()
            hero.take_damage(damage)
            print('{} использует специальный навык {} на {} урона!'.format(
                enemy.name, hero.name, damage))

        # Вывести ХП в конце каждого хода
        print('')
        print('У {} сейчас {} HP'.format(hero.name, hero.health))
        print('У {} сейчас {} HP'.format(enemy.name, enemy.health))

    # Вывод результата битвы
    if hero.is_alive():
        print('{} победил в битве'.format(hero.name))

    else:
        print('{} победил в битве'.format(enemy.name))


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    payer_name: str = input('...назови себя: ')
    print(f'Здравствуй, {payer_name}!')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Берсерк, Маг, Травница')
    hero: Hero = choice_char_class()
    start_training(hero)
    print('')
    print('Вы отправились в опасное приключение')
    while hero.is_alive():
        battle(hero, meet_enemy())
