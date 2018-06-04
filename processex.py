import multiprocessing, time,os


def run(name):
    print('Hello ,%s  ' % name)
    time.sleep(0.5)

if __name__=='__main__':
    """
    
    
    for i in range(10):
        process=multiprocessing.Process(target=run ,args=('process%s %s'%('process',i),))
        process.start()
        process.join()
    """
    print('process id %s'%(os.getppid(),))
