"""
Текстовая RPG, где можно играть за разных персонажей с элементами прогрессии.
В приключении игрока ждут бои с разнообразными противниками
"""
from random import choice
from graphic_arts.start_game_banner import run_screensaver
from hero_classes import Hero, Mage, Berserk, Healer
from enemy_classes import Enemy, HeadCrab
from typing import Type, Optional


def choice_char_class() -> Hero:
    """
    Возвращает выбранный игроком
    класс персонажа.
    """
    game_classes: dict[str, Type[Hero]] = {'berserk': Berserk,
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

        char_class: Optional[Hero] = None

        while not char_class:
            try:
                char_class = game_classes[selected_class]()
                char_class.status
                approve_choice = input('Нажми (Y), чтобы подтвердить '
                                       'выбор, или любую другую кнопку, '
                                       'чтобы выбрать другого '
                                       'персонажа. : ').lower()
            except KeyError:
                selected_class = input(f'Класс {selected_class} не найден, '
                                       'повтори ввод: ')
    assert char_class, 'Класс не задан'
    return char_class


def start_training(hero) -> None:
    """
    Принимает на вход класс персонажа из функции choice_char_class.
    Запускает тренировку, котороая завершится при вводе игроком команды skip
    """
    print('\nПотренируйся управлять своими навыками.')
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
        else:
            print('<Неизвестная комманда. Попробуй еще раз>')

    hero.recovery()
    print('Тренировка окончена.')


def meet_enemy(enemy_list: list[Type[Enemy]] = [Enemy, HeadCrab]) -> Enemy:
    """Выберает врога из списка классов Enemy."""
    print('')
    enemy = choice(enemy_list)()
    print(f'Вы встретили врага - {enemy.name}!')
    return enemy


def battle(hero: Hero, enemy: Enemy):
    """
    Запускает бой между игроком и врагом, бой завершится при смерти одного 
    из участников.
    """
    print('Эпичная битва между {} и {}!'.format(hero.name, enemy.name))

    while hero.is_alive() and enemy.is_alive():

        # Ход игрока
        print('')
        hero_action: Optional[str] = hero.choose_action()
        if hero_action == 'attack':
            damage: int = hero.attack_function()
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

        # Вывод ХП в конце каждого хода
        print('')
        print('У {} сейчас {} HP'.format(hero.name, hero.health))
        print('У {} сейчас {} HP'.format(enemy.name, enemy.health))

    # Вывод результата битвы
    # Повышение уровня и восстановление характеристик персонажа до стандартных
    # в случае победы игрока
    if hero.is_alive():
        print('{} победил в битве'.format(hero.name))
        print('Здоровье восстановлено.\n')
        hero.level_up()
        hero.recovery()
    else:
        print('{} победил в битве'.format(enemy.name))


def path(hero) -> None:
    """
    Запускает приключение персонажа. Завершает работу при смерти персонажа 
    игрока или при вводе игроком команды exit.
    """
    path_list: list[str] = [
        'left',
        'right'
    ]
    while hero.is_alive():
        path_choice = input('Ты видишь перед собой развилку.\n'
                            'Выбери направление пути:\n'
                            'Налево - введи left\n'
                            'Направо - введи right\n'
                            'Чтобы выйти из игры введи exit\n'
                            'Введи команду: ')

        if path_choice in path_list:
            battle(hero, meet_enemy())
        elif path_choice == 'exit':
            break
        else:
            print('<Неизвестная команда. Попробуй еще раз.>')
    print('На этом твой путь окончен.')


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
    print('Вы отправились в опасное приключение.\n')
    path(hero)
