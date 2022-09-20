__author__ = 'DIANA'


import random
from cities_database import make_letters_low, show_last_letter, make_list_with_first_letter
import cities_database


def handle_city_from_user(list_of_cities_names, attempts, first_letter=''):
    cities_with_first_letter = []

    if first_letter:
        cities_with_first_letter = make_list_with_first_letter(list_of_cities_names, first_letter)
        if not cities_with_first_letter:
            print(f"Вы проиграли, нет больше городов на букву '{first_letter.capitalize()}' :)")
            return False

    while attempts != 0:
        city = input("Введите название города: ")
        if city.lower() not in list_of_cities_names:
            attempts -= 1
            print(f"Города {city} нет в базе данных! Попыток осталось: {attempts}")
        elif not first_letter or city.lower() in cities_with_first_letter:
            list_of_cities_names.remove(city.lower())
            return show_last_letter(city)
        else:
            attempts -= 1
            print(f"Город {city} начинается не на букву '{first_letter.upper()}'! Попыток осталось: {attempts}")
    if attempts == 0:
        print("\nВы проиграли, а я выиграл :)")
        return False


def show_city_from_bot(list_of_cities_names, first_letter):

    cities_with_first_letter = make_list_with_first_letter(list_of_cities_names, first_letter)

    if len(cities_with_first_letter) == 0:
        print("\nВы выиграли:( ")
        return False

    random_city = random.choice(cities_with_first_letter)
    list_of_cities_names.remove(random_city.lower())

    return random_city.capitalize()


def main():
    user_attempts = 3
    cities_names_lower = make_letters_low(cities_database.cities_names)
    last_letter = ''
    for count_step in range(len(cities_database.cities_names)):
        try:
            last_letter = handle_city_from_user(cities_names_lower, user_attempts, last_letter)

            if not last_letter:
                break
            random_city = show_city_from_bot(cities_names_lower, last_letter)

            if not random_city:
                break
            print(f"Мой ответ: {random_city}\n")
            last_letter = show_last_letter(random_city)

        except KeyboardInterrupt:
            print("\n Пока :)")
            return False
    print("\n=== ИГРА ОКОНЧЕНА ===")
    pass


if __name__ == "__main__":
    main()
