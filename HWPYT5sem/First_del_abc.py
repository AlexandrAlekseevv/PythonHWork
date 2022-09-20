# 1- Напишите программу, удаляющую из текста все слова, 
# содержащие ""абв"".

#'абвгдейка - это передача' = >" - это передача"

file_text= open('HWPYT5sem/text/First_task_text.txt', 'r', encoding='utf-8') 
text_abc = file_text.read().split()#не разобрался как сохранить перенос строк. readline() только первую строку выводит,не смог зациклить,пробовал через while True:

file_text.close()                             

def delete_abc(text):
    """
    Удаляет слово , если отно начинается с "абв"
    """
    if not( str(text).lower().startswith('«абв') or str(text).lower().startswith('абв')):
       return str(text)


file_answer = open('HWPYT5sem/text/First_task_answer.txt', 'w', encoding='utf-8')
file_answer.write(" ".join(filter(delete_abc,text_abc)))
file_answer.close()

print(" ".join(filter(delete_abc,text_abc)))