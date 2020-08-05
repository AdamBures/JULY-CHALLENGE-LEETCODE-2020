class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        cur = [root]
        res = collections.deque()
        while cur:
            nxt = []
            res.appendleft([])
            for node in cur:
                res[0].append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right: 
                    nxt.append(node.right)
            cur = nxt
        return list(res)
