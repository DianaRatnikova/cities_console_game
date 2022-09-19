__author__ = 'DIANA'

'''
Написать скрипт для игры в города

принять на вход название города
определить его последнюю букву
найти в словаре город на эту букву, вывести его на экран, удалить это солово
если не находит - удалить

'''

import random
from dictionary import make_letters_low, show_last_letter, 
                       make_list_with_first_letter
import dictionary


def city_from_user(list_of_cities_names, attempts, first_letter=''):
    cities_with_first_letter = []

    if first_letter:
        cities_with_first_letter = make_list_with_first_letter(list_of_cities_names, first_letter)
        if len(cities_with_first_letter) == 0:
            print(f"Вы проиграли, нет больше городов на букву '{first_letter.capitalize()}' :)")
            return False

    while attempts != 0:
        city = input("Введите название города: ")
        if city.lower() not in list_of_cities_names:
            attempts -= 1
            print(f"Города {city} нет в базе данных! У Вас осталось {attempts} попыток")
        elif not first_letter:
            list_of_cities_names.remove(city.lower())
            return show_last_letter(city)
        elif city.lower() in cities_with_first_letter:
            list_of_cities_names.remove(city.lower())
            return show_last_letter(city)
        else:
            attempts -= 1
            print(f"Город {city} начинается не на букву '{first_letter.upper()}'! Попыток осталось: {attempts}")
    if attempts == 0:
        print("\nВы проиграли, а я выиграл :)")
        return False


def city_from_bot(list_of_cities_names, first_letter):
    cities_with_first_letter = make_list_with_first_letter(list_of_cities_names, first_letter)
    if len(cities_with_first_letter) == 0:
        print("\nВы выиграли:( ")
        return False
    else:
        random_city = random.choice(cities_with_first_letter)
        list_of_cities_names.remove(random_city.lower())
    return random_city.capitalize()


def main():
    cities_names_lower = make_letters_low(dictionary.cities_names)
    last_letter = ''
    while True:
        try:
            user_attempts = 3
            if last_letter:
                last_letter = city_from_user(cities_names_lower, user_attempts, last_letter)
            else:
                last_letter = city_from_user(cities_names_lower, user_attempts)
            if last_letter:
                random_city = city_from_bot(cities_names_lower, last_letter)
                if random_city:
                    print(f"Мой ответ: {random_city}\n")
                    last_letter = show_last_letter(random_city)
                else:
                    break
            else:
                break
        except KeyboardInterrupt:
            print("\n Пока :)")
            return False
    print("\n=== ИГРА ОКОНЧЕНА ===")
    pass


if __name__ == "__main__":
    main()
