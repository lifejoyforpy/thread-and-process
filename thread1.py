import threading
import time
zero = 0
def change_zero():
    global zero
    for i in range(1000000):
        zero = zero + 1
        zero = zero - 1

th1 = threading.Thread(target = change_zero)
th2 = threading.Thread(target = change_zero)
th1.start()
th2.start()
th1.join()
th2.join()
print(zero)

