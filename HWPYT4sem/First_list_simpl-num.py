# 1 - Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import def_mslf

number = abs(def_mslf.get_int('Задайте натуральное число: '))

def simple_num(num):
    """составит список простых множителей натуральногочисла num
    """
    list_num = []
    for i in range(2,num+1):
        if i >1 and (i%2 !=0 or i == 2) and (i %3 != 0 or i == 3) and num%i ==0:
            list_num.append(i)
    return list_num

print(simple_num(number))





