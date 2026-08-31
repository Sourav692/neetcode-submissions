class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map2 = {}
        map_s1 = {}
        for i in s1:
            if i in map_s1:
                map_s1[i] += 1
            else:
                map_s1[i] = 1
        left = 0
        for right in range(len(s2)):
            c = s2[right]
            if c in map2:
                map2[c] += 1
            else:
                map2[c] = 1
            if right - left + 1 > len(s1):
                left_char = s2[left]
                map2[left_char] -= 1
                if map2[left_char] == 0:
                    del map2[left_char]
                
                left += 1
            
            if map2 == map_s1:
                return True
        return False

            
