class Solution(object):
    def sumAndMultiply(self, n):
        digits = []
        total = 0

        for ch in str(n):
            if ch != '0':
                digit = int(ch)
                digits.append(ch)
                total += digit

        if not digits:
            return 0

        x = int("".join(digits))

        return x * total