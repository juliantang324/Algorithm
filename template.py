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


def solve():
    pass


TC = 0


def main():
    for _ in range(TC):
        solve()


main()
