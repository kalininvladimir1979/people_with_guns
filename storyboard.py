import imageio


# РАСКАДРОВКА

# Видео 1
nr1 = 5 # Переменная для определения шага раскадровки для видео 1
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\test1.mp4") # Указываем путь к видео 1

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr1 == 0: # шаг nr1 кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка1\\{}.jpg'.format(frame_number), im) # Указываем путь к папке для раскадровки видео 1


# Видео 2
nr2 = 24 # Переменная для определения щага раскадровки
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\test2.mp4")

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr2 == 0: # шаг nr кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка2\\{}.jpg'.format(frame_number), im)


# Видео 3
nr3 = 5 # Переменная для определения щага раскадровки
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\test3.mp4")

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr3 == 0: # шаг nr кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка3\\{}.jpg'.format(frame_number), im)


# Видео 4
nr4 = 5 # Переменная для определения щага раскадровки
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\test4.mp4")

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr4 == 0: # шаг nr кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка4\\{}.jpg'.format(frame_number), im)


# Видео 5
nr5 = 5 # Переменная для определения щага раскадровки
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\test5.mp4")

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr5 == 0: # шаг nr кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка5\\{}.jpg'.format(frame_number), im)


# Видео 6
nr6 = 100 # Переменная для определения щага раскадровки
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\test6.avi")

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr6 == 0: # шаг nr кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка6\\{}.jpg'.format(frame_number), im)


# Видео 7
nr7 = 100 # Переменная для определения щага раскадровки
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\test7.avi")

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr7 == 0: # шаг nr кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка7\\{}.jpg'.format(frame_number), im)


# Видео 8
nr8 = 5 # Переменная для определения щага раскадровки
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\test8.mp4")

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr8 == 0: # шаг nr кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка8\\{}.jpg'.format(frame_number), im)


# Видео 9
nr9 = 10 # Переменная для определения щага раскадровки
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\test9.mp4")

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr9 == 0: # шаг nr кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка9\\{}.jpg'.format(frame_number), im)


# Видео 10
nr10 = 3  # Переменная для определения щага раскадровки
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\test10.avi")

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr10 == 0: # шаг nr кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка10\\{}.jpg'.format(frame_number), im)

# Видео 11
nr11 = 1  # Переменная для определения щага раскадровки
reader = imageio.get_reader("D:\\Программирование\\Сет с оружием\\Сет с оружием\\video11.mov")

for frame_number, im in enumerate(reader): # Сохраняем кадры
    if frame_number % nr11 == 0: # шаг nr кадров
      imageio.imwrite('D:\\Программирование\\Сет с оружием\\Раскадровка11\\{}.jpg'.format(frame_number), im)


# Подсчет получившихся изображений
import os

# Присваиваем переменным значения путецй к папкам для сохранения раскадровок

path1 = 'D:\Программирование\Сет с оружием\Раскадровка1'
path2 = 'D:\Программирование\Сет с оружием\Раскадровка2'
path3 = 'D:\Программирование\Сет с оружием\Раскадровка3'
path4 = 'D:\Программирование\Сет с оружием\Раскадровка4'
path5 = 'D:\Программирование\Сет с оружием\Раскадровка5'
path6 = 'D:\Программирование\Сет с оружием\Раскадровка6'
path7 = 'D:\Программирование\Сет с оружием\Раскадровка7'
path8 = 'D:\Программирование\Сет с оружием\Раскадровка8'
path9 = 'D:\Программирование\Сет с оружием\Раскадровка9'
path10 = 'D:\Программирование\Сет с оружием\Раскадровка10'
path11 = 'D:\Программирование\Сет с оружием\Раскадровка11'


# Подсчитываем количество полученных изображений

count1 = 0
for root, dirs, files in os.walk(path1):
    count1 += len(files)

count2 = 0
for root, dirs, files in os.walk(path2):
    count2 += len(files)

count3 = 0
for root, dirs, files in os.walk(path3):
    count3 += len(files)

count4 = 0
for root, dirs, files in os.walk(path4):
    count4 += len(files)

count5 = 0
for root, dirs, files in os.walk(path5):
    count5 += len(files)

count6 = 0
for root, dirs, files in os.walk(path6):
    count6 += len(files)

count7 = 0
for root, dirs, files in os.walk(path7):
    count7 += len(files)

count8 = 0
for root, dirs, files in os.walk(path8):
    count8 += len(files)

count9 = 0
for root, dirs, files in os.walk(path9):
    count9 += len(files)

count10 = 0
for root, dirs, files in os.walk(path10):
    count10 += len(files)

count11 = 0
for root, dirs, files in os.walk(path11):
    count11 += len(files)

# Выводим подсчитанное количество полученных изображений в папкахз

print("Количество файлов в папке1:", count1)
print("Количество файлов в папке2:", count2)
print("Количество файлов в папке3:", count3)
print("Количество файлов в папке4:", count4)
print("Количество файлов в папке5:", count5)
print("Количество файлов в папке6:", count6)
print("Количество файлов в папке7:", count7)
print("Количество файлов в папке8:", count8)
print("Количество файлов в папке9:", count9)
print("Количество файлов в папке10:", count10)
print("Количество файлов в папке11:", count11)