from collections import defaultdict, deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS
        seen = set()
        seen.add(source)

        q = deque()
        q.append(source)

        while q:
            node = q.popleft()

            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)

        return False
