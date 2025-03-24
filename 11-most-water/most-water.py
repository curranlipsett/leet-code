# Pointer at each end of array, advance pointer with lower value
# When pointers point to equal values, advance both
# When pointers point to the same index, stop
# Each time a pointer moves, calculate the area and compare to max
class Solution:

    def findMostAreaBetweenIndicies(self, inputArr):
        arrayLen = len(inputArr)
        leftPointer = 0
        rightPointer = arrayLen - 1

        # Base cases for length 0, 1, and 2
        if arrayLen == 0:
            return 0
        if arrayLen == 1:
            return inputArr[0]
        if arrayLen == 2:
            return min(inputArr[0], inputArr[1])
        # Intial max is lower index value * len of array - 1
        maxArea = min(inputArr[leftPointer], inputArr[rightPointer]) * (arrayLen - 1)

        while leftPointer <= rightPointer:
            localArea = 0
            if inputArr[leftPointer] > inputArr[rightPointer]:
                localArea = min(inputArr[leftPointer], inputArr[rightPointer]) * (rightPointer - leftPointer)
                rightPointer -= 1
            elif inputArr[leftPointer] < inputArr[rightPointer]:
                localArea = min(inputArr[leftPointer], inputArr[rightPointer]) * (rightPointer - leftPointer)
                leftPointer += 1
            else:
                # Pointing to same value, move both pointers
                localArea = min(inputArr[leftPointer], inputArr[rightPointer]) * (rightPointer - leftPointer)
                leftPointer += 1
                rightPointer -= 1
            
            if localArea > maxArea:
                maxArea = localArea

        return maxArea


if __name__ == "__main__":
    sol = Solution()
    myArr = [1,0,0,0,0,0,0,2,2]
    myArr4 = [55]
    myArr5 = [5, 8]
    print("Got:", sol.findMostAreaBetweenIndicies(myArr), " expected: 8")
    print("Got:", sol.findMostAreaBetweenIndicies(myArr4), " expected: 55")
    print("Got:", sol.findMostAreaBetweenIndicies(myArr5), " expected: 5")

