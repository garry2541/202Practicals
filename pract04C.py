# Practical 04
# Threading

# This program won't run in Online Compiler
import time
import threading  
from threading import *  

def Ascending(arr):
     for i in range(0, len(arr)):    
         for j in range(i+1, len(arr)):    
             if(arr[i] > arr[j]):
                 temp = arr[i]  
                 arr[i] = arr[j]    
                 arr[j] = temp
     print("Elements of array sorted in Ascending order: " )
     print(arr)

def Descending(arr1):   
     for i in range(0, len(arr1)):    
           for j in range(i+1, len(arr1)):    
                  if(arr1[i] < arr1[j]):    
                      temp = arr1[i]  
                      arr1[i] = arr1[j]    
                      arr1[j] = temp
                      
     print("Elements of array sorted in Descending  order: ")
     print(arr1)
       
arr = [4, 5, 6, 7, 2]
arr1= [54,2,32,67,19]
  
t = time.time()

print("Input for Ascending:",arr)
print("Input for Descending:",arr1)
th1 = threading.Thread(target=Ascending, args=(arr, ))
th2 = threading.Thread(target=Descending, args=(arr1, ))
th1.start()
th1.join()
th2.start()
th2.join()
print("Total time taking by threads is: ",time.time() - t)
print("Again executing the main thread")
print("Thread 1 and Thread 2 have finished their execution")