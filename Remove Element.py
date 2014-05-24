class Solution:
    def removeElement(self, A, elem):
        length = len(A)
        last, i = length - 1, 0
        while i <= last:
            if A[i] == elem:
                A[i], A[last] = A[last], A[i]
                last -= 1
            else:
                i += 1
        return last + 1