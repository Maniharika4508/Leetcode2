class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
            s = 0
            temp = x
            while x> 0:
                d = x % 10
                s += d
                x//= 10
            if temp % s == 0:
               return s
            else:
                return -1

