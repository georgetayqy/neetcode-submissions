class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def make_set(self, v):
        self.parent[v] = v
    
    def find_set(self, v):
        # if they have the same super-ancestor, set
        # all of their parents to the same super-ancestor to compress the paths
        if v == self.parent[v]:
            return v
        
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]
    
    def union_set(self, v, w):
        v_parent = self.find_set(v)
        w_parent = self.find_set(w)

        if v_parent == w_parent:
            return False
        
        self.parent[w_parent] = v_parent
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()

        for i in range(n):
            uf.make_set(i)
        
        num_components = n
        for src, dest in edges:
            if uf.union_set(src, dest):
                num_components -= 1
        
        return num_components
