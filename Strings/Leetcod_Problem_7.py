class Solution:
    def reverse(self, x: int) -> int:
        
         is_nagative = False
         minus_sign = "-"

         string_number = str(x)

         reverse_num = string_number[::-1]

         if reverse_num[-1] == "-":
              reverse_num = reverse_num[:-1]
              is_nagative = True
        
         if is_nagative:
              reverse_num = minus_sign + reverse_num
              
        
         num = int(reverse_num)
         
         if num < -2147483648 or num > 2147483647:
              return 0

         return num

