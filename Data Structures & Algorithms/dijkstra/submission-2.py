class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        distances = {src:0}
        heap = [(0, src)]
        
        graph = {node:[] for node in range(n)}
        

        for u, v , weight in edges:
            graph[u].append((v,weight))

        while heap:
            cost, current = heapq.heappop(heap)
            if cost > distances[current]:
                continue
            
            for neighbor, weight in graph[current]:
                new_cost = cost + weight

                if new_cost < distances.get(neighbor, float('inf')):
                    distances[neighbor]=new_cost
                    heapq.heappush(heap,(new_cost, neighbor))

        for vertex in range(n):
            if vertex not in distances:
                distances[vertex] = -1
        
        return distances


            
