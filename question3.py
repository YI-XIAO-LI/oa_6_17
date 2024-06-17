from itertools import combinations

class Solution:
    def calculateVal(self, l):
        maxVal = 0
        l.sort()
        i = 0
        while i < len(l):
            j = i
            ptr = 1
            slide_mean = l[i]
            while j - ptr >= 0 and j + ptr < len(l):
                slide_mean = slide_mean * (1 + 2 * (ptr-1)) + l[j-ptr] + l[j+ptr]
                slide_mean /= (1 + 2 * ptr)
                if abs(slide_mean - l[i] > maxVal):
                    maxVal = slide_mean - l[i]
                ptr += 1

            j = i
            k = i+1
            ptr = 0
            if k + ptr < len(l):
                slide_mean = (l[i]+l[i+1])/2
            while j - ptr >= 0 and k + ptr < len(l):
                slide_mean = slide_mean * (2 + 2 * (ptr-1)) + l[j - ptr] + l[k + ptr]
                slide_mean /= (2 + 2 * ptr)
                if abs(slide_mean - l[i]) > maxVal:
                    maxVal = slide_mean - l[i]
                ptr += 1
            i += 1
        return maxVal


solution = Solution()
print(solution.calculateVal([1, 3, 5, 9]))
print(solution.calculateVal([10, 20]))
print(solution.calculateVal([7]))