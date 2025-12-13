# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def search(node,path=[]):
    global Good
    if node is None:
        return
    path.append(node.val)
    if node.val==max(path):
        Good+=1
    search(node.left,path.copy())
    search(node.right,path.copy())
    
        
def goodNodes(root):
    global Good
    #print(root)
    Good=0
    search(root,[])
    return Good