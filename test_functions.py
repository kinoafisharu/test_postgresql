superuser_password = ""

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import csv


import time
import datetime
from datetime import date


import sqlite3
from sqlite3 import Error
from random import randint
from tkinter import messagebox
# import matplotlib.pyplot as plt

# import shutil

print('Модуль test_functions')


def create_connection_postgresql(superuser_password):
    if len(superuser_password) == 0:
        print('Не указан пароль суперюзера postres в первой строчке файла test_functions.py')
        exit()
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password = superuser_password,
                                      host="127.0.0.1",
                                      port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        print("Успешное соединение с базой данных PostgreSQL")
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        pass
        # if connection:
        #    cursor.close()
        #    connection.close()
        #    print("Соединение с PostgreSQL закрыто")
    return connection


def create_connection(path):
    connection_sqlite3 = None
    try:
        connection_sqlite3 = sqlite3.connect(path)
        print("Успешное соединение с базой данных SQLite3     " + path)
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection_sqlite3


connection_sqlite3 = create_connection("test.db")
cursor_sqlite3 = connection_sqlite3.cursor()


connection = create_connection_postgresql(superuser_password)
cursor = connection.cursor()


def execute_query(connection, query):
    cursor_ = connection.cursor()
    try:
        cursor_.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def create_database_postgres_db():
    try:
        sql_create_database = 'create database postgres_db'
        cursor.execute(sql_create_database)
    # except psycopg2.errors.DuplicateDatabase:
    #     print'база данных "postgres_db" уже существует')
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    return True


