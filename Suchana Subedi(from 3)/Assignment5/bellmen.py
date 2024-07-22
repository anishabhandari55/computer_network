import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # Create the graph as an adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Dijkstra's algorithm
        min_heap = [(0, k)]  # (time, node)
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            if time > dist[node]:
                continue
            
            for neighbor, t in graph[node]:
                new_time = time + t
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))
        
        # Find the maximum time to reach any node
        max_time = max(dist[1:])
        
        return max_time if max_time < float('inf') else -1