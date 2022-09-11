# 5-Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/yWbkX.)

def get_int(input_string):
    """Эта функция проверяет тип вводных данных
    
    integer, если не подходит выдаёт сообщение об ошибке 
    и просит повторный ввод.
    """
    while type:
        number_int = input(input_string)
        try:
            number_int = int(number_int)
            return number_int
        except ValueError:
            print("Неверный ввод числа!Повторите!")




def fibonacci(number):
    """Функция создаёт список из ряда фибоначи
    
    Если число отрицательное ,то добавляет ноль 
    и отрицательные числа каждого элемента списка.
    """
    arr= [1,1]
    fib1 = 1
    fib2 = 1
    for i in range(abs(number)-2):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        arr.append(fib2)
    if number>0:
        return arr
    else :
        for i in range(len(arr)):
            arr.append(arr[i]*(-1))
        arr.append(0)
        arr.sort()
        return arr
 
print(fibonacci(get_int('')))

