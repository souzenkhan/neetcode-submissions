class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = "".join(char for char in s if char.isalnum())
        cleaned_str = cleaned_str.lower()
        left = 0 
        right = -1
        while left >= right and left < len(cleaned_str):
            if cleaned_str[left] == cleaned_str[right]:
                left += 1
                right -= 1
                continue
            else:
                return False


        return True
        