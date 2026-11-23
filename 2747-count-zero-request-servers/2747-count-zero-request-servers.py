class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda a: a[1])
        q = sorted((v, i) for i, v in enumerate(queries))

        count = [0] * (n + 1)
        ans = [0] * len(queries)
        left = right = active = 0

        for time, idx in q:
            while right < len(logs) and logs[right][1] <= time:
                s = logs[right][0]
                if count[s] == 0:
                    active += 1
                count[s] += 1
                right += 1

            while left < right and logs[left][1] < time - x:
                s = logs[left][0]
                count[s] -= 1
                if count[s] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans