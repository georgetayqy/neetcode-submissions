from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True

        adjList = defaultdict(set)
        
        for src, dest in edges:
            adjList[src].add(dest)
            adjList[dest].add(src)
        
        stack = []
        stack.append((0, -1))
        seen = set()

        while stack:
            current_node, parent = stack.pop()

            if current_node in seen:
                # cycle detected
                return False
            
            seen.add(current_node)

            for neighbours in adjList[current_node]:  
                if neighbours == parent:
                    continue

                stack.append((neighbours, current_node))

        return len(seen) == n
            