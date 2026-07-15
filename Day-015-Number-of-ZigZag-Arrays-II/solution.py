class Solution:
    MOD = 10**9 + 7

    def multiply(self, A, B, size):
        C = [[0] * size for _ in range(size)]

        for i in range(size):
            for k in range(size):
                if A[i][k] == 0:
                    continue
                for j in range(size):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % self.MOD

        return C

    def power(self, A, p, size):
        res = [[0] * size for _ in range(size)]

        for i in range(size):
            res[i][i] = 1

        while p > 0:
            if p & 1:
                res = self.multiply(res, A, size)
            A = self.multiply(A, A, size)
            p >>= 1

        return res

    def zigZagArrays(self, n, l, r):
        m = r - l + 1
        num_states = 2 * m

        if n == 1:
            return m

        T = [[0] * num_states for _ in range(num_states)]

        for i in range(m):
            for j in range(i + 1, m):
                T[i][j + m] = 1
            for j in range(i):
                T[i + m][j] = 1

        Tn = self.power(T, n - 1, num_states)

        total = 0
        for i in range(num_states):
            for j in range(num_states):
                total = (total + Tn[i][j]) % self.MOD

        return total