# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст. 


file_in = open('HWPYT4sem/RLE_file_in.txt', 'r')
text_in = file_in.read()


def zipping(message):
    cod_message = ''
    previos_symbol = ''
    count = ''
    if not message:
        return ""
    for i in message:
        if i != previos_symbol:
            cod_message+= str(count) + previos_symbol
            count = 1
            previos_symbol = i
        else:
            count+=1
    else:
        cod_message+=str(count) + previos_symbol
        return cod_message

def dezipping(message):
    decode_message = ''
    count = ''
    for i in message:
        if i.isdigit():
            count+=i
        else:
            decode_message+=i*int(count)
            count = ""
    return decode_message

file_out = open('HWPYT4sem/RLE_file_out.txt', 'w')
file_out.write(zipping(text_in))
file_in.close()
file_out = open('HWPYT4sem/RLE_file_out.txt', 'r')

text_crypt = file_out.read()
print(text_crypt)
file_decrypt = open('HWPYT4sem/RLE_dezip.txt', 'w')
file_decrypt.write(dezipping(text_crypt))

file_in.close()
file_out.close()
file_decrypt.close()
