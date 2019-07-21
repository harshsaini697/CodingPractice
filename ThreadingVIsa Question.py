import threading
import time
def worker(i):
    time.sleep(i)
    res.append(i)
    return
res=[]
tim=[8,3,5,1,9]
threads=[]
for i in tim:
    t=threading.Thread(target=worker,args=(i,))
    threads.append(t)
    t.start()

time.sleep(25)
print(res)

#[10,2,3,-1,-9,5,-2,7]