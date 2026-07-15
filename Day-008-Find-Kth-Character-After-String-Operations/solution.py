class Solution(object):
    def processStr(self, s, k):
        n = len(s)
        length = [0] * n
        current_len = 0

        for i, ch in enumerate(s):
            if 'a' <= ch <= 'z':
                current_len += 1
            elif ch == '*':
                if current_len > 0:
                    current_len -= 1
            elif ch == '#':
                current_len *= 2
            elif ch == '%':
                pass
            length[i] = current_len

        if k >= current_len or k < 0:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_len = length[i - 1] if i > 0 else 0

            if 'a' <= ch <= 'z':
                if k == prev_len:
                    return ch
            elif ch == '#':
                if k >= prev_len:
                    k -= prev_len
            elif ch == '%':
                k = current_len - 1 - k

            current_len = prev_len

        return '.'