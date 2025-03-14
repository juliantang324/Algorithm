# https://codeforces.com/problemset/problem/1832/C

import sys
from typing import List


def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(nums))


def solve(nums: List[int]) -> int:
    n = len(nums)
    cnt = left = 0
    for i in range(1, n - 1):
        if (nums[i + 1] - nums[i]) * (nums[i] - nums[left]) >= 0:
            cnt += 1
        else:
            left = i
    if n > 1 and nums[-1] == nums[left]:
        cnt += 1
    return n - cnt


TC = int(sys.stdin.readline())

for _ in range(TC):
    main()
