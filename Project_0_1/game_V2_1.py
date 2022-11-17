"""Игра угадай число.
Компьютер сам загадывает и угадывает число.
Если число больше или меньше загаданного, то меняется диапозон.
В итоге выводится количество попыток и среднее значение попыток после 1000 повторений.
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Установливаем рандомное число,
    а потом уменьшаем или увеличиваем его в зависимости от того, 
    больше оно или меньше нужного."""
    
    count = 0 # счетчик кол-ва попыток
    number_Max = 101 # исходное максимальное число из возможных вариантов
    number_Min = 1 # исходное минимальное число из возможных вариантов

    while True: 
        count += 1
    
        predict_number = (number_Min + number_Max)//2 # предполагаемое число
        
        if number < predict_number:
            number_Max = predict_number
        elif number > predict_number:
            number_Min = predict_number
        else: 
            number == predict_number
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

#RUN
if __name__ == '__main__':
    score_game(random_predict)