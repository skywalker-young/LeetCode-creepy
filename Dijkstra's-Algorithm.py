    def networkDelayTime(self, times, N, K):
        from collections import defaultdict
        nodes = defaultdict(dict)
        Q = set(range(N))
        for u, v, w in times:
            nodes[u - 1][v - 1] = w
        dist = [float('inf')] * N
        dist[K - 1] = 0
        while len(Q):
            u = None
            for node in Q:
                if u == None or dist[node] < dist[u]:
                    u = node
            Q.remove(u)
            for v in nodes[u]:
                alt = dist[u] + nodes[u][v]
                if alt < dist[v]:
                    dist[v] = alt
        d = max(dist)
        return -1 if d == float('inf') else d
