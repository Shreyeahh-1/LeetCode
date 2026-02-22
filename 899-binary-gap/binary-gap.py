class Solution:
    def binaryGap(self, n: int) -> int:
        A = []
        for i in range(32):
            if (n >> i) & 1:
                A.append(i)

        ans = 0
        for i in range(len(A) - 1):
            ans = max(ans, A[i+1] - A[i])

        return ans

        