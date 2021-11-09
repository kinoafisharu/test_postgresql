from tkinter import *
from test_functions import *

root = Tk()

root.geometry('900x400+400+50')
root.title(' Тесты для PostgreSQL.ru ')

global category_id_selected
global product_id_selected


def hello():
    print("hello!")


mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="1. Создание базы данных postgres_db", command=create_database_postgres_db)
filemenu.add_command(label="2. Информация о сервере базы данных PostgreSQL", command=postgres_info)
filemenu.add_command(label="3. Создание таблицы str_articles в БД PostgreSQL", command=create_table_str_articles)
filemenu.add_separator()
filemenu.add_command(label="4. Занесение в таблицу str_articles в БД PostgreSQL записей из файла str_articles_part1.sql", command=read_sql_1)
filemenu.add_command(label="5. Количество записей в таблице str_articles в БД PostgreSQL", command=count_records_1)
filemenu.add_command(label="6. Удаление всех записей из таблицы str_articles в БД PostgreSQL", command=delete_records_1)
filemenu.add_command(label="7. Вывод всех записей из таблицы str_articles в текстовый файл", command=print_records_1)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=root.quit)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="1. Модули для БД Sqlite3", command=hello)
helpmenu.add_command(label="2. Информация о базе данных БД Sqlite3", command=sqlite3_info)
helpmenu.add_command(label="3. Создание таблицы str_articles в БД Sqlite3", command=create_table_str_articles_sqlite3)
helpmenu.add_separator()
helpmenu.add_command(label="4. Занесение в таблицу str_articles в БД Sqlite3 записей из файла str_articles_part1.sql", command=read_sql)
helpmenu.add_command(label="5. Количество записей в таблице str_articles в БД Sqlite3", command=count_records_3)
helpmenu.add_command(label="6. Удаление всех записей из таблицы str_articles в БД Sqlite3", command=delete_records_3)
helpmenu.add_command(label="7. Вывод всех записей из таблицы str_articles в текстовый файл", command=print_records_3)


reportsmenu = Menu(mainmenu, tearoff=0)
reportsmenu.add_separator()
# reportsmenu.add_command(label="Количество любимых продуктов по категориям", command=utl_products_category_favorite)
reportsmenu.add_separator()
reportsmenu.add_command(label="         По избранным ")

utilitmenu = Menu(mainmenu, tearoff=0)
utilitmenu.add_command(label="Вывод всех таблиц в БД PostgreSQL", command=list_tables)
utilitmenu.add_separator()
utilitmenu.add_command(label="    Одноразовые утилиты")
utilitmenu.add_separator()

testmenu = Menu(mainmenu, tearoff=0)
testmenu.add_command(label="Тест read_csv() для 'str_articles_part2.sql'   ", command=read_csv)
testmenu.add_command(label="Тест read_inp() для 'str_articles_part2.sql'   ", command=read_inp)
testmenu.add_command(label="Тест read_sql() для 'str_articles_part1.sql'   ", command=read_sql)
testmenu.add_separator()
testmenu.add_command(label="Тест read_sql() для 'str_articles_part1.sql'   ", command=list_simbols)


mainmenu.add_cascade(label="Работа с PostgreSQL", menu=filemenu, font=('Arial', 10))
mainmenu.add_cascade(label="Работа с Sqlite3", menu=helpmenu)
mainmenu.add_cascade(label=" Отчеты ", menu=reportsmenu)
mainmenu.add_cascade(label="Тесты для PostgreSQL", menu=utilitmenu)
mainmenu.add_cascade(label="Тесты для Sqlite3", menu=testmenu)

root.mainloop()
