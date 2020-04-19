# -*- coding: utf-8 -*-


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        a = {'D':'R','R':'D'}
        while 'R' in senate and 'D' in senate:
            i = senate.index(a[senate[0]])
            senate = senate[1:i] + senate[i+1:] + senate[0]
        return 'Dire' if 'R' not in senate else 'Radiant'


def main():
    string = 'DRRDRDRDRDDRDRDR'
    solution = Solution()
    sol = solution.predictPartyVictory(string)
    print(sol)


if __name__ == '__main__':
    main()

