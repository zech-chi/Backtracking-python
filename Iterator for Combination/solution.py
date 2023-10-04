class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.n = combinationLength
        self.table = [None for _ in range(combinationLength)]
        self.index = 0
        self.res = []
        self.backtrack()
        self.len = len(self.res)
        self.cur_index = 0


    def backtrack(self):
        if self.index == self.n:
            self.res.append("".join(self.table))
            return
        
        for c in self.chars:
            if self.index == 0:
                self.table[self.index] = c
                self.index += 1
                self.backtrack()
                self.index -= 1
            else:
                if self.table[self.index - 1] < c:
                    self.table[self.index] = c
                    self.index += 1
                    self. backtrack()
                    self.index -= 1

    def next(self) -> str:
        self.cur_index += 1
        return self.res[self.cur_index - 1]

    def hasNext(self) -> bool:
        return self.cur_index != self.len
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
