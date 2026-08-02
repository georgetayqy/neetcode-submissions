class UnionFind:
    def __init__(self):
        self.parents = {}
    
    def is_a_parent(self, v):
        return v in self.parents
    
    def make_set(self, v):
        self.parents[v] = v
    
    def find_parent(self, v):
        if v == self.parents[v]:
            return v

        self.parents[v] = self.find_parent(
            self.parents[v]
        )
        return self.parents[v]
    
    def union(self, v, u):
        a = self.find_parent(v)
        b = self.find_parent(u)

        if a != b:
            # not of the same set
            self.parents[b] = a
            return True
        
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionfind = UnionFind()

        for src, dest in edges:
            unionfind.make_set(src)
            unionfind.make_set(dest)
        
        for src, dest in edges:
            if not unionfind.union(src, dest):
                return [src, dest]

        return []