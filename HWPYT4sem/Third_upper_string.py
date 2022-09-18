# 3 - В файле, содержащем фамилии студентов и их оценки, 
# изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».

# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4


file = open('HWPYT4sem/text.txt','r', encoding='utf-8')
list_of_studend = file.read().split('\n')


def name_upper(st):
    """Проверяет оценку студента 
    
    если оценка больше 4 баллов, меняет буквы в имени на заглавные
    """
    check_list = ""
    for list_lines in st:
        for index_listlines in list_lines:
            if int(list_lines[-1])>4:
                index_listlines = str(index_listlines).upper()
            check_list+= str(index_listlines)
        check_list+="\n"
    print(check_list)
    return check_list


file_out = open('HWPYT4sem/text_out.txt','w', encoding='utf-8')
file_out.write(name_upper(list_of_studend))

file.close()
file_out.close()
