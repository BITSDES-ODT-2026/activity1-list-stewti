from machine import Pin
import time

a=Pin(35,Pin.OUT)
b=Pin(25,Pin.OUT)
c=Pin(27,Pin.OUT)
d=Pin(22,Pin.OUT)

numby = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

for i in numby(3)
    a.value(i[0])
    b.value(i[1])
    c.value(i[2])
    d.value(i[3])
    time.sleep(0.2)#Create any list
