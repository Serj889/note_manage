list_of_titles = []     # Создание списка заголовков
title_00 = '0'

while title_00 != '':       # Запрос заголовка до тех пор пока не будет нажата клавиша ENTER
    print('Введите заголовок заметки, или нажмите ENTER для выхода: ', end='')
    title_00 = input()      # Запрос заголовка от пользователя
    if title_00 == '':      # Проверка нажата ли клавиша ENTER для выхода
        break
    if title_00 not in list_of_titles:      # Просмотр списка заголовков на наличие возможных дублей
        if title_00.isspace():              # Проверка что строка не состоит только из пробелов
            print('Вы ввели пустую строку.')
        else:
            # Добавление нового заголовка в список
            list_of_titles.append(title_00)
    else:
        # Подсказка для пользователя о дублировании заголовков
        print('Такой заголовок уже есть.')

print('')
# Сообщение для пользователя если он не ввел ни одного заголовка
if len(list_of_titles) == 0:
    print('Вы не ввели ни одного заголовка.')
else:
    print('Заголовки заметки:')
    for i in range(len(list_of_titles)):
        # Вывод всех заголовков в столбик
        print('-', list_of_titles[i])
print('')