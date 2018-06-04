import queue,time,threading

q = queue.Queue(maxsize=1000)

def producer():
    count = 1
    try:
        while True:
            q.put('骨头%s'%count)
            print('生产骨头%s'%count)
            time.sleep(0.5)
            count+=1
    except Exception as e:
        print(e)


def consumer(name):
    try:
        while True:
            print('%s  取到 [%s]并吃了'%(name,q.get()))
            time.sleep(0.5)
            print('why')
    except Exception as e:
        print(e)



p = threading.Thread(target=producer,args=())
c = threading.Thread(target=consumer,args=('liming',))
c1= threading.Thread(target=consumer,args=('zhangsan',))

p.start()
c.start()
c1.start()
while True:
    pass




