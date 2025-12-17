import numpy as np
#s="aabcbcbcaccbcaabc"
#p=".*a*aa*.*b*.c*.*a*"

s="mississippi"
p="mis*is*ip*."
s="mississippi"
p="mis*is*p*."
#simplify patten
def encode(s,p):
    n_p=""
    for i,c in enumerate(p[:-1]):
        if c=="*":
            continue
        if p[i+1]=="*":
            c_tmp=c
            if c == ".":
                n_p+="+"
            elif c in s:
                n_p+=c.upper()
        else:
            n_p+=c
    if p[-1]!="*":
        n_p+=p[-1]
    return list(n_p)
           
   
          
def isMatch(s, p):
    global maps,done
    s=list(s)
    p=list(p)
    print(s,p)
    
    p=encode(s,p)
    print(s,p)
    maps=np.zeros([len(s)+1,len(p)+1]).astype(bool)
    done=np.zeros([len(s)+1,len(p)+1]).astype(bool)
    maps[0,0]=True
    for j in range(1,len(p)+1):
        if (p[j-1]>="A" and p[j-1]<="Z") or p[j-1]=="+":
            maps[0,j]=True*maps[0,j-1]
    
    for i in range(1,len(s)+1):
        for j in range(1,len(p)+1):
            
            if (p[j-1]>="A" and p[j-1]<="Z") or p[j-1]=="+":
                if p[j-1]=="+":
                    maps[i,j]=maps[i-1,j] or maps[i,j-1]
                else:
                    print(s[i-1]==p[j-1].lower())
                    
                    maps[i,j]=(maps[i-1,j]*s[i-1]==p[j-1].lower()) or maps[i,j-1] # when *, s[i-1]=p[j-1] if i>j
            else:
                print("char")
                maps[i,j]=maps[i-1,j-1]* (p[j-1]==s[i-1] or p[j-1]==".")
            print(i,j,s[:i],p[:j],p[j-1],maps[i,j])
            print(maps[:i+1,:j+1])
            
            
    print(maps)
    return maps[len(s),len(p)]
print(isMatch(s,p))