class Solution:
    def myAtoi(self, str: str) -> int:
        start = -1
        for i in range(len(str)):
            if str[i] != ' ':
                start = i
                break
        if start == -1:
            return 0
        negative = False
        if str[start] == '+' or str[start] == '-':
            negative = str[start] == '-'
            start += 1
        end = start
        while end < len(str):
            if not str[end].isnumeric():
                break
            end += 1
        if end == start:
            return 0
        num = int(str[start:end])
        if negative and num > 2**31:
            return - 2**31
        elif negative:
            return - num
        elif num > 2**31-1:
            return 2**31-1
        else:
            return num    