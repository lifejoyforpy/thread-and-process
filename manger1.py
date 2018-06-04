from multiprocessing import Process ,Manager
import os

def f(d,l):
    d[1]='1'
    d['2']=2
    d['3']= None
    l.append(os.getpid())
    print(l)

if __name__=='__main__':
    with Manager() as m:
        d=m.dict() # create dict share in Process
        l=m.list(range(5))# create list share in Process
        p_list=[]
        for i in range(10):
            p=Process(target=f ,args=(d,l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)
        print(l)
