class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        last = {}
        new_parent = parent[:]

        def dfs(node):
            char = s[node]
            old = last.get(char, -1)

            if old != -1:
                new_parent[node] = old

            last[char] = node

            for child in children[node]:
                dfs(child)

            if old == -1:
                last.pop(char, None)
            else:
                last[char] = old

        dfs(0)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[new_parent[i]].append(i)

        ans = [1] * n

        def calculate(node):
            for child in children[node]:
                ans[node] += calculate(child)
            return ans[node]

        calculate(0)
        return ans