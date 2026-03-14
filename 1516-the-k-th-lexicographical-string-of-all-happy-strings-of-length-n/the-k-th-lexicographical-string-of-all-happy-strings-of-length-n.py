class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.current_string = ""
        self.result = ""
        self.index_in_sorted_list = 0

        def generate_happy_strings(n, k):
            if len(self.current_string) == n:
                self.index_in_sorted_list += 1
                if self.index_in_sorted_list == k:
                    self.result = self.current_string
                return

            for current_char in ['a','b','c']:
                if len(self.current_string) > 0 and self.current_string[-1] == current_char:
                    continue
                self.current_string += current_char
                generate_happy_strings(n, k)
                if self.result != "": return
                self.current_string = self.current_string[:-1]


        generate_happy_strings(n, k)
        return self.result
        