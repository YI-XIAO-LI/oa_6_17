class Solution:
    def checkSubstring(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        res = 0
        ptr = 0
        flag = 0
        while ptr < len2:
            i, j = 0, ptr
            while i < len1 and j < len2:
                if s1[i] == s2[j]:
                    j += 1
                i += 1
            # the case where is contains sth other than str1
            if j == ptr:
                flag = 1
                break
            ptr = j
            res += 1

        if flag:
            return -1
        return res


solution = Solution()
print(solution.checkSubstring("abc", "abcbc"))
print(solution.checkSubstring("abc", "abdbc"))
print(solution.checkSubstring("xyz", "xzyxy"))
print(solution.checkSubstring("xyz", ""))
