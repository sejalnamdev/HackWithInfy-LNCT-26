class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s) - 1
        ans = []

        while i >= 0:
            # 1. Skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1

            if i < 0:
                break

            # 2. Find end of word
            j = i

            # 3. Move to start of word
            while i >= 0 and s[i] != " ":
                i -= 1

            # 4. Extract word
            ans.append(s[i+1 : j+1])

        return " ".join(ans)