import heapq
import sys
from math import inf
from typing import List

"""
分层图最短路。

建图：把每条有向边及其反向边加到图中，用一个额外变量 inv 表示这条边是否为反向边。

从 1 到 i 的路径分成两段：
从 1 到 x，走原图上的边。（记作状态 0）
从 x 到 i，走反向边。（记作状态 1）

由于到达每个节点时，都有两个状态，所以相当于在有 2n 个节点的图上跑 Dijkstra 算法。Dijkstra 算法介绍

类似状态机 DP，在 Dijkstra 的优先队列中，额外记录一个状态 inv，如果 inv=0 表示当前在走原图上的边，如果 inv=1 表示当前在走反向边。

如果当前状态是 0，那么可以转移到 0 或者 1。
如果当前状态是 1，那么只能转移到 1。
"""


def main():
    # 读取第一行数据，分别是两个整数 n 和 m
    n, m = list(map(int, sys.stdin.readline().strip().split()))

    # 读取接下来的 m 行数据，每行包含三个整数
    graph = [[] for _ in range(n)]
    while m > 0:
        m -= 1
        line = sys.stdin.readline().strip()
        data = list(map(int, line.split()))
        u = int(data[0])
        v = int(data[1])
        w = int(data[2])
        graph[u - 1].append((v - 1, w, 0))
        graph[v - 1].append((u - 1, w, 1))

    # 调用解决方案函数，并将结果打印出来
    dist = [[inf, inf] for _ in range(n)]
    dist[0][0] = 0
    dist[0][1] = 0
    h = [(0, 0, 0), (0, 0, 1)]
    heapq.heapify(h)
    while h:
        d, u, state = heapq.heappop(h)
        if d > dist[u][state]:
            continue
        for v, w, inv in graph[u]:
            if state == 1 and inv == 0:
                continue
            if d + w < dist[v][inv]:
                dist[v][inv] = d + w
                heapq.heappush(h, (dist[v][inv], v, inv))
    ans = []
    for x, y in dist[1:]:
        res = min(x, y)
        ans.append(int(res) if res < inf else -1)
    print(" ".join(str(x) for x in ans))


# def dijkstra(graph, start):
#     n = len(graph)
#     dist = [[inf, inf] for _ in range(n)]
#     dist[start][0] = 0
#     dist[start][1] = 0
#     h = [(0, start, 0), (0, start, 1)]
#     heapq.heapify(h)
#     while h:
#         d, u, state = heapq.heappop(h)
#         if d > dist[u][state]:
#             continue
#         for v, w, inv in graph[u]:
#             if state == 1 and inv == 0:
#                 continue
#             if d + w < dist[v][inv]:
#                 dist[v][inv] = d + w
#                 heapq.heappush(h, (dist[v][inv], v, inv))
#     return dist
#
#
# def solve(graph) -> List[int]:
#     dist = dijkstra(graph, 0)
#     ans = []
#     for x, y in dist[1:]:
#         res = min(x, y)
#         ans.append(int(res) if res < inf else -1)
#     return ans


if __name__ == "__main__":
    main()
