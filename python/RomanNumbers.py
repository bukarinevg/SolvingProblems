"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Romanian:

    main_values = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
    
    subtract_values = {
        'IV' : 4,
        'IX' : 9,
        'XL' : 40,
        'XC' : 90,
        'CD' : 400,
        'CM' : 900
        }
    
    

    def romanToInt(self, s: str) -> int:
        k = 0
        sum = 0
        for i in s:
            if (s[k:k+2] in self.subtract_values ):
                sum += self.subtract_values[s[k:k+2]]
            elif (k != 0 and s[k-1:k+1] in self.subtract_values  ):
                k+=1
                continue
            else:
                sum += self.main_values[i]   
            k+= 1
        return sum


        main_values = {
        'I' : 1,
        'IV' : 4,
        'V' : 5,
        'IX' : 9,
        'X' : 10,
        'XL' : 40,
        'L' : 50,
        'XC' : 90,
        'C' : 100,
        'CD' : 400,
        'D' : 500,
        'CM' : 900,
        'M' : 1000
        }

    def intToRoman(self, remainder: int) -> str:
        roman = ''
        dictonary = reversed(list(self.main_values.items()))
        k = 0
        for i, value in dictonary:
            if k % 4 == 0  and remainder // value > 0:
                roman += i * (remainder // value)
                remainder = remainder % value
            elif remainder - value >=0 :
                roman += i
                remainder = remainder - value
               
            k += 1
            
        return roman

        if (num // 1000) > 0:
            roman += "M" * (num // 1000)
            num = num % 1000  
        if (num - 900) >= 0:
            print(str(num) + '---')
            roman += "CM"
            num = num - 900
        if (num - 500) >= 0:
            print(num)
            roman += "D"
            num = num - 500
        if (num - 400) >= 0:
            print(num)
            roman += "CD"
            num = num - 400
        if (num // 100) > 0:
            roman += "C" * (num // 100) 
            num = num % 100
        if (num - 90) >= 0:
            roman += "XC"
            num = num - 90
        if (num - 50) >= 0:
            roman += "L"
            num = num - 50
        if (num - 40) >= 0:
            roman += "XL"
            num = num - 40
        if (num // 10) > 0:
            roman += "X" * (num // 10)
            num = num % 10
        if (num - 9) >= 0:
            roman = str(roman + 'IX')
            num = num - 9
        if (num - 5) >= 0:
            roman = str(roman + 'V')
            num = num - 5
        if (num - 4) >= 0:
            roman = str(roman + 'IV')
            num = num - 4
        while (num // 1) > 0:
            roman += "I"
            num = num -1
          
        return roman




#print([i for i in itertools.combinations(nums, 3)])