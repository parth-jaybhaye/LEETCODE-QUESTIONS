class Solution(object):
    def processStr(self, s):
        result = []

        for ch in s:
            if 'a' <= ch <= 'z':
                result.append(ch)
            elif ch == '*':
                if result:
                    result.pop()
            elif ch == '#':
                result.extend(result)
            else:
                result.reverse()

        return "".join(result)