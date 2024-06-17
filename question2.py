class Solution:
    def checkParenthesis(self, s):
        l = []
        res = [" " for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == "(":
                l.append((i, "("))
            elif s[i] == ")":
                if len(l) and l[0][1] == "(":
                    l.pop(0)
                else:
                    res[i] = "?"
        for i in l:
            res[i[0]] = "x"
        return "".join(res)


solution = Solution()
print(solution.checkParenthesis("bge)))))))))"))
print(solution.checkParenthesis("((IIII))))))"))
print(solution.checkParenthesis("()()()()(uuu"))
print(solution.checkParenthesis("))))UUUU((()"))