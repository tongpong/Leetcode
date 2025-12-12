n=25633
import time 
import numpy as np
#1832ms 5.89%
def countCoveredBuildings(n,buildings):
    buildings=np.array(buildings)
    edges_x=np.zeros(len(buildings))
    edges_y=np.zeros(len(buildings))
    
    x_dict={}
    y_dict={}
    for i,b in enumerate(buildings):
        x,y=tuple(b.tolist())
        if x not in x_dict: 
            x_dict[x]={}
        x_dict[x][y]=i
        
        if y not in y_dict: 
            y_dict[y]={}
        y_dict[y][x]=i
    for x in x_dict:
        s=np.sort(list(x_dict[x].keys()))
        idxs=x_dict[x][s[0]]
        edges_x[idxs]=1
        idxs=x_dict[x][s[-1]]
        edges_x[idxs]=1
    
    for y in y_dict:
        s=np.sort(list(y_dict[y].keys()))
        idxs=y_dict[y][s[0]]
        edges_y[idxs]=1
        idxs=y_dict[y][s[-1]]
        edges_y[idxs]=1
    edges=edges_x+edges_y
    return int(np.sum(edges==0))
t=time.time()
print(countCoveredBuildings(n,buildings),time.time()-t)
    
