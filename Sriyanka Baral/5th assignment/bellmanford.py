class Solution:
    def networkDelayTime(self, times, N, K):
        # Create an adjacency list
        graph = [[] for _ in range(N)]
        for u, v, w in times:
            graph[u-1].append((v-1, w))
        
        # Priority queue to store (time, node)
        pq = [(0, K-1)]
        # Dictionary to store the shortest time to each node
        shortest_time = [float('inf')] * N
        shortest_time[K-1] = 0
        
        while pq:
            # Extract the node with the smallest time
            pq.sort()
            current_time, node = pq.pop(0)
            
            # If the current time is greater than the recorded shortest time, skip
            if current_time > shortest_time[node]:
                continue
            
            for neighbor, weight in graph[node]:
                time = current_time + weight
                
                # Only consider this new path if it's better
                if time < shortest_time[neighbor]:
                    shortest_time[neighbor] = time
                    pq.append((time, neighbor))
        
        # Get the maximum time from the shortest times recorded
        max_time = max(shortest_time)
        return max_time if max_time < float('inf') else -1