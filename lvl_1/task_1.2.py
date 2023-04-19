#
# РАНХиГС. Python. Поток 2
# Коновченко Александр Михайлович
#

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random
import datetime

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
print('Задача 1.2 A')

songs_long = .0
songs_long_td = datetime.timedelta(0)
i = 0
while i < 3:
    song = random.choice(my_favorite_songs)
    print(song)
    songs_long += song[1]
    songs_long_td += datetime.timedelta(minutes=int(song[1]), seconds=round(song[1] % 1 * 100))
    i += 1

print(f'Три песни звучат {round(songs_long, 2)} минут.')
print(f'Три песни звучат {songs_long_td} минут (с использованием модуля date_time).')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

print('\nЗадача 1.2 B')
songs_long = .0
songs_long_td = datetime.timedelta(0)
i = 0
keys = []
keys = list(my_favorite_songs_dict.keys())
while i < 3:
    song_title = random.choice(keys)
    curr_song_long = my_favorite_songs_dict[song_title]
    print(f'[{song_title}: {curr_song_long}]')
    songs_long += curr_song_long
    songs_long_td += datetime.timedelta(minutes=int(curr_song_long), seconds=round(curr_song_long % 1 * 100))
    i += 1

print(f'Три песни звучат {round(songs_long, 2)} минут.')
print(f'Три песни звучат {songs_long_td} минут (с использованием модуля date_time).')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
