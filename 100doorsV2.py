import random
import sys
import os

def toggle(door):
    if door==0:
        door=1
    else:
        door=0
    return door
doors=[0]
for x in range(1, 100):
    doors.append(0)
'''
for object in doors:
    print (object)
print (len(doors))
'''
for x in range(1, 101):
    y=x-1
    while y<100:
        if random.random()>=0.5:
            doors[y] = toggle(doors[y])
        y+=x

print (doors)
print ("A következő ajtók vannak nyitva:\n (Ez a v2 randomizált változat)")
for x in range(0, 100):
    if doors[x]==1:
        print (x+1)
