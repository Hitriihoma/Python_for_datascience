import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/Hitriihoma/Python_for_datascience/master/Lab1.csv'
ar1 =  pd.read_csv(url, header=None, error_bad_lines=False).to_numpy()
print(ar1, '\n')
 
ar1_min_coord = np.where(ar1 == np.min(ar1)) # координаты минимального элемента
ar1_max_coord = np.where(ar1 == np.max(ar1)) # координаты максимального элемента

#ar1[ar1_min_coord], ar1[ar1_max_coord] = ar1[ar1_max_coord], ar1[ar1_min_coord] # лёгкий путь

# мне не удобно обходить массивы которые выдаёт np.where()
# поэтому мы помучаемся сейчас чтобы было полегче потом
list_min = [] # для удобства добавления
list_max = [] # для удобства добавления

# удобный список координат минимальных элементов
for i in range(len(ar1_min_coord[0])):
    list_min_temp = np.array([], dtype = int) # для координат i-го минимального
    for j in range(len(ar1_min_coord)):
        list_min_temp = np.append(list_min_temp, ar1_min_coord[j][i])
    list_min.append(list_min_temp.tolist()) # список списков с координатами минимальных элементов

# удобный список координат максимальных элементов
for i in range(len(ar1_max_coord[0])):
     list_max_temp = np.array([], dtype = int) # для координат i-го максимального
     for j in range(len(ar1_max_coord)):
        list_max_temp = np.append(list_max_temp, ar1_max_coord[j][i])   
     list_max.append(list_max_temp.tolist()) # cписок спиcков с координатами максимальных элементов

ar2 = tuple(map(tuple, ar1)) # можно copy(), но кортеж надёжнее
for i in range(len(list_min)):
    ar1[list_min[i][0]][list_min[i][1]] = np.max(ar2) # замена всех мин элементов на макс значение 
for i in range(len(list_max)):
    ar1[list_max[i][0]][list_max[i][1]] = np.min(ar2) # замена всех макс элементов на мин значения 

print(ar1)
