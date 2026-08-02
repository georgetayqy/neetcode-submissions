class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = {i: set() for i in range(n)}

        for src, dest in edges:
            parents[src].add(dest)
            parents[dest].add(src)

        num_components = 0
        seen = set()

        for i in range(n):
            if i in seen:
                continue

            num_components += 1

            stack = [(i, -1)]
            while stack:
                curr, parent = stack.pop()

                if curr in seen:
                    continue
                
                seen.add(curr)

                for neighbour in parents[curr]:
                    if neighbour == parent:
                        continue
                    
                    stack.append((neighbour, curr))
            
        return num_components
