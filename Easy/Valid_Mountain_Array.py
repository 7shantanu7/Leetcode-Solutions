class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        result = False
        if len(A) >= 3:
            for x in range(0, len(A)-1):
                if A[x+1] > A[x]:
                    result = True
                else:
                    break

            if result:
                for index in range(x, len(A)-1):
                    if (A[index+1] < A[index]):
                        result = True
                    else:
                        result = False
                        break

        return result