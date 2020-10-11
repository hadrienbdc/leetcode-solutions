from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        dict_ = Counter(s)
        visited = set()
        stack = []
        for i in range(len(s)):
            dict_[s[i]] -= 1
            if s[i] not in visited:
                while stack and stack[-1] > s[i] and dict_[stack[-1]]:
                    last = stack.pop()
                    visited.remove(last)

                visited.add(s[i])
                stack.append(s[i])

        result = "".join(stack)

        return result
