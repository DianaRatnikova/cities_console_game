cities_names = ["Астрахань", "Астана", "Быдгощ", "Берлин", "Будапешт",
                "Воронеж", "Вроцлав", "Гданьск", "Гамбург", "Дрезден",
                "Дюссельдорф", "Екатеринбург", "Женева", "Зальцбург",
                "Йошкар-Ола", "Набережные челны"]

impossible_first_letters = ["ы", "ь", "ъ"]


def make_letters_low(cities_names):
    cities_names_lower = [name.lower() for name in cities_names]
    return cities_names_lower


def show_last_letter(city_name):
    for (index, letter) in enumerate(city_name):
        if city_name.lower()[-(index+1)] not in impossible_first_letters:
            return city_name.lower()[-(index+1)]


def make_list_with_first_letter(list_of_cities_names, first_letter):
    cities_with_first_letter = [city.lower() for city in list_of_cities_names if city[0].lower() == first_letter]
    return cities_with_first_letter
