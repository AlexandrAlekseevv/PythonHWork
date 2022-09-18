# Шифр Цезаря - это способ шифрования, где каждая буква смещается 
# на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция. К примеру, 
# слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.

# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает 
# ключ, считывает текст и дешифровывает его.

import def_mslf

file_caesar = open('HWPYT4sem/text_caesar.txt', 'r', encoding='utf-8')
instruction_caesar = file_caesar.read()

file_caesar.close()

def encrypt_or_decrypt(string_input):
    """Запрашивает у пользователя режим шифрования
    
    зашифровать(e) или дешифровать(d)
    """
    while True:
        choice = input(f"\nВы хотите зашифровать(e) или дешифровать(d)? :{string_input}").lower()
        if choice.startswith("e"):
            vers_crypt = "encrypt"
            return vers_crypt
        elif choice.startswith("d"):
            vers_crypt = "decrypt"
            return vers_crypt 
        else :            
            print('\nВведите латиницей "e" или "d", без кавычек: ')

choice_e_or_d = encrypt_or_decrypt('')
key_lock = def_mslf.get_int("Введите ключ шифрования(целое число): ")

def caesar_crypt(massege,key,mode):
    """зашифровывает и расшифровывает текст
    
    получает на вход текст(massege), ключ шифрования(key), и режим(mode) зашифровать или расшифровать
    """
    if mode == "encrypt":
        crypt_massege = ""
        for i,char in enumerate(massege):
            crypt_massege+=chr(ord(char)+key)
        return crypt_massege
    elif mode == "decrypt":
        decrypt_massege = ""
        for i,char in enumerate(massege):
            decrypt_massege+=chr(ord(char)-key)
        return decrypt_massege

file_caesar = open('HWPYT4sem/text_caesar.txt', 'w', encoding='utf-8')
file_caesar.write(caesar_crypt(instruction_caesar, key_lock, choice_e_or_d))
file_caesar.close()

print(caesar_crypt(instruction_caesar,key_lock,choice_e_or_d))