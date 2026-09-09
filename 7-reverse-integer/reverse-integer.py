class Solution(object):
    def reverse(self, x):
        r=int(str(abs(x))[::-1])
        if r>2**31-1:
            return 0
        return -r if x<0 else r
        