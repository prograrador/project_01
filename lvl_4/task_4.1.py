# Задача 4.1.
# Домашнее задание на SQL

# **********************************************************
# Python. Поток 2. Студент Коновченко Александр Михайлович
# **********************************************************

# В базе данных teacher создайте таблицу Students
# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)
# Наполните таблицу следующими данными:
# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def execute_query(sql):
    try:
      connection = get_connection()
      cursor = connection.cursor()
      cursor.execute(sql)
      connection.commit()
    except (Exception, sqlite3.Error) as error:
      print("Ошибка при выполнении SQL запроса: ", error)
    finally:
      close_connection(connection)
      

def create_and_fill_students():
  sqlquery = """CREATE TABLE Students
                  (
                    Student_Id int NOT NULL PRIMARY KEY,
                    Student_Name varchar(80) NOT NULL,
                    School_Id int NOT NULL
                  );"""
  execute_query(sqlquery)
  sqlquery = """INSERT INTO Students (Student_Id , Student_Name , School_Id)
                    VALUES
                    (201, 'Иван', 1),
                    (202, 'Петр', 2),
                    (203, 'Анастасия', 3),
                    (204, 'Игорь', 4);"""
  execute_query(sqlquery)

#create_and_fill_students()

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.
# Формат вывода:
# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

def get_student_by_id(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = """SELECT Student_Id, Student_Name, School_Id, School_Name 
                  FROM Students NATURAL JOIN School
                  WHERE Student_Id = ?;"""
    cursor.execute(sqlquery,(student_id,))
    record = cursor.fetchone()
    print ("Данные по студенту")
    print ("ID студента:", record[0])
    print ("Имя студента:", record[1])
    print ("ID школы:", record[2])
    print ("Название школы:", record[3])
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)
  finally:
    close_connection(connection)

get_student_by_id(203)

