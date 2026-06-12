class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i = 0
        j = 0
        result = []

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            start = max(start1, start2)
            end = min(end1, end2)

            if start <= end:
                result.append([start, end])

            if end1 < end2:
                i += 1
            else:
                j += 1

        return result