class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last ={}
        for i, c in enumerate(s):
            if c in last:
                last[c] = max(i, last[c])
            else: 
                last[c] = i
        p = 0
        count = 0
        out = []
        highest_index = 0
        start = p
        while p < len(s):
            end = last[s[p]]

            if highest_index < end:
                highest_index = end

            count += 1

            if p == highest_index:
                out.append(count)
                count = 0
                start = p + 1

            p += 1
        return out