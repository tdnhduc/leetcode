#!/usr/bin/env python3.8

class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        convert = []
        for i in s:
            convert.append(SYMBOL[i])
        result = 0
        if len(convert) == 1:
            return convert[0]
        for i in range(len(s) - 1):
            if convert[i] >= convert[i + 1]:
                result += convert[i]
            else:   
                result -= convert[i]
        result += convert[len(convert) - 1]
        return result
