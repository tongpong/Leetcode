arr=[5,1,1,8,1,6,5,9,7,8]
arr=[0,2,1,4,3]


#1422ms 5.19
def maxChunksToSorted(arr):
    
    arr=np.array(arr)
    sorted_arr=np.sort(arr)
    chunks=np.split(arr, np.arange(len(arr)))
    
    fixed=[]
    counter=0
    st=0
    ed=0
    tmp=[]
    for each in chunks:
        if len(each)==0:
            continue
        tmp+=each.tolist()
        t_size=len(tmp)+len(fixed)
        #print(fixed,tmp)
        if np.all((np.sort(fixed+tmp)-sorted_arr[:t_size])==0):
            fixed+=tmp
            tmp=[]
            counter+=1
    if counter==0:
        return 1
        
    return counter
print(maxChunksToSorted(arr))