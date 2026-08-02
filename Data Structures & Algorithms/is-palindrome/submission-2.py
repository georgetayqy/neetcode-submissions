class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        if len(s) <= 1:
            # a string of length 1 is always palindromic
            # a string of length 0 is palindromic vacuously
            return True

        while left < right:
            while left < right and not self.isalnum(s[left]):
                # if all are not alphanumeric, then, when we remove
                # all of the non-alphanumeric stuff, it will become
                # an empty string and hence is palindromic
                left += 1

            while right > left and not self.isalnum(s[right]):
                # if the first part passes, then we can assume that
                # there is at least one alphanumeric char
                # and this will terminate
                right -= 1

            # when both loops terminate, either because all are non-alphanumeric
            # or when an alphanumeric character is found, we can be sure that
            # both pointers will point to an alphanumeric character
            if s[left].lower() != s[right].lower():
                return False

            # advance both pointers to get the next element to check
            left += 1
            right -= 1

        return True

    def isalnum(self, char):
        ord_char = ord(char)

        return (
            (ord("A") <= ord_char <= ord("Z")) or
            (ord("a") <= ord_char <= ord("z")) or
            (ord("0") <= ord_char <= ord("9"))
        )
