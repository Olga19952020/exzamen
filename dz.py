#Создать 2 таблицы в Базе данных
#Одна будет хранить текстовые данные(1 колонка)
#Другая числовые(1 колонка)
#Есть список,состоящий из чисел и слов.
#Если элемент списка слово,записать его в соответствующую таблицу,затем посчитать
# длину слова и записать ее в числовую таблицу
#Если элемент списка число:проверить,если число четное записать его в таблицу чисел,
#если нечетное,то записать во вторую таблицу слово:<<нечетное>>
#Если число записей во второй тпблице больше 5,то удалить 1 запись в первой таблице.
#Если меньше,то обновить 1 запись в первой тпблице на <<hello>>
import  sqlite3
conn = sqlite3.connect('name.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tab_1 (id INTEDGER PRIMARY KEY AUTOINCREMENT,col_1 TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS tab_2 (id INTEDGER PRIMARY KEY AUTOINCREMENT,col_1  INTEGER)")
list = ('hello', 'world', 'home', 'apple')
num = (1,2,3,4,5,6,7,8,9,10)
for word in list.split(' '):
    print(len(word))


