class Answer:
    def __init__(self):
        self.ans = [0, 0, 0]

    def put(self, x: int):
        _ans = self.ans
        if x > _ans[0]:
            _ans[0], _ans[1], _ans[2] = x, _ans[0], _ans[1]
        elif x != _ans[0] and x > _ans[1]:
            _ans[1], _ans[2] = x, _ans[1]
        elif x != _ans[0] and x != _ans[1] and x > _ans[2]:
            _ans[2] = x

    def get(self) -> List[int]:
        return [num for num in self.ans if num != 0]

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        sum1 = [[0] * (n + 2) for _ in range(m + 2)]
        sum2 = [[0] * (n + 2) for _ in range(m + 2)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum1[i][j] = sum1[i - 1][j - 1] + grid[i - 1][j - 1]
                sum2[i][j] = sum2[i - 1][j + 1] + grid[i - 1][j - 1]

        ans = Answer()

        for r in range(m):
            for c in range(n):
                ans.put(grid[r][c])

                for L in range(1, min(m, n)):
                    if r + 2 * L >= m or c - L < 0 or c + L >= n:
                        break

                    edge1 = sum2[r + L + 1][c - L + 1] - sum2[r + 1][c+ 1]
                    edge2  = sum1[r + 2 * L + 1][c + 1] - sum1[r + L + 1][c - L + 1]
                    edge3 = sum1[r + L + 1][c + L + 1] - sum1[r + 1][c + 1]
                    edge4 = sum2[ r + 2 * L + 1][c + 1] - sum2[r + L + 1][c + L + 1]

                    total = edge1 + edge2 + edge3 + edge4 + grid[r][c] - grid[r + 2 * L][c]
                    ans.put(total)

        return ans.get()

        