class Solution(object):
    def reverse(self, x):
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)
        rem = x % 10
        div = int(x / 10)
        rev = rem
        while div != 0:
            rem = div % 10
            div = int(div / 10)
            rev = rev * 10 + rem
        if rev > 2147483647 or rev < -2147483648:
            return 0
        if is_negative:
            return -rev
        return rev


a = Solution()
print(a.reverse(321))
print(a.reverse(-123))
print(a.reverse(120))
print(a.reverse(0))
print(a.reverse(2))
print(a.reverse(1534236469))
