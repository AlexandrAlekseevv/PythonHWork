


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
 


def get_float(input_string):
    """Эта функция проверяет тип вводных данных
    
    float, если не подходит выдаёт сообщение об ошибке 
    и просит повторный ввод.
    """
    while type:
        number_float = input(input_string)
        try:
            number_float = float(number_float)
            return number_float
        except ValueError:
            print("Неверный ввод числа!")
