class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}
        for i in range(len(s)):
            if seen.get(s[i]) == None:
                seen[s[i]] = 1
            else:
                seen[s[i]] += 1

            if seen.get(t[i]) == None:
                seen[t[i]] = -1
            else:
                seen[t[i]] -= 1
        
        for n in seen:
            if seen[n] != 0:
                return False
        return True