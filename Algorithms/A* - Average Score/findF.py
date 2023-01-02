from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import math
with open(r'/Users/nguyenbathiem/Desktop/wordle-project/Wordle_solver/kkk.txt','r') as f:
    lg_data=list()
    for line in f.readlines():
        line = eval(line)
        lg_data.append(line)
final_data=list()
data=defaultdict(list)
for game in lg_data:
    for i in range(len(game)):
        data[game[i][1]].append(len(game)-i)
for point in data.keys():
    data[point] = sum(data[point])/len(data[point])

for k,v in data.items():
    final_data.append((k,v))
print(final_data)