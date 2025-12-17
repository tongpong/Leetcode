import numpy as np
from collections import defaultdict
BusinessLineSet=np.sort(["electronics", "grocery", "pharmacy", "restaurant"])
#
def ToASCII(code):
    code=[ord(c) for c in list(code)]
    return np.array(code)
def checkcode(strcode):
    code=ToASCII(strcode)
    mask1=code==ord('_')
    mask2=(code>=ord("a")) * (code<=ord("z"))
    mask3=(code>=ord("A")) * (code<=ord("Z"))
    mask4=(code>=ord('0')) * (code<=ord('9'))
    #print(strcode,code,mask1,mask2,mask3,mask4,mask1+mask2+mask3+mask4)
    return np.all(mask1+mask2+mask3+mask4)
def validateCoupons(code,businessLine, isActive):
    code_Dict=defaultdict(list)
    ans=[]
    for C,BL,Act in zip(code,businessLine, isActive):
        v1=checkcode(C)
        v2=BL in BusinessLineSet
        if v1 and v2 and Act and len(C)>0:
            code_Dict[BL].append(C)
    for BL in BusinessLineSet:
        ans+=np.sort(code_Dict[BL]).tolist()
    
    return ans
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        return validateCoupons(code,businessLine,isActive)