import random
from random import randint

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

def blackjack_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]



def blackjack(a):
    print('Поиграем в Блэкджэк?')

    random.shuffle(a)
    print('Ваша колода состоит из данных карт:', a)
    player_count = 0
    dealer_count = 0

    while True:
        choice = input('Будете брать карту или посмотрите оставшиеся карты? y/n/k\n')
        if choice == 'y':
            deck = a.pop()
            print('Вам попалась карта достоинством %d' %deck)
            player_count += deck
            deck = a.pop()
            dealer_count += deck
            random.shuffle(a)
            if player_count > 21:
                print('Извините, вы вышли за 21 очко и проиграли')
                break
            elif player_count == 21:
                print('Поздравляю, вы выйграли набрав 21 очко!')
                break
            elif dealer_count == 21:
                print('Извините, у крупье 21 очко, вы проиграли!')
                break
            else:
                print('У вас %d очков.' %player_count)
                print('У крупье %d очков.' %dealer_count)
        elif choice == 'n':
            print('У вас %d очков.' %player_count)
            print('У крупье %d очков.' %dealer_count)
            if dealer_count > player_count:
                print('У крупье больше очков, вы проиграли!')
            elif dealer_count == player_count:
                print('Ничья')
            else:
                print('Вы выйграли!')
            break
        elif choice == 'k':
            random.shuffle(a)
            print('В колоде осталось:', a)
            blackjack_sort(a)


    print('До новых встреч!')

if __name__ == '__main__':
    blackjack(a)