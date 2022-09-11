# 4- Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

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
            print("Неверный ввод числа!")

def binary_translate(number,binary_string = ''):
    """Функция переводит из десятиной системы счисления 
    в двоичную , использует рекурсию.
    """
    if number > 0:
        binary_string += binary_translate(number//2,binary_string) + str(number % 2)
    return binary_string
 
 
print(binary_translate(get_int('Введите искомое число: ')))
