# https://codeforces.com/problemset/problem/327/A

import sys
from typing import List


def main():
    n = list(map(int, sys.stdin.readline().strip()))[0]
    nums = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(nums))


def solve(nums: List[int]) -> int:
    pre = [1 if x == 1 else -1 for x in nums]
    n = len(nums)
    for i in range(1, n):
        pre[i] = min(pre[i - 1], 0) + pre[i]
    return sum(nums) - min(pre)


main()
