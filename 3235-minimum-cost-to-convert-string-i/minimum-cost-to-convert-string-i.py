class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        adjacency_list = [[] for i in range(26)]

        conversion_count = len(original)
        for i in range(conversion_count):
            adjacency_list[ord(original[i]) - ord("a")].append(
                (ord(changed[i]) - ord("a"), cost[i])
            )

        min_conversion_costs = [
            self._dijkstra(i, adjacency_list) for i in range(26)
        ]
        
        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                char_conversion_cost = min_conversion_costs[ord(s) - ord("a")][ord(t) - ord("a")
                ]
                if char_conversion_cost == -1:
                    return -1
                total_cost += char_conversion_cost

        return total_cost


    def _dijkstra(self, start_char, adjacency_list):
        priority_queue = [(0, start_char)]

        min_costs = [-1] * 26

        while priority_queue:
            current_cost, current_char = heapq.heappop(priority_queue)

            if min_costs[current_char] != -1 and min_costs[current_char] < current_cost:
                continue

            min_costs[current_char] = current_cost

            for target_char, conversion_cost in adjacency_list[current_char]:
                new_total_cost = current_cost + conversion_cost
                if min_costs[target_char] == -1 or new_total_cost < min_costs[target_char]:
                    min_costs[target_char] = new_total_cost
                    heapq.heappush(priority_queue, (new_total_cost, target_char))

        return min_costs