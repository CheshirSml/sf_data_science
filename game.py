#игра угадай число (guess the number game)
import numpy as np

number = np.random.randint (1, 100)# think of a number

count = 0 #count of try

while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 100\n'))
    
    if predict_number > number:
        print('Число должно быть меньше')
        
    elif predict_number < number:
        print('Число должно быть больше')
        
    else:
        print(f"Вы угадали! Это число = {number}, за {count} попыток")
        break
    
    
    #ttest information - trassh