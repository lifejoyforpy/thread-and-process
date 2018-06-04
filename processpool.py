from multiprocessing import  Pool ,Process
import  time,os



def foo(i):
    time.sleep(2)
    print("process : %s"%(os.getppid()))
    return i+100
def Bar(bar): # bar 接收的是foo的return值
    print('done :',bar)

if __name__=='__main__':
    pool= Pool(5) #允许进程池同时放5个进程
    for i in range(10):
        #pool.apply(func=foo ,args=(i,))# apply 串行
        #pool.apply_async(func=foo ,args=(i,))
        pool.apply_async(func=foo, args=(i,),callback=Bar)
    print('end')
    pool.close()
    pool.join()