import heapq

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        # Initialize a list to store the maximum probability to reach each node
        max_prob = [0.0] * n
        max_prob[start] = 1.0  # Start node has a probability of 1 to reach itself

        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        # Priority queue to perform Dijkstra-like traversal
        # We use negative probabilities to simulate a max-heap using Python's min-heap
        pq = [(-1.0, start)]

        while pq:
            # Extract the node with the highest probability
            current_prob, node = heapq.heappop(pq)
            current_prob = -current_prob

            # If we've reached the end node, return the probability
            if node == end:
                return current_prob

            # Traverse neighboring nodes
            for neighbor, edge_prob in graph[node]:
                # Calculate new probability through this path
                new_prob = current_prob * edge_prob
                # If the new probability is higher, update and push to the queue
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        # If no path found to the end node, return 0
        return 0.0
