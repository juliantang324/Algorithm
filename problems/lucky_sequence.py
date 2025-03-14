# https://codeforces.com/problemset/problem/145/C

import sys
from types import GeneratorType
from typing import List


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


mod = 10 ** 9 + 7


def main():
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(a, k))


def lucky(x: int) -> bool:
    while x > 0:
        if x % 10 != 4 and x % 10 != 7:
            return False
        x //= 10
    return True


def solve(arr: List[int], k: int):
    luck = []

    @iterative_decorator
    def dfs(i, h):
        if h == 0:
            yield 1
        if i < 0:
            yield 0
        res = yield dfs(i - 1, h)
        if not lucky(arr[i]):
            res += yield dfs(i - 1, h - 1)
        elif arr[i] not in luck:
            luck.append(arr[i])
            res += yield dfs(i - 1, h - 1)
            luck.pop()
        yield res

    return dfs(len(arr) - 1, k) % mod


main()
