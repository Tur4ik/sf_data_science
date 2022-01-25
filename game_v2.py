"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import random


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    auxiliary_number1 = 0
    auxiliary_number2 = 101
    expected_number = random.randint(auxiliary_number1, auxiliary_number2)
    while expected_number != number:
        count += 1
        if expected_number < number:
            auxiliary_number1 = expected_number
            expected_number = random.randint(auxiliary_number1, auxiliary_number2)
        else:
            auxiliary_number2 = expected_number
            expected_number = random.randint(auxiliary_number1, auxiliary_number2)
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = []
    for i in range(1000000):
        random_array.append(random.randint(1, 101))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(sum(count_ls) / 1000000)
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
