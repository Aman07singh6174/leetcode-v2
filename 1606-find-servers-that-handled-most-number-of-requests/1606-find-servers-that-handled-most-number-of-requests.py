import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                _, server = heapq.heappop(busy)
                available.append(server)

            available.sort()

            if not available:
                continue

            start = i % k
            server = -1

            for s in available:
                if s >= start:
                    server = s
                    break

            if server == -1:
                server = available[0]

            available.remove(server)
            count[server] += 1

            heapq.heappush(busy, (arrival[i] + load[i], server))

        maximum = max(count)
        return [i for i in range(k) if count[i] == maximum]