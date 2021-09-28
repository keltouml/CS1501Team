# Ariel Liu (al2ka)
# 9. palindrome number

class Solution:
    def isPalindrome(self, x: int) -> bool:
    	if x < 0:
    		return False
    	else:
    		if str(x) == str(x)[::1]:
    			return True 
    		else:
    			return False