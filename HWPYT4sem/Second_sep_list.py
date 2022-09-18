# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
#[1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]


start_list = [1,1,1,1,2,2,2,3,3,3,4]

def separ_list_to_uniq_num(list_num):
    """Функция убирает повторяющиеся  элементы из последовательности чисел
    
    оставит только по одному повтору каждого числа
    """
    new_separ_list = []
    for i in list_num:
        if i not in new_separ_list:
            new_separ_list.append(i)
    return new_separ_list

print(separ_list_to_uniq_num(start_list))
