import os
import random
import sys
from typing import *
from collections import defaultdict, Counter, deque
from functools import cache, reduce
from itertools import pairwise, combinations, permutations, groupby, accumulate
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import *
from math import gcd, lcm, isqrt
from operator import add, sub, mul, floordiv, truediv, and_, or_, xor

from types import GeneratorType


# Decorator to convert recursive functions to iterative using a stack
def iterative_decorator(func, call_stack=[]):
    def wrapped_function(*args, **kwargs):
        if call_stack:
            return func(*args, **kwargs)
        else:
            result = func(*args, **kwargs)
            while True:
                if isinstance(result, GeneratorType):
                    call_stack.append(result)
                    result = next(result)
                else:
                    call_stack.pop()
                    if not call_stack:
                        break
                    result = call_stack[-1].send(result)
            return result

    return wrapped_function


# Input and output shortcuts
read_input = sys.stdin.readline
write_output = lambda x: sys.stdout.write(str(x) + "\n")
write_output_list = lambda x: sys.stdout.write(" ".join(map(str, x)) + "\n")

# Input parsing shortcuts
read_line = lambda: read_input().rstrip("\n")
read_int = lambda: int(read_input())
map_int_input = lambda: map(int, read_input().split())
list_map_int_input = lambda: list(map_int_input())
tuple_map_int_input = lambda: tuple(map_int_input())
list_chars_input = lambda: list(read_line())


def solve(a: List[int], b: List[int], queries: List[Tuple[int, ...]]) -> List[int]:
    mod = 998244353
    n = len(a)
    ta = [0] * (4 * n)
    tb = [0] * (4 * n)
    t = [0] * (4 * n)
    todo_a = [0] * (4 * n)
    todo_b = [0] * (4 * n)

    def maintain(node: int) -> None:
        ta[node] = (ta[node * 2 + 1] + ta[node * 2 + 2]) % mod
        tb[node] = (tb[node * 2 + 1] + tb[node * 2 + 2]) % mod
        t[node] = (t[node * 2 + 1] + t[node * 2 + 2]) % mod

    def do(node: int, left: int, right: int, val: Tuple[int, int]) -> None:
        size = right - left + 1
        ta[node]  = (ta[node] + val[0] * size) % mod
        t[node] = (t[node] + val[0] * tb[node]) % mod
        tb[node] = (tb[node] + val[1] * size) % mod
        t[node] = (t[node] + val[1] * ta[node]) % mod
        todo_a[node] = (todo_a[node] + val[0]) % mod
        todo_b[node] = (todo_b[node] + val[1]) % mod

    def spread(node: int, left: int, right: int) -> None:
        if todo_a[node] or todo_b[node]:
            mid = (left + right) // 2
            do(node * 2 + 1, left, mid, (todo_a[node], todo_b[node]))
            do(node * 2 + 2, mid + 1, right, (todo_a[node], todo_b[node]))
            todo_a[node] = todo_b[node] = 0

    def build(node: int, left: int, right: int) -> None:
        if left == right:
            ta[node] = a[left]
            tb[node] = b[left]
            t[node] = a[left] * b[left] % mod
            return
        mid = (left + right) // 2
        build(node * 2 + 1, left, mid)
        build(node * 2 + 2, mid + 1, right)
        maintain(node)

    def update(node: int, left: int, right: int, L: int, R: int, val: Tuple[int, int]) -> None:
        if L <= left and right <= R:
            do(node, left, right, val)
            return
        spread(node, left, right)
        mid = (left + right) // 2
        if L <= mid:
            update(node * 2 + 1, left, mid, L, R, val)
        if R > mid:
            update(node * 2 + 2, mid + 1, right, L, R, val)
        maintain(node)

    def query(node: int, left: int, right, L: int, R: int) -> int:
        if L <= left and right <= R:
            return t[node]
        spread(node, left, right)
        mid = (left + right) // 2
        res = 0
        if L <= mid:
            res = query(node * 2 + 1, left, mid, L, R)
        if R > mid:
            res += query(node * 2 + 2, mid + 1, right, L, R)
        return res % mod

    build(0, 0, n - 1)
    ans = []
    for q in queries:
        if q[0] == 1:
            l, r, x = q[1:]
            update(0, 0, n - 1, l - 1, r - 1, (x, 0))
        elif q[0] == 2:
            l, r, x = q[1:]
            update(0, 0, n - 1, l - 1, r - 1, (0, x))
        else:
            l, r = q[1:]
            ans.append(query(0, 0, n - 1, l - 1, r - 1))
    return ans


TC = 0


def main():
    n, q = list_map_int_input()
    a = list_map_int_input()
    b = list_map_int_input()
    queries = [tuple_map_int_input() for _ in range(q)]
    result = solve(a, b, queries)
    for res in result:
        write_output(res)


main()
