class Solution():
    def isValid(self, s):
        # Until the while condition is true.
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()','').replace('{}','').replace('[]','')
        return s == ''

a = Solution()

print(a.isValid('{[]'))
