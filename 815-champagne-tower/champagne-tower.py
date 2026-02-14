class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        levels = [[0] * (i+1) for i in range(query_row + 1)]
        levels[0][0] = poured

        for r in range(query_row):
            for c in range(r + 1):
                next = (levels[r][c] - 1) / 2
                if next > 0:
                    levels[r + 1][c] += next
                    levels[r + 1][c + 1] += next

        return min(1, levels[query_row][query_glass])