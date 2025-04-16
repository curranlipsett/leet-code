from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToChar = {
          "2" : "abc",
          "3" : "def",
          "4" : "ghi",
          "5" : "jkl",
          "6" : "mno",
          "7" : "pqrs",
          "8" : "tuv",
          "9" : "wxyz"
        }

        resultset = []


        def backtrack(i, currentStr):
            if len(currentStr) == len(digits):
                resultset.append(currentStr)
                return
            
            for character in digitsToChar[digits[i]]:
                backtrack(i + 1, currentStr + character)

        if digits:
            backtrack(0, "")

            
        return resultset

if __name__ == "__main__":
    mySol = Solution()
    print(mySol.letterCombinations("23"))
