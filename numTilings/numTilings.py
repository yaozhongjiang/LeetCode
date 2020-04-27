# -*- coding: utf-8 -*-

class Solution:
    def numTilings(self, N: int) -> int:
        a = [ 0 for i in range(0, N + 2)]
        b = [ 0 for i in range(0, N + 2)]
        c = 1e9 + 7
        a[1] = 1
        a[2] = 2
        b[2] = 1
        if N >= 3:
            for i in range(3, N+1):
                a[i]=(a[i-1]+a[i-2]+2 * b[i-1]) % c
                b[i]=(b[i-1]+a[i-2]) % c
                i += 1
        return int(a[N])


def main():
    num = 3
    solution = Solution()
    sol = solution.numTilings(num)
    print(sol)


if __name__ == '__main__':
    main()

