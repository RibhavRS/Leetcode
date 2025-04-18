class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(abs(x))
        reversed_num = int(str_num[::-1])
        if x < 0:
            reversed_num = -reversed_num
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num

        
      