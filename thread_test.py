import threading ,time

"""
基本写法

t=0
def run(n):
    print(time.time())
    print('run:',n)
    time.sleep(2)

t1=threading.Thread(target=run,args=('thread1',))
t2=threading.Thread(target=run,args=('thread2',))
t1.start()
t2.start()
t1.join()
t2.join()
print('都结束:')

run('thread1')
run('thread2')
print(1527857896.410399-1527857894.4084523)
"""
"""
 类的方式
"""
"""
class myThread(threading.Thread):
    def __init__(self,*args, **kwargs):
        super(myThread,self).__init__()
        self.args=args
        self.kwargs=kwargs
    def run(self):
        print("run task",self.args,self.kwargs)
myThread("test").run()
"""
"""
join等带子线程结束，阻塞主线程

"""

def run(n):
    print(time.time())
    print('run:',n)
    time.sleep(2)
time1= time.time()
for i in range(10):
    t= threading.Thread(target=run ,args=('t-%s'%i,))
    t.setDaemon(True)#把当前线程设置为守护线程，即主线程接触，程序退出，不会等守护线程执行结束 ,场景是，scoketserver，每来一个连接请求，创建一个线程，设置为守护线程，主线程(服务)退出，立即结束，不用等待守护线程结束，守护线程立刻结束，不执行
    # 即主线程结束，每个请求的子线程立刻结束，不用等待子线程执行完成。代码表现，主线程结束，子线程执行一半立刻退出执行/后面代码不执行
    t.start()
    #t.join()

print('cost:' ,time.time()-time1 )

# GIL(global   interpreter lock  ) 全局解释器锁


#


