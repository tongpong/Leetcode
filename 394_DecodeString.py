import numpy
from collections import defaultdict
s="3[a2[c]1[de]]"

#s="3[a]2[bc]"

def construst(s,banket,offset=0):
    print("in",s)
    i=0
    ans=""
    num_st=""
    while i<len(s):
        c=s[i]
        if c >="0" and c <="9":
            num_st+=c
        elif c =="[":
            st=i+offset
            j=banket[st]-offset
            subs=construst(s[i+1:j-1],banket,offset+i+1)
            for a in range(int(num_st)):
                ans+=subs
            print("layer",offset,s[i+1:j-1],num_st,subs,ans)
            num_st=""
            i=j-1
            
        else:
            ans+=c
        i+=1
    #print("out",ans,num_st)
    return ans
def decodeString(s):
    level=0
    banket={}
    trees=defaultdict(list)
    num_st=""
    for i,c in enumerate(s):
        if c =="[":
            
            trees[level].append([i,-1])
            level+=1
            num_st=""
        elif c == "]":
            level-=1
            trees[level][-1][1]=i+1
            st,ed=tuple(trees[level][-1])
            banket[st]=ed
        i+=1
    print(trees,banket)
    return construst(s,banket)
        
print(decodeString(s))