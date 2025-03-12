import heapq
import sys
from typing import List


def main():
    # 读取第一行数据，分别是两个整数 n 和 m
    n, m = list(map(int, sys.stdin.readline().strip().split()))

    # 读取接下来的 m 行数据，每行包含三个整数
    # edges = []
    graph = [[] for _ in range(n)]
    while m > 0:
        m -= 1
        line = sys.stdin.readline().strip()
        data = list(map(int, line.split()))
        u = int(data[0])
        v = int(data[1])
        w = int(data[2])
        # edges.append((u, v, w))
        graph[u - 1].append((v - 1, w))

    # 调用解决方案函数，并将结果打印出来
    result = solve(graph)
    print(" ".join(str(x) for x in result))


def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    h = [(0, start)]
    while h:
        d, u = heapq.heappop(h)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(h, (dist[v], v))
    return dist


def solve(graph) -> List[int]:
    n = len(graph)
    dist1 = dijkstra(graph, 0)
    ans = [-1] * (n - 1)
    for i in range(1, n):
        dist2 = dijkstra(graph, i)
        res = min(dist1[j] + dist2[j] for j in range(n))
        if res < float('inf'):
            ans[i - 1] = res
    return ans


if __name__ == "__main__":
    main()
