username = input('Введите Имя пользователя: ')                      # username - имя пользователя
title = input('Заголовок заметки: ')                                # title - заголовок заметки
content = input('Описание заметки: ')                               # content - описание заметки
status = input('Статус заметки: ')                                  # status - статус заметки
created_date = input('Дата Создания заметки в формате "день-месяц-год": ')          # created_date - дата создания заметки в формате "день-месяц-год", например "10-11-2024"
issue_date = input('Дата Истечения заметки (дедлайн) в формате "день-месяц-год": ') # issue_date - дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024"

print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата Создания заметки в формате "день-месяц-год":', created_date)
print('Дата Истечения заметки (дедлайн) в формате "день-месяц-год":', issue_date)
print('')

temp_created_date = created_date[0:5]   # Временная переменная хранится дата создания без отображения года
temp_issue_date = issue_date[0:5]       # Временная переменная хранится дата дедлайна без отображения года

print('Дата Cоздания заметки в текущем году: ', temp_created_date)
print('Дата Дедлайна заметки в текущем году: ', temp_issue_date)
print('')
