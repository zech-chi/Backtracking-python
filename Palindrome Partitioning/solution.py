class Solution:
    def isPalindrome(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return 0
            l += 1
            r -= 1
        return 1

    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(i, cur_palindrome):
            if i == len(s):
                res.append(cur_palindrome.copy())
            
            start = i
            for end in range(i, len(s)):
                if self.isPalindrome(s[start: end + 1]):
                    cur_palindrome.append(s[start: end + 1])
                    backtrack(end + 1, cur_palindrome)
                    cur_palindrome.pop()

        
        backtrack(0, [])
        return res
