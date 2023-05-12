# Задача 3.1.

# **********************************************************
# Python. Поток 2. Студент Коновченко Александр Михайлович
# **********************************************************

# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

import random

class Matrix:

    def __init__(self, *, row:list=None, rows=10, columns=10, value=0):
        '''Конструктор. Для инициализации может принять список row, 
        либо размеры матрицы rows и columns со значением для заполнения ячеек value'''
        rows: int
        columns: int
        self.table = []
        if(row!=None):
            self.columns = len(row)
            self.rows = self.columns
            for i in range(self.rows):
                self.table.append(row)
        else:
            self.rows = rows
            self.columns = columns
            for i in range(self.rows): 
                self.table.append([value] * self.columns)

    def print(self):
        '''Метод печати матрицы по строкам'''
        print(f'\nМатрица размером {self.rows}x{self.columns}:')
        for i in range(self.rows):
            print(self.table[i])            

    def fill_with_random(self, max_value=100):
        '''Метдо для заполнения матрицы случайными значениями, принимает максимальное значение случайного числа max_value'''
        for i in range(self.rows):
            for j in range(self.columns):
                self.table[i][j] = random.randint(0, max_value)

    def fill_with(self, value=0):
        '''Метод заполнения всех ячеек одинаковыми значениями, принимает для заполнения значение value'''
        for i in range(self.rows):
            for j in range(self.columns):
                self.table[i][j] = value

    def get_row(self, row_index):
        '''Метод получения строки с заданным индексом row_index'''
        if(row_index < 0 or row_index > self.rows-1):
            print('Index out of bounds')
        else:
            return self.table[row_index]

    def set_row(self, row_index, row:list):
        '''Метод установки строки с индексом row_index списком row'''
        if(len(row)!=self.columns):
            print('Длина заменяемой строки не совпадает с количеством столбцов. Добавить такую строку нельзя.')
            return
        else:
            self.table[row_index] = row

    def add_row(self, row:list):
        '''Метод добавления в матрицу заданного списка row. Размер добавляемого списка должен соответствовать 
        количеству имеющихся в матрице столбцов'''
        if(len(row)!=self.columns):
            print('Длина добавляемой строки не совпадает с количеством столбцов. Добавить такую строку нельзя.')
            return
        else:
            self.table.append(row)
            self.rows += 1

    def set_cell(self, row, column, value):
        '''Метод присвоения ячейке с заданными координатами row и column заданного значения value'''
        self.table[row][column] = value

    def get_cell(self, row, column) -> int:
        '''Метод получения значения ячейки с заданными координатами row и column'''
        return self.table[row][column]


m = Matrix(row=[1,2,3,4,5])
m.print()

m.fill_with(73)
m.print()

n = Matrix(rows=4, columns=5)
n.fill_with_random(100)
n.print()

print()
print(n.get_row(2))

n.set_row(2, [777, 777, 777 ,777 ,777])
n.print()

n.add_row([5, 5, 5, 5, 5])
n.print()

n.set_cell(2, 2, 1000)
n.print()