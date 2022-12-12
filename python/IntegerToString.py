class Solution:
    digits = [
            "Zero", " One", " Two",   " Three", " Four",
            " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven",  
            " Twelve", " Thirteen",  " Fourteen", " Fifteen", " Sixteen",
            " Seventeen", " Eighteen", " Nineteen"
        ]
    tens = [
            " Twenty", " Thirty", " Forty",  " Fifty",
            " Sixty",  " Seventy", " Eighty", " Ninety"
        ]
    
    rank = {
           0 : "", 3 : " Thousand", 6 : " Million",9 : " Billion"
        }
        
        
    def getHundread(self, num: int) -> str:
            str_num =''

            if ( num  >= 100):
                str_num +=  self.digits[num // 100 ] + " Hundred"
                num = num % 100
            if ( num >= 20):
                str_num += self.tens[ num // 10 -2 ] 
                num = num % 10
            if (num >=10 ):
                str_num += self.digits[num]
                return str_num
            if (num > 0):
                str_num += self.digits[num % 10 ] 
                return str_num
            return str_num
            
        
    def numberToWords(self, num: int) -> str: 
            if num == 0:
                return "Zero"
            dig_num = len(str(num))
            i = 0
            str_num = ''
            while i < dig_num:
                if (num > 0): 
                    if num % 1000 > 0:
                     #   print(10** (i+2) )
                        rank = self.rank[i]
                    else:
                        rank = ''  
                    str_num = self.getHundread(num % 1000)+ rank + str_num
                    num = num // 1000
                    i += 3
            return str.strip(str_num)