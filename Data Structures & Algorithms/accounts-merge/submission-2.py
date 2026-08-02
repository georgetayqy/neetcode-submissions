from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parents = {}
        self.rank = {}

    def make_set(self, v):
        if v in self.parents:
            return

        self.parents[v] = v
        self.rank[v] = 1
    
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
            if self.rank[a] < self.rank[b]:
                a, b = b, a
            
            self.rank[a] += self.rank[b]
            self.parents[b] = a
            return True
        
        return False

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = UnionFind()
        emailToId = {}

        for idx, accountDetails in enumerate(accounts):
            union.make_set(idx)
            
            for i in range(1, len(accountDetails)):
                current_email = accountDetails[i]
                if current_email in emailToId:
                    union.union(idx, emailToId[current_email])
                else:
                    emailToId[current_email] = idx
        
        # append the emails to the parent
        emailGroups = defaultdict(list)
        for email, id in emailToId.items():
            parent = union.find_parent(id)
            emailGroups[parent].append(email)

        returns = []
        for id, emails in emailGroups.items():
            returns.append(
                [accounts[id][0]] + sorted(emails)
            )
        
        return returns

            
