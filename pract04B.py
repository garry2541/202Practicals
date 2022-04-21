# Practical 04
# Threading

# Try this Online compiler for this program
# https://www.online-python.com/

import os
import time
import threading
from threading import *

def cal_square(num):
    print("Calculate the square of the given number:") 
    for n in num:
        time.sleep(0.3)
        print("Square is: ",str(n*n)+" ")
  
def cal_cube(num):  
    print("Calculate the cube of the given number:")
    for n in num:
        time.sleep(0.3)
        print("Cube is: ",str(n*n*n)+" ")
  
ar = [4, 5, 6, 7, 2]
  
t = time.time()
th1 = threading.Thread(target=cal_square, args=(ar, ))
th2 = threading.Thread(target=cal_cube, args=(ar, ))
th1.start()
th2.start()

th1.join()
th2.join()
print("Total time taking by threads is : ",time.time() - t)
print("Again executing the main thread")
print("Thread 1 and Thread 2 have finished their execution.")