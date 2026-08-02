class UnionFind:
    def __init__(self):
        self.p = {}

    def make_set(self, v):
        if v in self.p:
            return
        
        self.p[v] = v
    
    def find_parent(self, v):
        # stop when we reach the root
        if v == self.p[v]:
            return v
        
        # use path compression
        # set the parent of us as the parent of our parent
        # trying to compress the downwards parent-child chains
        self.p[v] = self.find_parent(
            self.p[v]
        )
        return self.p[v]

    def union(self, v, u):
        first = self.find_parent(v)
        second = self.find_parent(u)

        if first != second:
            # arbitrarily set the parent of the first node to the second node
            self.p[first] = second
            return True
        
        # if they have the same parent, then they must be in the same
        # set (same ancestor)
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = UnionFind()

        for src, dest in edges:
            union.make_set(src)
            union.make_set(dest)

            if not union.union(src, dest):
                return [src, dest]

        raise Exception
