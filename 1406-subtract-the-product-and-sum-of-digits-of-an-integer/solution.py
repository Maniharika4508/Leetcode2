class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        sum=0
        while(n>0):
            d=n%10
            sum=sum+d
            prod=prod*d
            n=n//10
        return prod-sum
