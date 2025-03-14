# https://codeforces.com/problemset/problem/2041/E

import sys


def main():
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    ans = [b]
    if a != b:
        s = a * 3 - b
        c = min(b, s - b) - 1
        d = s - c
        ans = [c, b, d]
    print(len(ans))
    print(" ".join(str(x) for x in ans))


main()
