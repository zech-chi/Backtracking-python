class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def cal_poss(n):
            if n == 1:
                return 3
            return 2 * cal_poss(n - 1)
        
        if k > cal_poss(n):
            return ""

        def backtrack(table, index):
            nonlocal counter
            nonlocal k
            nonlocal ans
            if index == n:
                counter += 1
                if counter == k:
                    ans = table
                return
            
            for i in ["a", "b", "c"]:
                if counter < k:
                    if index == 0:
                        table[0] = i
                        backtrack(table, index + 1)
                    else:
                        if table[index - 1] != i:
                            table[index] = i
                            backtrack(table, index + 1)       

        table = [None for _ in range(n)]
        counter = 0
        ans = []
        backtrack(table, 0)
        return "".join(ans)