def postgres_info():
    try:
        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(connection.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    return True


def sqlite3_info():
    try:
        print("Информация о БД Sqlite3")
        # Выполнение SQL-запроса
        cursor_sqlite3.execute("SELECT sqlite_version();")
        # Получить результат
        record = cursor_sqlite3.fetchone()
        print("Вы подключены к - ", record, "\n")
    except (Exception, Error) as error:
        print("Ошибка при работе с БД Sqlite3", error)
    return True


def create_table_mobile():
    try:
        # SQL-запрос для создания новой таблицы
        create_table_query = '''CREATE TABLE mobile
                                  (ID INT PRIMARY KEY     NOT NULL,
                                  MODEL           TEXT    NOT NULL,
                                  PRICE         REAL); '''
        # Выполнение команды: это создает новую таблицу
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица mobile успешно создана в PostgreSQL")
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    return


def delete_records(connection2):
    try:
        query = "DELETE FROM str_articles"
        cursor2 = connection2.cursor()
        cursor2.execute(query)
        connection2.commit()
        print("Все записи из таблицы str_articles удалены")
    except (Exception, Error) as error:
        print("Ошибка при работе с БД:", error)
    return


def delete_records_1():
    delete_records(connection)
    return


def delete_records_3():
    delete_records(connection_sqlite3)
    return


def create_table_str_articles_sqlite3():
    try:
        query_create_str_articles = """
            CREATE TABLE str_articles(
            id int NOT NULL,
            `type` integer NOT NULL,
            `name` text NOT NULL,
            `text` mediumtext NOT NULL,
            `date` datetime NOT NULL,
            `user` int NOT NULL,
            `flag_del` int NOT NULL,
            `count` int NOT NULL DEFAULT '0',
            `view` int NOT NULL,
            `plus` int NOT NULL,
            `minus` int NOT NULL,
            `money` int NOT NULL,
            `flags` varchar(6) NOT NULL,
            `date_r` datetime NOT NULL
            )
            """
        # Выполнение команды: это создает новую таблицу
        cursor_sqlite3.execute(query_create_str_articles)
        print("Таблица str_articles успешно создана в Sqlite3")
        connection_sqlite3.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с Sqlite3:", error)
    return


def create_table_str_articles():
    # PostgreSQL
    query_create_str_articles = """
    CREATE TABLE str_articles(
    id int NOT NULL,
    type int NOT NULL,
    name text NOT NULL,
    text text NOT NULL,
    date timestamp NOT NULL,
    user1 INT NOT NULL,
    flag_del int NOT NULL DEFAULT '0',
    count int NOT NULL DEFAULT '0',
    view int NOT NULL,
    plus int NOT NULL,
    minus int NOT NULL,
    money int NOT NULL,
    flags varchar(6) NOT NULL,
    date_r timestamp NOT NULL
    );
    """
    try:
        cursor.execute(query_create_str_articles)
        connection.commit()
        print("Таблица str_articles успешно создана в PostgreSQL")
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    return

    return


def create_table():
    create_table_mobile()
    return


def insert_into_str_articles_sqlite3(tuple11):
    query_ins = """
    INSERT INTO `str_articles` (
    `id`,
    `type`,
    `name`, 
    `text`, 
    `date`, 
    `user`, 
    `flag_del`, 
    `count`, 
    `view`, 
    `plus`, 
    `minus`, 
    `money`, 
    `flags`, 
    `date_r`) 
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """
    cursor_sqlite3.execute(query_ins, (tuple11))
    connection_sqlite3.commit()
    return


def read_csv():
    with open('str_articles_part2.sql', newline='') as file_csv:
        reader = csv.reader(file_csv)
        for row in reader:
            print(row)
    return


def count_records_str_articles(variand_db):
    if variand_db == 3:
        connection2 = connection_sqlite3
        db_name = 'Sqlite3'
    else:
        connection2 = connection
        db_name = 'PostgreSQL'
    cursor2 = connection2.cursor()
    cursor.execute("SELECT COUNT(*) FROM str_articles")
    row = cursor.fetchone()
    if row is not None:
        return row[0]
    else:
        return 0


def count_records_sqlite3():
    cursor_sqlite3.execute("SELECT COUNT() FROM str_articles")
    row = cursor_sqlite3.fetchone()
    if row is not None:
        return row[0]
    else:
        return 0


def count_records_1():
    r = count_records_str_articles(1)
    print('В таблице str_articles БД PostgreSQL записей =', r)
    return


def count_records_3():
    r = count_records_sqlite3()
    print('В таблице str_articles записей =', r)
    return


def write_row11(row, f_out):
    f_out.write(' '  + "\n")
    f_out.write('- ' * 35  + "\n")
    f_out.write('id = ' + str(row[0]) + ', type = ' + str(row[1])+ ', name = ' + row[2] + "\n")
    f_out.write('text = ' + "\n")
    s = row[3]
    while len(s) > 0:
        if len(s) > 80:
            s1 = s[:80]
            s = s[80:]
            f_out.write(s1 + "\n")
        else:
            f_out.write(s + "\n")
            break
    d = row[4]
    df = d.strftime("%Y-%m-%d %H:%M:%S")
    # print('line 295 type("datetime.datetime")', type(d), d, df, type(df))
    f_out.write('date = ')
    f_out.write(df )
    f_out.write(', user = ' + str(row[5]) + ', flag_del = ' + str(row[6]) )
    f_out.write(', count = ' + str(row[7]) + ', view = ' + str(row[8]) + '\n')
    f_out.write('plus = ' + str(row[9]) + ', minus = ' + str(row[10]) + ', money = ' + str(row[11]))
    f_out.write(' flags = ' + str(row[12]) + ', date_r = ' + row[13].strftime("%Y-%m-%d %H:%M:%S") + '\n')

    return


def print_records(variand_db):
    if variand_db == 3:
        connection2 = connection_sqlite3
        file_name = '_results_Sqlite3.txt'
        db_name = 'Sqlite3'
    else:
        connection2 = connection
        file_name = '_results_PostgreSQL.txt'
        db_name = 'PostgreSQL'
    try:
        query = "SELECT * FROM str_articles"
        cursor2 = connection2.cursor()
        cursor2.execute(query)
        with open(file_name, 'w') as f_out:
            f_out.write('База данных: ' + db_name + "\n")
            row = cursor2.fetchone()
            if row is None:
                print('Таблица пуста ')
            while row is not None:
                if len(row) == 0:
                    break
                # print(row)
                write_row11(row, f_out)
                row = cursor2.fetchone()
    except (Exception, Error) as error:
        print("Ошибка при выводе в файл:", error)
    print('Конец вывода в файл ' + file_name)
    return


def print_records_1():
    print_records(1)
    print('Создан файл _results_PostgreSQL.txt')
    return


def print_records_3():
    # print_records(connection_sqlite3)
    print_records(3)
    print('Создан файл _results_Sqlite3.txt')
    return


def read_inp():
    # Если файла нет, возвращает 0, иначе 1
    print('function read_inp ')
    file_inp_dir = 'str_articles_part2.sql'
    try:
        f = open(file_inp_dir, encoding='utf-8-sig')
    except FileNotFoundError:
        #        f.close()
        return 0

    n = 0
    m = 0
    for line in f:
        m = m + 1
        s = line
        s = s[1:-3]
        print()

        print(s)
        tuple11 = s
        print(m, type(tuple11))
        list2 = s.split(',')
        print(list2)
        if m > 1:
            break
        # insert_into_str_articles_sqlite3(tuple11)
    return


def read_sql():
    print('Function  read_sql()', 'Start')
    with open('str_articles_part1.sql', encoding='utf-8-sig') as f:
        str_sql = f.read()
        str_sql = str_sql.replace(r"\'", '"')
        n = 0
        p = str_sql.find('INSERT', 1)
        while p > 0:
            n += 1
            str_sql_1 = str_sql[:p]
            str_sql = str_sql[p:]
            # print()
            # print()
            # print(n, str_sql_1)
            cursor_sqlite3.execute(str_sql_1)
            p = str_sql.find('INSERT', 1)
            if p < 0:
                if str_sql.startswith('INSERT'):
                    cursor_sqlite3.execute(str_sql)
        # cursor_sqlite3.executemany(str_sql)
        connection_sqlite3.commit()
        print('Function  read_sql()', 'End')
        return


def read_sql_1():
    print('Function  read_sql_1() for DB PostgreSQL', 'Start')
    with open('str_articles_part1.sql', encoding='utf-8-sig') as f:
        str_sql = f.read()
        str_sql = str_sql.replace(r"\'", '"')
        str_sql = str_sql.replace("`str_articles`", "str_articles")
        str_sql = str_sql.replace("`user`", "user1")
        str_sql = str_sql.replace("`", "")
        str_sql = str_sql.replace("'0000-00-00 00:00:00'", "'2000-01-01 00:00:01'")
        n = 0
        p = str_sql.find('INSERT', 1)
        while p > 0:
            n += 1
            str_sql_1 = str_sql[:p]
            str_sql = str_sql[p:]
            # print()
            # print()
            # print(n, str_sql_1)
            cursor.execute(str_sql_1)
            p = str_sql.find('INSERT', 1)
            if p < 0:
                if str_sql.startswith('INSERT'):
                    cursor.execute(str_sql)
        connection.commit()
        print('Function  read_sql_1() for DB PostgreSQL', 'End')
        return


def list_tables():
    return


def list_simbols():
    print('Тест кавычек')
    x = "`"
    print(x, "from sql обратная ковычка, ord()=", ord(x))

    x = "'"
    print(x, "from sql прямая ковычка, ord()=", ord(x))

    return

