# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют 
# два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""





from random import randint
import def_mslf


candes = def_mslf.get_int('Сколько всего будет конфет?: ')

maxsum= def_mslf.get_int('Сколько максимум конфет можно будет взять за один ход?: ')

def skynet(candyes,max_s):
    skynet_num = max_s
    win_num = []
    for i in range(1,(candyes//(max_s+1))+1):
        win_num.append(((max_s+1)*i)+1)
    #print( win_num)
    if candyes<=max_s:
        skynet_num= candyes-1
        if candyes ==1:
            return candyes
        return skynet_num
    while ((candyes-skynet_num) not in win_num) :
        skynet_num-=1
        if skynet_num == 1:
            return randint(1,max_s)
    return skynet_num


def gameplay(candyes):
    while candyes>0:
        player= "first_player"    
        while player.startswith('f'):
            print(f"\nВ игре {candyes} конфет")
            candyes -=Do_u_wanna_candy('',maxsum)
            #candyes -=skynet(candyes,maxsum) #  забавно)
            player = "second_player"
        if candyes>0: 
            skynet_move=skynet(candyes,maxsum)
            candyes-=skynet_move
            print(f"Противник взял {skynet_move} конфет,осталось {candyes} конфет")
            if candyes==0:
                print("\nYOU WIN"*5)
    if player.startswith('f'):
        print("\nYOU LOOSE "*5)


def Do_u_wanna_candy(input_string,max_candy):
    while True:
        while type:
            number_int = input(f"\nВозьмите не более {max_candy} конфет: {input_string}")
            try:
                number_int = int(number_int)
                if 0<number_int<(max_candy+1):
                    print(f"\nВы взяли {number_int} конфет")
                    return number_int       
                elif 0>number_int :            
                    print('\nЖаль,но возвращать конфеты нельзя')
                elif number_int == 0:
                    print("\nПропустить ход не получится! Смелее!")
                else:
                    print(f"\nНе жадничайте!Можно взять не больше {max_candy}")
            except ValueError:
                print("\nНеверный ввод числа!")


gameplay(candes)