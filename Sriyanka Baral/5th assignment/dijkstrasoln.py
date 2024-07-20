import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Step 1: Initialize the maximum probability list
        max_prob = [0.0] * n
        max_prob[start] = 1.0  # Start node has a probability of 1 to reach itself

        # Step 2: Build the graph using adjacency list
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        # Step 3: Set up a priority queue for Dijkstra's algorithm
        pq = [(-1.0, start)]  # Using negative probabilities to simulate a max-heap

        while pq:
            # Step 4: Extract the node with the highest probability
            current_prob, node = heapq.heappop(pq)
            current_prob = -current_prob  # Convert back to positive

            # If we've reached the end node, return the probability
            if node == end:
                return current_prob

            # Step 5: Traverse the neighbors of the current node
            for neighbor, edge_prob in graph[node]:
                # Calculate new probability through this edge
                new_prob = current_prob * edge_prob
                # If this new path offers a higher probability, update and push to the queue
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        # Step 6: If no path found to the end node, return 0
        return 0.0

# Example usage
sol = Solution()
n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2
print(sol.maxProbability(n, edges, succProb, start, end))  # Output: 0.25

        