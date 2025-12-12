import numpy as np
import itertools
import math
import time
from collections import defaultdict

inp=4

def countArrangement(n):
    perm=np.arange(n)+1
    ps=itertools.permutations(perm)
    ans=0
    for p in ps:
        tmp=0
        for i in range(n):
            if p[i]%(i+1)==0 or (i+1)%p[i]==0:
                tmp+=1
        if tmp==n:
            ans+=1
    return int(ans)

def node(p,stack):
    global valid,used,leng,count
    if len(stack)==leng:
        count+=1
        #print(p,stack)
        return
    for c in valid[p]:
        if used[c]:
            continue
        used[c]=True
        node(p+1,stack+[c])
        used[c]=False
    
def countArrangement(n):
    global perm,valid,used,count,leng
    leng=n
    valid=defaultdict(list)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i%j==0 or j%i==0:
                valid[i].append(j)
    count=0
    used=np.zeros(n+1,dtype=bool)
    node(1,[])
    return count


t=time.time()
print(countArrangement(inp),time.time()-t)