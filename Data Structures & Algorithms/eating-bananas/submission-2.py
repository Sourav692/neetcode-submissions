class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        while left <= right:
            speed = (left + right) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / speed)

            if totalTime <= h:
                ans = speed
                right = speed - 1
            else:
                left = speed + 1
        return ans