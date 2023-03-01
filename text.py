# Сообщения классов Charactor и Hero
# attack
ATTACK_DESC_MSG: str = '<{} нанёс урон, равный {}>'
# defense
DEFENSE_DESC_MSG: str = ('<{} увеличил защиту на {}. '
                         'теперь он может заблокировать {} урона.>')
# take_damage
TAKE_DMG_MSG: str = ('<{} получил урон в размере '
                     '{}. Заблокировано {} урона.>')
TAKE_ZERO_DMG_MSG: str = ('<Заблокирован весь урон. '
                          '{} не получил повреждений.>')
# special if not imp
NOT_INPL_SPECIAL_MSG: str = 'Задайте метод special в классе {}'
# choose_action
SELECT_ACTION_MSG: str = ('Твой ход.\n' 'Тебе доступны действия:\n'
                          'attack — чтобы атаковать противника, \n'
                          'defense — чтобы увеличить защиту, \n'
                          'special — чтобы использовать свою суперсилу,  \n'
                          'status — чтобы увидеть информацию о '
                          'персонаже.\n'
                          'surrender — чтобы сдаться. : ')
# CMD_NOT_FOUND
# status
STATUS_MSG: str = ('\n{} - {}.\nЗдоровье - {}\nЗащита - {}\nАтака - {}\n'
                   'Специальный навык - {}')
# level_up
LEVEL_UP_MSG: str = 'Уровень повышен!\n Текущий уровень {}\n'
SELECT_ATTRIBUTE_MSG: str = ('Выбери атрибут для улучшения:\n'
                             'Здоровье +5 - команда health\n'
                             'Защита +2 - команда defense\n'
                             'Атака + 4 - команда Attack\n')
CMD_NOT_FOUND: str = 'Команда {} не найдена, повтори ввод: '  # Универсальная


# Описания героев
BRIEF_DESCRIPTION_HERO: str = ('отважный искатель приключений, ходят слухи, '
                               'что неплохо поет')
BRIEF_DESCRIPTION_MAGE: str = ('ученик Дамблдора, в университете подсел на '
                               'зелье, повышающее атаку')
BRIEF_DESCRIPTION_BERSERK: str = ('кровавый клинок (но вот чья кровь?), '
                                  'способен нанести себе урон и увеличить атаку')
BRIEF_DESCRIPTION_HEALER: str = 'знаток травки, способна пополнять здоровье'

# Описания врагов
BRIEF_DESCRIPTION_ENEMY: str = 'мерзкий гоблин'
BRIEF_DESCRIPTION_HEADCRAB: str = 'представитель инопланетной фауны'

# Сообщения специальных навыков героев
SPECIAL_MSG_HERO: str = '{} использовал навык "{}". Как красиво!'
SPECIAL_MSG_HERO_BUFFED: str = ('{} впадает в экстаз от пения.\n'
                                'Здоровье увеличено до 100\n'
                                'Защита увеличена до 15\n'
                                'Атака увеличена до 25')
SPECIAL_MSG_MAGE: str = ('{} использовал навык "{}".\n'
                         'Атака увеличена на 10 ({}).')
SPECIAL_MSG_BERSERK: str = ('{} использовал навык "{}".\n'
                            'Здоровье уменьшено на 5 ({}), '
                            'Атака увеличена на 15 ({}).')
SPECIAL_MSG_HEALER: str = ('{} использовала навык "{}".\n'
                           'Здоровье увеличено на 15 ({}).\n'
                           '(Вы не сможете пополнять здоровье, если оно больше'
                           ' или равно 110)')
SPECIAL_MSG_HEALER_BUFFED: str = (
    '{} использовала навык "{}".\n Минздрав предупреждал, а ты не слушал и '
    'словил передоз. Здоровье уменьшено до ({}).'
)
# Сообщения специальных навыков врагов
SPECIAL_MSG_ENEMY: str = ('{} использовал навык "{}". '
                          'Неприятно, но что поделать')
SPECIAL_MSG_HEADCRAB: str = ('{} использовал навык "{}" '
                             'и нанес тебе 15 урона')

# сообщения функций
# approve_choice
SELECTED_MSG: str = ('Введи название персонажа, '
                     'за которого хочешь играть: Берсерк — berserk, '
                     'Маг — mage, Травница — healer.\n'
                     'Или введи skip, чтобы продолжить играть '
                     'за стандартного персонажа: ')
APPROVE_MSG: str = ('Нажми (Y), чтобы подтвердить '
                    'выбор, или любую другую кнопку, '
                    'чтобы выбрать другого '
                    'персонажа. : ')
# start_training
TRAINING_MSG: str = ('\nПотренируйся управлять своими навыками.'
                     'Введи одну из команд: '
                     'attack — чтобы атаковать противника, \n'
                     'defense — чтобы блокировать атаку противника, \n'
                     'special — чтобы использовать свою суперсилу,  \n'
                     'status — чтобы увидеть информацию о персонаже.\n'
                     'Если не хочешь тренироваться, введи команду skip: ')
# path
PATH_MSG: str = ('Ты видишь перед собой развилку.\n'
                 'Выбери направление пути:\n'
                 'Налево - введи left\n'
                 'Направо - введи right\n'
                 'Чтобы выйти из игры введи exit\n'
                 'Введи команду: ')
GAME_OVER: str = 'На этом твой путь окончен.'
# battle
ROUND_RESULT: str = '\nУ {} сейчас {} HP\nУ {} сейчас {} HP'
