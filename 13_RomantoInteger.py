s = "MCMXCIV"

maps={}
maps["I"]=1
maps["V"]=5
maps["X"]=10
maps["L"]=50
maps["C"]=100
maps["D"]=500
maps["M"]=1000
RC=list(maps.keys())
print(RC)
def romanToInt(s):
    ans=0
    level=0
    base=0
    for i in s[::-1]:
        lv=RC.index(i)
        
        if lv>=level:
            level=lv
            ans+=maps[i]
        else:
            ans-=maps[i]
           
        
    return ans
print(romanToInt(s))