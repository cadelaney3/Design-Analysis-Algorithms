import random
import time

def sortAnalysis(arr):
    count = 0
    for i in range(1, len(arr)):
        v = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > v:
            count += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = v
    return count

def randomArray(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,n))
    return arr

arraylst = []
for i in range(1,31):
    arraylst.append(randomArray(i * 100))

for idx,item in enumerate(arraylst):
    start_time = time.time()
    print("array_size", idx*100+100, " count = ", sortAnalysis(item), " time = ", time.time() - start_time)
