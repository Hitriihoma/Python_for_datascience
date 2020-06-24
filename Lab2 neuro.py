import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from scipy import ndimage


#img = np.loadtxt(fname='image.csv', delimiter=',')
train_numbers = np.random.choice(10,7,False) # in arange(10), 7 random elements, replace=False (unique)
check_numbers = np.delete(np.arange(10), train_numbers)
#img = plt.imread('1.jpg')

Y = np.array([])
for i in range(train_numbers.size):
    Y = np.append(Y, 1 if train_numbers[i] % 2 == 0 else 0)
Y_check = np.array([])
for i in range(check_numbers.size):
    Y_check = np.append(Y_check, 1 if check_numbers[i] % 2 == 0 else 0)
D = np.array([])    
for i in range(train_numbers.size):
    #print(i)
    j=train_numbers[i]
    D = np.append(D, np.loadtxt(fname=f'image{j}.csv', delimiter=','))
    #print(D)
    #print()
D = D.reshape((7,25)) 
#print(D)   
w = np.ones(25)

D_check = np.array([])
for i in range(check_numbers.size):
    j=check_numbers[i]
    D_check = np.append(D_check, np.loadtxt(fname=f'image{j}.csv', delimiter=','))
D_check = D_check.reshape((3,25)) 



#D = np.array( [ [0,0,1], [0,1,0] ])
#Y = np.array([0,1])
#w = np.ones(3)
alpha = 0.2 #темп
beta = -0.4 #торможение

sigma = lambda x: 1 if x > 0 else 0

def f(x):
    s = beta + np.sum(x @ w)
    return sigma(s)


def train():
    global w
    _w = w.copy()
    for x,y in zip(D, Y):
        w += alpha * (y-f(x)) * x
    return ( w != _w).any()

while train():
    print(w)

for i in range(check_numbers.size):
    #print(i)
    j=check_numbers[i]
    print(j, np.sum(D_check[i] @ w))

print()
print(train_numbers)
print(Y)
print(check_numbers)
print(Y_check)
print(w.shape)


#plt.imsave(fname='11.png', arr=transformed)
#plt.imshow(img)