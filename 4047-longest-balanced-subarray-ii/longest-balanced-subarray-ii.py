class SegmentTree:
    def __init__(self, n):
        self.lazy = [0] * (4 * n)
        self.mx = [0] * (4 * n)
        self.mn = [0] * (4 * n)

    def update(self, node, l, r):
        if self.lazy[node] != 0:
            self.mx[node] += self.lazy[node]
            self.mn[node] += self.lazy[node]
            if l < r:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def change_range(self, node, val, changel, changer, l, r):
        self.update(node, l, r)

        if l > changer or r < changel: return
        if l >= changel and r <= changer:
            self.lazy[node] += val
            self.update(node, l, r)
            return

        mid = l + (r - l) // 2
        self.change_range(node * 2, val, changel, changer, l, mid)
        self.change_range(node * 2 + 1, val, changel, changer, mid + 1, r)

        self.mx[node] = max(self.mx[node * 2], self.mx[node * 2 + 1])
        self.mn[node] = min(self.mn[node * 2], self.mn[node * 2 + 1])

    def left_zero(self, node, l, r):
        self.update(node, l, r)

        if self.mn[node] > 0 or self.mx[node] < 0: return -1

        if l == r:
            if self.mn[node] == 0: return l
            else: return -1

        mid = l + (r - l) // 2
        left = self.left_zero(node * 2, l, mid) 
        if left != -1: return left
        return self.left_zero(node * 2 + 1, mid + 1, r)
    

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prev = {}
        st = SegmentTree(n)

        for r in range(n):
            curr = nums[r]
            val = 1 if curr % 2 == 0 else -1

            if curr in prev: st.change_range(1, -val, 0, prev[curr], 0, n - 1)
            st.change_range(1, val, 0, r, 0, n - 1)
            prev[curr] = r

            l = st.left_zero(1, 0, n - 1)
            if l != -1: res = max(res, r - l + 1)

        return res

        