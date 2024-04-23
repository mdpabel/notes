---
title: Algorithms
description: Implementations of algorithms
date: 03-24-2024
status: draft
priority: 1
---

## Minimum Spanning Tree

1. https://leetcode.com/problems/min-cost-to-connect-all-points/

```py
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = [[] for _ in range(n)]

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edges[i].append([cost, j])
                edges[j].append([cost, i])

        # prim's
        visited = set()
        heap = [[0, 0]] #[cost, point]
        costs = 0

        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            costs += cost
            visited.add(i)

            for neiCost, nei in edges[i]:
                if nei not in visited:
                    heapq.heappush(heap, [neiCost, nei])

        return costs
```
