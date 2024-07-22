import heapq

class Solution:
    def countPaths(self, n, roads):
        MOD = 10**9 + 7
        
        # Create the graph
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Dijkstra's algorithm to find shortest paths and count ways
        def dijkstra():
            dist = [float('inf')] * n
            ways = [0] * n
            min_heap = [(0, 0)]  # (distance, node)
            dist[0] = 0
            ways[0] = 1
            
            while min_heap:
                current_dist, u = heapq.heappop(min_heap)
                
                if current_dist > dist[u]:
                    continue
                
                for v, time in graph[u]:
                    new_dist = current_dist + time
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        ways[v] = ways[u]
                        heapq.heappush(min_heap, (new_dist, v))
                    elif new_dist == dist[v]:
                        ways[v] = (ways[v] + ways[u]) % MOD
            
            return ways[n - 1]
        
        return dijkstra()