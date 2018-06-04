import threading ,time

#全局标志位.模拟红绿灯，和车的行为
event = threading.Event()

#红绿灯行为线程

def red_gren():
    #开始默认绿灯，设置标志位
    count=0
    event.set()
    ct=0
    while True:  
        if count>5 and count<10:
            event.clear()
            print('\33[41;1m red light is waiting \033[0m')
        
        elif count>10:
            event.set()
            count=0
        else :
            print('\33[42;1m green light is going')        
        print('\33[42;1m red light is waiting')
        time.sleep(1)
        count +=1
def car(name):
    while True:
        if event.is_set():
            print('%s going '%name)            
        else:
            print('%s waiting '%name)
            event.wait()
t1=threading.Thread(target=red_gren,args=())
t2=threading.Thread(target=car ,args=('BMW',))
t1.start()
t2.start()