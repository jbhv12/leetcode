class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l=[first]
        for e in encoded:
            l.append(e^l[-1])
        return l