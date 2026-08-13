import collections


class SegmentTreeNode:
    def __init__(
        self,
        lo,
        hi,
        maxLetter,
        prefixLetter,
        suffixLetter,
        maxLength,
        prefixLength,
        suffixLength,
        left=None,
        right=None,
    ):
        self.lo = lo
        self.hi = hi
        self.maxLetter = maxLetter
        self.prefixLetter = prefixLetter
        self.suffixLetter = suffixLetter
        self.maxLength = maxLength
        self.prefixLength = prefixLength
        self.suffixLength = suffixLength
        self.left = left
        self.right = right


class SegmentTree:
    def __init__(self, s: str):
        self.root = self._build(s, 0, len(s) - 1)

    def update(self, i: int, val: str):
        self.root = self._update(self.root, i, val)

    def getMaxLength(self) -> int:
        return self.root.maxLength

    def _build(self, s: str, lo: int, hi: int):
        if lo == hi:
            return SegmentTreeNode(lo, hi, s[lo], s[lo], s[lo], 1, 1, 1)

        mid = (lo + hi) // 2
        left = self._build(s, lo, mid)
        right = self._build(s, mid + 1, hi)
        return self._merge(left, right)

    def _update(self, root, i, c):
        if root.lo == i and root.hi == i:
            root.maxLetter = c
            root.prefixLetter = c
            root.suffixLetter = c
            return root

        mid = (root.lo + root.hi) // 2

        if i <= mid:
            root.left = self._update(root.left, i, c)
        else:
            root.right = self._update(root.right, i, c)

        return self._merge(root.left, root.right)

    def _merge(self, left, right):
        maxLetter = left.maxLetter
        maxLength = left.maxLength

        if right.maxLength > maxLength:
            maxLetter = right.maxLetter
            maxLength = right.maxLength

        if (
            left.suffixLetter == right.prefixLetter
            and left.suffixLength + right.prefixLength > maxLength
        ):
            maxLetter = left.suffixLetter
            maxLength = left.suffixLength + right.prefixLength

        prefixLetter = left.prefixLetter
        prefixLength = left.prefixLength
        if (
            left.lo + prefixLength == right.lo
            and left.prefixLetter == right.prefixLetter
        ):
            prefixLength += right.prefixLength

        suffixLetter = right.suffixLetter
        suffixLength = right.suffixLength
        if (
            right.hi - suffixLength == left.hi
            and right.suffixLetter == left.suffixLetter
        ):
            suffixLength += left.suffixLength

        return SegmentTreeNode(
            left.lo,
            right.hi,
            maxLetter,
            prefixLetter,
            suffixLetter,
            maxLength,
            prefixLength,
            suffixLength,
            left,
            right,
        )


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: list[int],
    ) -> list[int]:
        ans = []
        tree = SegmentTree(s)

        for i in range(len(queryIndices)):
            tree.update(queryIndices[i], queryCharacters[i])
            ans.append(tree.getMaxLength())

        return ans