import numpy as np
def problem3x(p):
    x = p[:,0]
    y = p[:,1]
    
    m = len(x)
    n = len(y)
    
    e = []
    z = []
    
    for v in range(2,12):
        if (n>=v) and (m>=v):
            d = np.polyfit(x,y,v-1)
            q = np.polyval(d,x)
            e = y - q
            a = np.linalg.norm(e)
            z.append(a)
        if v==11:
            print(d);