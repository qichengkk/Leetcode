class Solution:
    def levelOrder(self, root):
        result = []
        if root == None:
            return result
        current = [root]
        while len(current) > 0:
            # Python is just so slow, but who I can complain? I have to write following code to optimize for skewed tree 
            # -- None of the code from this tag to the next tag is actually needed -- #
            if len(current) == 1 and (current[0].left == None or current[0].right== None):
                this_node = current[0]
                result.append([this_node.val])
                if this_node.left == None and this_node.right != None:
                    current = [this_node.right]
                elif this_node.left != None and this_node.right == None:
                    current = [this_node.left]
                else:
                    current.pop(0)
            else:
            # -- None of the code above this tag up to the previous tag is actually needed -- #
                vals = []
                size = len(current)
                for i in range(size):
                    this_node = current[0]
                    vals.append(this_node.val)
                    if i < len(current) - 1:
                        this_node.next = current[i+1]
                    if this_node.left != None:
                        current.append(this_node.left)
                    if this_node.right != None:
                        current.append(this_node.right)
                    current.pop(0)
                result.append(vals)
        return result