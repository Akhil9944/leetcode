class Solution(object):
    def recoverTree(self, root):
        first = second = prev = None
        curr = root
        
        while curr:
            if not curr.left:
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right
                    
        if first and second:
            first.val, second.val = second.val, first.val