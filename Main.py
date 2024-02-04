import os
import shutil
S = "C:/Users/lenovo/OneDrive/Desktop/HomeWork/1st HW/Files"
D = "C:/Users/lenovo/OneDrive/Desktop/HomeWork/1st HW/MOVE Files"
List = os.listdir(S)
#print(List)
T = 0
for i in List:
    N,E=os.path.splitext(i)
    print(N)
    print(E)
    T = T + 1
print("Total number of document :",T)
