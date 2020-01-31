class Solution():
    def isHappy(self, n):

        if n < 1: return False
        elif n == 1: return True

        while n != 1 and n > 1:
              num = list(map(int,str(n)))

              sum = 0

              for i in range(len(num)):
                  sum = sum + (num[i]**2)

              if sum == 1:
                  return True
              else:
                  n = sum

a = Solution()

print(a.isHappy(19))



