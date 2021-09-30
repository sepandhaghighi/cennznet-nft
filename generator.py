import random
import math
import matplotlib.pyplot as plt
import itertools
import requests

def x_formula(x,y):
    result = random.uniform(-1,1) * math.sqrt((x + y)**2) + math.floor(x - y)
    return result

def y_formula(x,y):
    result = random.uniform(-1,1) * math.sqrt(abs(x-y)) ** 3  + math.ceil(x + y)
    return result
    
def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += step

x_1 = list(float_range(-1 * math.pi,math.pi,0.01))
y_1 = list(float_range(-1 * math.pi,math.pi,0.01))
prod = list(itertools.product(x_1,y_1))
x_2 = []
y_2 = []
seed = random.randint(0,2000)
print("Seed : {0}".format(seed))
for item in prod:
    random.seed(seed)
    x_2.append(x_formula(item[0],item[1]))
    y_2.append(y_formula(item[0],item[1]))
fig = plt.figure()
fig.set_size_inches(10, 10)
ax = fig.add_subplot(111,projection='polar')
ax.set_facecolor("white")
ax.scatter(y_2,x_2,alpha=0.1,c='black',s=0.01)
ax.set_axis_off()
ax.patch.set_zorder(-1)
ax.add_artist(ax.patch)
plt.show()
           
    
    
