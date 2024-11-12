class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if len(str(x)) == 1:
            return True
        
        if len(str(x)) == 2:
            return str(x)[0] == str(x)[1]
        
        if str(x)[0] == str(x)[-1]:
            return self.isPalindrome(str(x)[1:-1])
        else:
            return False
            
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(1234567890987654321))