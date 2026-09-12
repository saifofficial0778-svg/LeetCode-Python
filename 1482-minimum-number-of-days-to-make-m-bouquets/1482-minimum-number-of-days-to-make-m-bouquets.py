class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        # Total flowers required
        if m * k > n:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while low < high:
            days = (low + high) // 2

            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                high = days
            else:
                low = days + 1

        return low