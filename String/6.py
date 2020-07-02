class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        rows = [[] for _ in range(numRows)]
        cur = 0
        rev = False
        for i in range(len(s)):
            rows[cur].append(s[i])
            if rev:
                if cur == 0:
                    rev = False
                    cur += 1
                else:
                    cur -= 1
            else:
                if cur == numRows - 1:
                    rev = True
                    cur -= 1
                else:
                    cur += 1
        convertion = ''
        for i in range(numRows):
            for ch in rows[i]:
                convertion += ch
        return convertion