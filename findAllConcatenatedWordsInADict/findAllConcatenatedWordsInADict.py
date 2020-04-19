# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def canBreak(w, wdict):
            if w == '':  flag[0] = True
            for i in range( len(w)):
                if w[:i + 1] in wdict and wdict[w[:i + 1]]:
                    canBreak(w[i + 1:], wdict)
                    if flag[0]: return True

        res = []
        wdict = {}
        for w in words:
            wdict[w] = True
        for w in words:
            wdict[w] = False
            flag = [False]
            if canBreak(w, wdict):
                res.append(w)
            wdict[w] = True
        return res


def main():
    string = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    solution = Solution()
    sol = solution.findAllConcatenatedWordsInADict(string)
    print(sol)


if __name__ == '__main__':
    main()

