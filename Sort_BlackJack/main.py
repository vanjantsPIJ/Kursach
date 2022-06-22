#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
from random import randint


def list_sel_sort(list):
    for i in range(len(list) - 1):
        m = i
        j = i + 1
        while j < len(list):
            if list[j] < list[m]:
                m = j
            j = j + 1
        list[i], list[m] = list[m], list[i]



def sel_sort(array):
    print("Сортировка простым выбором!")
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        print("Выборка", i+1)
        array[i], array[m] = array[m], array[i]
        print(array)


a = []
for i in range(10):
    a.append(randint(1, 10))

sel_sort(a)
print("Отсортированный массив:", a)
print("\n")



def blackjack_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]



list = []


def blackjack(a):
    print('Поиграем в Блэкджэк?')


    step_count=0
    random.shuffle(a)
    print('Ваша колода состоит из данных карт:', a)
    player_count = 0
    dealer_count = 0

    while True:
        choice = input('Будете брать карту или посмотрите оставшиеся карты? y(да)/n(нет)/k(колода)\nМожет хотите посмотреть статистику? s(статистика)\n')
        if choice == 'y':
            deck = a.pop()
            step_count += 1
            print('\nВам попалась карта достоинством %d' %deck)
            player_count += deck
            deck = a.pop()
            dealer_count += deck
            random.shuffle(a)
            if player_count > 21:
                print('Извините, вы вышли за 21 очко и проиграли.\n')
                result = "Поражение, выход за 21 очко."
                list.append(step_count)
                list_sel_sort(list)
                with open('statistics.txt', 'a') as f:
                    print("Взято карт: %d" % step_count, file=f)
                    print("Ваше количество очков: %d" % player_count, file=f)
                    print("Количество очков у крупье: %d" % dealer_count, file=f)
                    print("Исход: %s\n" % result, file=f)
                cont_quest = input('Хотите ещё сыграть? y(yes)/n(no)\n')
                if cont_quest == 'y':
                    a = []
                    for i in range(10):
                        a.append(randint(1, 10))
                    blackjack(a)
                elif cont_quest == 'n':
                    break
            elif player_count == 21:
                print('Поздравляю, вы выйграли набрав 21 очко!\n')
                result = "Победа, набрано ровно 21 очко."
                list.append(step_count)
                list_sel_sort(list)
                with open('statistics.txt', 'a') as f:
                    print("Взято карт: %d" % step_count, file=f)
                    print("Ваше количество очков: %d" % player_count, file=f)
                    print("Количество очков у крупье: %d" % dealer_count, file=f)
                    print("Исход: %s\n" % result, file=f)
                cont_quest = input('Хотите ещё сыграть? y(yes)/n(no)\n')
                if cont_quest == 'y':
                    a = []
                    for i in range(10):
                        a.append(randint(1, 10))
                    blackjack(a)
                elif cont_quest == 'n':
                    break
            elif dealer_count == 21:
                print('Извините, у крупье 21 очко, вы проиграли.\n')
                result = "Поражение, крупье собрал 21 очко."
                list.append(step_count)
                list_sel_sort(list)
                with open('statistics.txt', 'a') as f:
                    print("Взято карт: %d" % step_count, file=f)
                    print("Ваше количество очков: %d" % player_count, file=f)
                    print("Количество очков у крупье: %d" % dealer_count, file=f)
                    print("Исход: %s\n" % result, file=f)
                cont_quest = input('Хотите ещё сыграть? y(yes)/n(no)\n')
                if cont_quest == 'y':
                    a = []
                    for i in range(10):
                        a.append(randint(1, 10))
                    blackjack(a)
                elif cont_quest == 'n':
                    break
            elif dealer_count > 21:
                print('Крупье вышел за 21 очко, вы выйграли!\n')
                result = "Победа, крупье вышел за 21 очко."
                list.append(step_count)
                list_sel_sort(list)
                with open('statistics.txt', 'a') as f:
                    print("Взято карт: %d" % step_count, file=f)
                    print("Ваше количество очков: %d" % player_count, file=f)
                    print("Количество очков у крупье: %d" % dealer_count, file=f)
                    print("Исход: %s\n" % result, file=f)
                cont_quest = input('Хотите ещё сыграть? y(yes)/n(no)\n')
                if cont_quest == 'y':
                    a = []
                    for i in range(10):
                        a.append(randint(1, 10))
                    blackjack(a)
                elif cont_quest == 'n':
                    break
            elif (player_count > 21) and (dealer_count>21):
                print('Вы и крупье вышли за 21 очко, ничья!\n')
                result = "Ничья"
                list.append(step_count)
                list_sel_sort(list)
                with open('statistics.txt', 'a') as f:
                    print("Взято карт: %d" % step_count, file=f)
                    print("Ваше количество очков: %d" % player_count, file=f)
                    print("Количество очков у крупье: %d" % dealer_count, file=f)
                    print("Исход: %s\n" % result, file=f)
                cont_quest = input('Хотите ещё сыграть? y(yes)/n(no)\n')
                if cont_quest == 'y':
                    a = []
                    for i in range(10):
                        a.append(randint(1, 10))
                    blackjack(a)
                elif cont_quest == 'n':
                    break
            else:
                print('У вас %d очков.' %player_count)
                print('У крупье %d очков.' %dealer_count)
        elif choice == 'n':
            print('У вас %d очков.' %player_count)
            print('У крупье %d очков.' %dealer_count)
            if dealer_count > player_count:
                print('У крупье больше очков, вы проиграли!')
                result = "Поражение, у крупье больше очков."
                list.append(step_count)
                list_sel_sort(list)
                with open('statistics.txt', 'a') as f:
                    print("Взято карт: %d" % step_count, file=f)
                    print("Ваше количество очков: %d" % player_count, file=f)
                    print("Количество очков у крупье: %d" % dealer_count, file=f)
                    print("Исход: %s\n" % result, file=f)
                cont_quest = input('Хотите ещё сыграть? y(yes)/n(no)\n')
                if cont_quest == 'y':
                    a = []
                    for i in range(10):
                        a.append(randint(1, 10))
                    blackjack(a)
                elif cont_quest == 'n':
                    break
            elif dealer_count == player_count:
                print('Ничья')
                result = "Ничья"
                list.append(step_count)
                list_sel_sort(list)
                with open('statistics.txt', 'a') as f:
                    print("Взято карт: %d" % step_count, file=f)
                    print("Ваше количество очков: %d" % player_count, file=f)
                    print("Количество очков у крупье: %d" % dealer_count, file=f)
                    print("Исход: %s\n" % result, file=f)
                cont_quest = input('Хотите ещё сыграть? y(yes)/n(no)\n')
                if cont_quest == 'y':
                    a = []
                    for i in range(10):
                        a.append(randint(1, 10))
                    blackjack(a)
                elif cont_quest == 'n':
                    break
            else:
                print('Вы выйграли!')
                result = "Победа, набрано больше очков чем у крупье!"
                list.append(step_count)
                list_sel_sort(list)
                with open('statistics.txt', 'a') as f:
                    print("Взято карт: %d" % step_count, file=f)
                    print("Ваше количество очков: %d" % player_count, file=f)
                    print("Количество очков у крупье: %d" % dealer_count, file=f)
                    print("Исход: %s\n" % result, file=f)
                cont_quest = input('Хотите ещё сыграть? y(yes)/n(no)\n')
                if cont_quest == 'y':
                    a = []
                    for i in range(10):
                        a.append(randint(1, 10))
                    blackjack(a)
                elif cont_quest == 'n':
                    break
        elif choice == 'k':
            blackjack_sort(a)
            print('В колоде осталось:', a)
            random.shuffle(a)
        elif choice == 's':
            with open("statistics.txt", "r") as f:
                for line in f:
                    print(line)



    print('До новых встреч!')


    with open('statistics.txt', 'a') as f:
        print("Взято карт: %d" %step_count, file = f)
        print("Ваше количество очков: %d" %player_count, file = f)
        print("Количество очков у крупье: %d" %dealer_count, file = f)
        print("Исход: %s\n" %result, file = f)

    endgame_choice = input("Хотите посмотреть статистику? y(yes)/n(no)\n")
    if endgame_choice == 'y':
        with open("statistics.txt", "r") as f:
            for line in f:
                print(line)
        print("СТАТИСТИКА ХОДОВ")
        print("Лучшее количество ходов: %s" %list[0])
        print("Худшее количество ходов: %s" %list[-1])
        exit()
    else:
        exit()


if __name__ == '__main__':
    blackjack(a)

