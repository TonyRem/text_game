"""
Текстовая RPG, где можно играть за разных персонажей с элементами прогрессии.
В приключении игрока ждут бои с разнообразными противниками
"""
from random import choice
from typing import Type, Optional

from graphic_arts.start_game_banner import run_screensaver
from hero_classes import Hero, Mage, Berserk, Healer
from enemy_classes import Enemy, ENEMY_LIST
import text


def choice_hero_class() -> Hero:
    """
    Возвращает выбранный игроком
    класс персонажа.
    """
    GAME_CLASSES: dict[str, Type[Hero]] = {'berserk': Berserk,
                                           'mage': Mage,
                                           'healer': Healer,
                                           'skip': Hero}

    while True:
        selected_class: str = input(text.SELECTED_MSG)
        if selected_class not in GAME_CLASSES:
            print(text.CMD_NOT_FOUND.format(selected_class))
            continue
        chosen_hero: Hero = GAME_CLASSES[selected_class]()
        chosen_hero.status()
        if input(text.APPROVE_MSG).lower() == 'y':
            return chosen_hero


def start_training(hero) -> None:
    """
    Принимает на вход класс персонажа из функции choice_hero_class.
    Запускает тренировку, котороая завершится при вводе игроком команды skip
    """
    print(text.TRAINING_MSG)
    commands: dict = {
        'attack': hero.attack_function,
        'defense': hero.defense_function,
        'special': hero.special,
        'status': hero.status
    }

    while True:
        training_cmd: str = input('Введи команду: ')
        if training_cmd == 'skip':
            break
        if training_cmd not in commands:
            print(text.CMD_NOT_FOUND.format(training_cmd))
            continue
        result = commands[training_cmd]
        result()

    hero.recovery()
    print('Тренировка окончена.')


def meet_enemy(enemy_list: list[Type[Enemy]] = ENEMY_LIST) -> Enemy:
    """Выберает врага из списка классов Enemy."""
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
            hero.attack_function(enemy)
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
        if hero.is_alive() and enemy.is_alive():
            enemy_action = choice(['attack', 'defense', 'special'])
            if enemy_action == 'attack':
                enemy.attack_function(hero)
            elif enemy_action == 'defense':
                enemy.defense_function()
            else:
                enemy.special(hero)

        # Вывод ХП в конце каждого хода
        print(text.ROUND_RESULT.format(hero.name, hero.health,
                                       enemy.name, enemy.health))

    # Вывод результата битвы
    # Повышение уровня и восстановление характеристик персонажа до стандартных
    # в случае победы игрока
    if hero.is_alive():
        print('{} победил в битве'.format(hero.name))
        print('Здоровье восстановлено.\n')
        hero.recovery()
        hero.level_up()

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
        path_choice = input(text.PATH_MSG)
        if path_choice == 'exit':
            break
        if path_choice not in path_list:
            print(text.CMD_NOT_FOUND.format(path_choice))
            continue
        battle(hero, meet_enemy())
    print(text.GAME_OVER)


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Сейчас у тебя класс Новичок, но ты можешь выбрать один из трех '
          'путей силы:')
    print('Берсерк, Маг, Травница')
    hero: Hero = choice_hero_class()
    start_training(hero)
    print('')
    print('Вы отправились в опасное приключение.\n')
    path(hero)
