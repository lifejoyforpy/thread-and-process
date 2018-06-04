from multiprocessing import Pipe ,Process
# 进程通过数据收发
def f(conn):
    conn.send('hello child')
    conn.close()
if __name__=='__main__':
    pa_conn,ch_conn= Pipe()
    p=Process(target=f ,args=(ch_conn,))
    p.start()
    print(pa_conn.recv())
    p.join()
