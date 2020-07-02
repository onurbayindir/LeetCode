class Solution:
    def reverse(self, x: int) -> int:
        # Python solution is pretty straightforward
        # since there is no possibility for integer overflow
        num = str(x)
        if num[0] == '-':
            num = int('-' + num[1:][::-1])
        else:
            num = int(num[::-1])
        if -2**31 <= num < 2**31-1:
            return num
        return 0