# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

arr = [2,3,4,5,6,8,10]

def product_of_pairs(num_list):
    """Функция считает произведение пар чисел списка
    
    первого и последнего элемента , если количество элементов нечётное 
    средний элемент умнажает на себя.
    """
    list_prod=[]
    for i in range(1,int(((len(num_list))/2)+1.5)):
        
        prod_pair = num_list[i-1]*num_list[(-1)*i]
        list_prod.append(prod_pair)
        
    return list_prod

print(product_of_pairs(arr))