# 信号量
# 主要设置为同一时间只能有固定数量执行，比如线城池，约定固定链接数
import threading,time

def test(n): 
    semaphore.acquire()
    time.sleep(1)
    print('task : %s '%n)
    semaphore.release()

if __name__=='__main__':  
    semaphore=threading.BoundedSemaphore(5) #设置信号量
    for i in range(10):
        t=threading.Thread(target=test ,args=('t-%s'%i,))
        t.start()
    while threading.active_count()!=1:
        pass
    else:
        print('end')
