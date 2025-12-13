l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def createListNode(list_):
    Head=None
    Current=ListNode(None)
    for i in list_:
        TMP=ListNode(i)
        Current.next=TMP
        Current=Current.next
        if Head is None:
            Head=Current
    return Head
l1=createListNode(l1)
l2=createListNode(l2)

def AddRemain(lin,Current,remain):
    while lin:
        s=lin.val+remain
        Current.next=ListNode(s%10)
        Current=Current.next
        lin=lin.next
        remain=int(s/10)
    if remain>0:
        Current.next=ListNode(remain)

    return Current
#3ms 73.03%
def addTwoNumbers(l1,l2):
    
    Head=None
    Current=None
    
    s= l1.val+l2.val
    Head=ListNode(s%10)
    Current=Head
    remain=int(s/10)
    l1=l1.next
    l2=l2.next
    
    while l1 is not None and l2 is not None:
        s= l1.val+l2.val+remain
        Current.next=ListNode(s%10)
        remain=int(s/10)
        Current=Current.next
        l1=l1.next
        l2=l2.next
        
    if l1:
        AddRemain(l1,Current,remain)
    else:
        AddRemain(l2,Current,remain)
    return Head    

print(addTwoNumbers(l1,l2))