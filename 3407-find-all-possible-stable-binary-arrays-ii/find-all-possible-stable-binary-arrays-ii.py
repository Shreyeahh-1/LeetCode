class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        dp = [[[0,0] for _ in range(one + 1)] for _ in range(zero +1)]
        for i in range(zero + 1):
            for j in range(one + 1):
                for lastBit in range(2):
                    if i == 0:
                        if lastBit == 0 or j > limit: dp[i][j][lastBit] = 0
                        else: dp[i][j][lastBit] = 1
                    elif j == 0:
                        if lastBit == 1 or i > limit: dp[i][j][lastBit] = 0
                        else: dp[i][j][lastBit] = 1
                    elif lastBit == 0:
                        dp[i][j][lastBit] = (dp[i - 1][j][0] + dp[i-1][j][1]) % mod
                        if i > limit:
                            dp[i][j][lastBit] = (dp[i][j][lastBit] - dp[i- 1- limit][j][1] + mod) % mod
                    else:
                        dp[i][j][lastBit] = ( dp[i][j-1][0] + dp[i][j-1][1]) % mod
                        if j>limit:
                            dp[i][j][lastBit] = (dp[i][j][lastBit] - dp[i][j - 1 - limit][0] + mod) % mod
        return (dp[zero][one][0] + dp[zero][one][1]) % mod




        # mod = 10**9 + 7

        # from functools import cache
        # @cache
        # def dp(zero, one, lastBit):
        #     if zero == 0:
        #         if lastbit == 0 or one > limit:
        #             return 0
        #         else:
        #             return 1
        #     elif one == 0:
        #         if lastbit == 1 or zero >limit:
        #             return 0
        #         else:
        #             return 1
            
        #     if lastBit == 0:
        #         res = dp(zero -1, one, 0) + dp(zero -1, one, 1)
        #         if zero > limit:
        #             res -= dp(zero - limit -1, one, 1)
        #         else:
        #             res = dp(zero, one - 1, 0) + dp(zero, one - 1, 1)
        #             if one > limit:
        #                 res -= dp(zero, one - limit - 1, 0)

        #         return res % mod
            
        #     return (dp(zero, one, 0) + dp(zero, one, 1)) % mod