# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        averages = []
        roots = [root]
      
        def get_next_roots(roots):
            next_roots = []
            for root in roots:
                if root.left is not None:
                    next_roots.append(root.left)
                if root.right is not None:
                    next_roots.append(root.right)
            return next_roots
    
        def traverse(_map, root_nodes):
            #evaluate each level and store all nodes in each level
            nodes = []
            for node in root_nodes:
                nodes.append(node.val)
            _map.append(sum(nodes)/float(len(nodes)))
            root_nodes = get_next_roots(root_nodes)
            if not root_nodes:
                return _map
            return traverse(_map, root_nodes)
            
        return traverse(averages, roots)
              