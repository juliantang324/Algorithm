# https://codeforces.com/problemset/problem/1800/D

import sys


def main():
    n = int(sys.stdin.readline())
    arr = str(sys.stdin.readline().strip())
    print(solve(arr))


def solve(arr: str) -> int:
    ans = left = 0
    for right, x in enumerate(arr):
        if right - left + 1 > 2:
            if x != arr[left]:
                ans += 1
            left += 1
    return ans + 1


TC = int(sys.stdin.readline())

for _ in range(TC):
    main()
