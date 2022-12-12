import math
import os
import random
import re
import sys
from datetime import datetime
import string
import itertools as it

class Tasks:
    def plusMinus(self, arr):
        """
        Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
        Print the decimal value of each fraction on a new line with  places after the decimal.
        """
        positive = 0
        negative = 0
        null = 0
        n = len(arr)
        positive = [i for i in arr if i> 0]
        negative = [i for i in arr if i < 0]
        null = [i for i in arr if i == 0]
        print(f"{len(positive) / n:.6}")
        print(f"{len(negative) / n:.6}")
        print(f"{len(null) /     n:.6}")
    
    def miniMaxSum(self, arr):
        """
        Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
        Then print the respective minimum and maximum values as a single line of two space-separated long integers.
        """
        arr = sorted(arr)
        print(sum(arr[:-1]), sum(arr[1:]))
    
    def timeConversion(self, s):
        """
        Given a time in -hour AM/PM format, convert it to military (24-hour) time. 
        Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
        - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
        """
        s = datetime.strptime(s, "%I%M%S%p")
        print(datetime.strftime(s, "%H:%M:%S"))
        return datetime.strftime(s, "%H:%M:%S")
    
    def matchingStrings(self, strings, queries):
        """
        There is a collection of input strings and a collection of query strings. 
        For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
        """
        count = []
        for query in queries:
            i = strings.count(query)
            count.append(i)
        print(count)
        return count
    
    def lonelyinteger(a):
        """
        Given an array of integers, where all elements but one occur twice, find the unique element.
        """
        j = []
        for i in a:
            j.append(a.count(i))
        ind= j.index(1)
        print(a[ind])
        return(a[ind])
    
    def flippingBitsFirst(self, n):
        binary_value = ''
        binary = '{0:b}'.format(n)
        length = 32 - len(binary)
        binary = binary
        
        for i in binary:
            if i == "1":
                binary_value =  binary_value   + '0' 
            elif i == "0":
                binary_value = binary_value + '1'
        print(binary)
        print(binary_value)
        return int("1" *length + binary_value, 2)
        
    def flippingBitsSecond(self, n):
        return (2**32 - 1 - n )
    
    def diagonalDifference(self, arr):
        """
        Given a square matrix, calculate the absolute difference between the sums of its diagonals.
        """
        sum_first = 0
        sum_second = 0
        n = len(arr[0])
        print(n)
        for i in range(0,n):
            print(i)
            sum_first += arr[i][i]
            sum_second += arr[i][n-1 - i]
        return abs(sum_second - sum_first)
    
    def countingSort(self, arr):
        """
        Quicksort usually has a running time of , but is there an algorithm that can sort even faster? 
        In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. 
        At the end, run through your counting array, printing the value of each non-zero valued index that number of times.
        For this exercise, always return a frequency array with 100 elements.
        """
        foo = [0]*100
        for val in arr:
                foo[val] += 1
        return(foo)
    
    def countingSortSecond(self, arr):
        return [arr.count(i) for i in range(100)]  

    def twoArrays(self,k, A, B):
        # Write your code here
        A.sort(reverse=True)
        B.sort(reverse=False)
        print(A,B)
        for i in range(0, len(A)):
            if A[i] + B[i] < k:
                return 'NO'
        return 'YES'
    
    def pangrams(self, s):
        """
        Вам задана строка , состоящая из пробелов и латинских букв. Строка называется панграммой, если она содержит каждую из 26 латинских букв хотя бы раз. Определите является ли строка  панграммой.
        Parameters
        ----------
        S : str, required
            входная строка
        """
        alphabet = set(string.ascii_lowercase)
        symbols = set(s.replace(" ", '').lower())
        if len(alphabet.intersection(symbols)) == 26:
            return 'pangram'
        else:
            return 'not pangram'
    
    def birthday(self, s, d, m):
        """
        проверяет сколько в последованности s , m- суммированных элементов чтобы получить число d
        (ррабоает только для 2 размерных членов)
        Parameters
        ----------
        s: list , required
                sequence of numbers
        d: int , required 
                target value
        m: int ,required
                the count of summing elements
        
        """
        k = 0
        sum_value = s[0]
        ind = [1]
        print(f'list - {ind}')
        for i in range(1, len(s)+ 1):      
            if sum_value <= d  and len(ind) <= m:
                if sum_value == d and len(ind) == m:
                    k += 1
                    print(k)
                    sum_value = s[i-1]
                    ind =[].append(i-1)
                    
                for j in range(i , len(s)):
                    print(f'({i - 1, j} - index) - sum ={sum_value + s[j]}, ind = {ind}')
                
                    if sum_value + s[j] <= d  and len(ind)+ 1 <= m:
                        sum_value = sum_value + s[j]
                        ind.append(j)
                        print(f"sum = s[i-1] + s[j] and items= {i-1, j}")
                        if sum_value == d and len(ind) == m:
                            k += 1
                            print(k)
                            sum_value = s[i -1]
                            ind = [i]
                    else:
                        ind = [i]
                        sum_value = s[i - 1]                     
       
        return k
    
    def birthdaysecond(self, s, d, m):
        """
        comb = it.permutations(a, 2) # it.combinations если не хотите учитывать обратные перестановки
        count combination of elements to get the equlent sum
        """
        comb = it.combinations(s, m)
        new_comb = [tuple(sorted(i)) for i in comb if sum(i) == d]
        print(set(new_comb))
        return(len(set(new_comb)))    

    def flippingMatrix(matrix):
        n = (len(matrix)) 
        s= 0 
        print(matrix)
        for i in range(int(n//2)):
            for j in range(int(n//2)):
                s += max(matrix[i][j ], matrix[i][n - j - 1], matrix[n-i-1][j], matrix[n-i-1][n - j -1])
        return s
    
    def mostActive(self, customers):
        """
        An institutional broker wants to review their book of customers to see which are most active.  Given a list of trades by customer name, determine which customers account for at least 5% of the total number of trades.  Order the list alphabetically ascending by name.
        """
        """
        n=len(customers)
        res=dict()
        for i in customers:
            if i not in res:
                res[i]=1
            else:
                res[i]+=1
        perc=dict()
        for i in res:
            perc[i]= (res[i]/n)*100
        b=[]
        for i in perc:
            if perc[i]>=5:
                b.append(i)
        return(sorted(b))
        """
        appearance = []
        customers_set = (set(customers))
        n = len(customers)
        for i in customers_set:
            if customers.count(i) / n  >= 0.05:
                appearance.append(i)
        
        return sorted(appearance)
    
    def maxCost(self, cost, labels, dailyCount):
        """
        A company manufactures a fixed number of laptops every day. However, if some defect is encountered during the testing of a laptop, it is labeled as “illegal” and is not counted in the laptop count of the day. 
        Given the cost to manufacture each laptop, its label as "illegal" or "legal", and the number of legal laptops to be manufactured each day, find the maximum cost incurred by the company in a single day in manufacturing all the laptops.
        """
        day = 0
        sum_price = 0
        sum_price_second = 0
        for i in range(len(cost)):            
            if labels[i] == 'legal':
                print('legal -', i)
                day += 1
                sum_price += cost[i]
            elif labels[i] == 'illegal':
                print('illegal - ', i)
                sum_price += cost[i]
            
            if day == dailyCount:
                day = 0
                sum_price_second = max(sum_price, sum_price_second)
                print(sum_price)
                print(i)
                sum_price = 0
    
        return sum_price_second
       
    def ParallelProcesing(files, numCores, limit):
        """
        A computer has a certain number of cores and a list of files that need to be executed. If a file is executed by a single core, the execution time equals the number of lines of code in the file. If the lines of code can be divided by the number of cores, another option is to execute the file in parallel using all the cores, in which case the execution time is divided by the number of cores. However, there is a limit as to how many files can be executed in parallel. Given the lengths of the code files, the number of cores, and the limit, what is the minimum amount of time needed to execute all the files?
        """
        lim = 0
        time = 0
        files= sorted(files,  reverse=True)
        for i in files:
            if i % numCores == 0 and lim < limit:
                time += i / numCores
                lim += 1
            else:
                time += i
        return int(time)
        
    

first_task = Tasks()
print(first_task.maxCost([2,5, 3, 11, 1],  ["legal", "illegal", "legal", "legal", "legal"], 2 ))
