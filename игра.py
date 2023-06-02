import random #библеотека случайностей
import os
import re



def check_play_status():
    valid_responses = ['да', 'нет']
    while True:
        try:
            response = input('Поиграем снова? (Да или Нет): ')
            if response.lower() not in valid_responses:
                raise ValueError('Только Да или Нет')

            if response.lower() == 'да':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Спасибо за игру!')
                exit()
        except ValueError as err:
            print(err)


def play_rps():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Камень, Ножнцы, Бумага - Су Е Фа!!!')

        user_choise = input('Выбери оружие'
                            ' [К]амень, [Н]ожницы или [Б]умага: ')

        if not re.match("[КкНнБб]", user_choise):
            print('Выберите букву:')
            print('[К]амень, [Н]ожницы или [Б]умага')
            continue

        print(f'Твой выбор: {user_choise}')

        choises = ['К', 'Н', 'Б']
        opp_choise = random.choice(choises)

        print(f'Я выбираю: {opp_choise}')

        if opp_choise == user_choise.upper():
            print('Ничья!')
            play = check_play_status()
        elif opp_choise == 'К' and user_choise.upper() == 'Н':
            print('Камень бьет ножницы, я победил!!')
            play = check_play_status()
        elif opp_choise == 'Н' and user_choise.upper() == 'Б':
            print('Ножницы бьют бумагу, я победил!!')
            play = check_play_status()
        elif opp_choise == 'Б' and user_choise.upper() == 'К':
            print('Бумага бьет камень, я победил!!')
            play = check_play_status()
        else:
            print('Ты победил!!\n')
            play = check_play_status()


if __name__ == '__main__':
    play_rps()
