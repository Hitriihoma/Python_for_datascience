import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
 
digits = np.dot(plt.imread('digits.png')[...,:3],[1,1,1]) # вход, изображение
 
D = []
for i in range(8):
    a = i * 48
    x=  (digits[5:104,0+a:48+a] > 1).astype(int).flatten()
    y = (np.array(list(bin(i)[2:].zfill(3))) == '1').astype(int)
    D += [[x,y]]
 
w = np.zeros((D[0][0].shape[0],D[0][1].shape[0])) # инициализация весов
 
β = -0.4 # торможение
 
α = 0.2 # темп обучения
 
σ = lambda x: (x > 1).astype(int) # функция активации
 
def f(x):
    s = β + x @ w
    return σ(s)
 
def train():
    global w
    _w = w.copy()
    for x, y in D:
        i = np.where(x>0)
        w[i] += α * (y - f(x))
    return (w != _w).any()
           
while train():
    print(w) # веса
 
for i in range(8):
    print(f(D[i][0])) # тренировочная
 
def transform_rotate(fi): # fi - degrees
    Dr = []
    for i in range(8):
        a = i * 48
        rotated = ndimage.rotate(digits[5:104,0+a:48+a], fi, reshape=0)
        x = (rotated > 1).astype(int).flatten()
        Dr += [x]
    return Dr
    
print('rotated ratio')
for j in np.arange(0,100,10):
    Dc = []
    for i in range(8):
        Dc.append(np.array_equal(f(D[i][0]), f(transform_rotate(j)[i])))
    print(f'Угол = {j}, Доля совпадений {Dc.count(True)/8}')
    
'''Выход
[0 0 0]
[0 0 1]
[0 1 0]
[0 1 1]
[1 0 0]
[1 0 1]
[1 1 0]
[1 1 1]
rotated ratio
Угол = 0, Доля совпадений 1.0
Угол = 10, Доля совпадений 0.625
Угол = 20, Доля совпадений 0.5
Угол = 30, Доля совпадений 0.375
Угол = 40, Доля совпадений 0.375
Угол = 50, Доля совпадений 0.25
Угол = 60, Доля совпадений 0.25
Угол = 70, Доля совпадений 0.125
Угол = 80, Доля совпадений 0.125
Угол = 90, Доля совпадений 0.0'''    
