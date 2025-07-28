class Solution:
    def averageValue(self, nums: List[int]) -> int:
      sum1=0
      count=0
      for num in nums:
        if num%2==0 and num%3==0 :
          sum1+=num
          count+=1
      if sum1==0:
          return 0
      else:
          return sum1//count

