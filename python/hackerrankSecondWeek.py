import math
import os
import random
import re
import sys
from datetime import datetime
import string
import itertools as it

class Tasks:
    arr_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    arr_en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
    
    def findZigZagSequence(self, a, n):
        """
        a.sort()
        k=int((n+1)/2)
        x=a[:k-1]
        y=a[k-1:][::-1]
        z=x+y
        for each in z:
        print(each,end = ' ')
            
        """
        a.sort()
        mid = int((n + 1)/2)-1 # subtracted 1
        a[mid], a[n-1] = a[n-1], a[mid]

        st = mid + 1
        ed = n - 2 #changed 1 to 2
        while(st <= ed):
            a[st], a[ed] = a[ed], a[st]
            st = st + 1
            ed = ed - 1 #changed '+' to '–'

        for i in range (n):
            if i == n-1:
                print(a[i])
            else:
                print(a[i], end = ' ')
        return a
    
    def sockMerchant(self, n, ar):
        """
        There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
        """
        
        """
        couple = False
        k = 0
        couple = False
        arr = sorted(ar)
        print(arr)
        for i  in range(0, n-1):
            if arr[i] == arr[i+1] and couple == False:
                couple = True
                
            elif couple:
                couple = False            
                
            print(i, '-', arr[i],' ', arr[i+1], 'bool -', couple)    
            if couple != True and arr[i] != arr[i-1]:
                k+= 1
        print(k)
        """
        return sum([ar.count(i) // 2 for i in set(ar)])
    
    def pageCount(n, p):
        print(int(n / 2))
        if  ( int(n / 2) > p    ):
            return p // 2 
        else:
            return (n - p) // 2 
        
    def pageCount(n, p):
        """
        A teacher asks the class to open their books to a page number. 
        A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page  is always on the right side:
        """
        mid = n // 2

        if p > mid and n % 2 == 0:
            return ( n - p  + 1 )// 2
        elif p > mid and n % 2 != 0:
            return ( n - p   )// 2         
        else:
            return (p ) // 2

    def caesarCipher(self, s, k):
        """
        Caesar Cipher 
        Parametrs:
        s - string 
        k = koef 
        """
        new_str = ''
        for char in s:
            if char in self.arr_en:
                ind = self.arr_en.index(char)
                new_ind = k + ind if  k + ind + 1 < len(self.arr_en) else abs( ( (k + ind   )  % 26))
                print(f"""char:{char}, index:{ind} , new_index:{new_ind} -   {k + ind} """ )
                new_char = str(self.arr_en[new_ind ])
                new_str = new_str+ new_char
                
            elif char in self.arr_en:
                ind = self.arr_en.index(char)
                new_ind = k + ind if  k + ind + 1 < len(self.arr_en)  else abs(((k + ind   )  % 26))
                print(f"""char:{char}, index:{ind} , new_index:{new_ind} -   {abs( (k + ind) )} """ )
                new_char = str(self.arr_en[new_ind])
                new_str = new_str+ new_char
                
            else:
                print(char)
                new_str = new_str + char
                
                
        return new_str

    
   
    

first_task = Tasks()
