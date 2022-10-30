class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqr = int(sqrt(c))
        arr = set([i*i for i in range(sqr + 1)])

        for num in arr:
            b = c - num
            if b in arr:
                return True
        return False