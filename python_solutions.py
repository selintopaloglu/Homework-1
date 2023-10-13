#INTRODUCTION

# Say "Hello, World!" With Python

print("Hello, World!")


#Python If-Else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2 != 0:     
    print("Weird")
else:
    if n>=2 and n<=5:
        print("Not Weird")
    if n>=6 and n<=20:
        print("Weird")
    if n>20:
        print("Not Weird")    

#Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)


#Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(float(a/b))

#Loops

if __name__ == '__main__':
    n = int(input())
    
for i in range(n):
    print (i**2)

#Write a function

def is_leap(year):
    leap = False
    
    if year % 4 ==0:
        if year%100 ==0:
            if year%400==0:
                leap= True
                
        else:
            leap= True    
            
            
    
    return leap

year = int(input())

#Print Function

if __name__ == '__main__':
    n = int(input())
    k = ""
    for i in range(1,n+1):
        k+= str(i)
    print (k)    


#DATA TYPES

#List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
List=[[i,j,k] for i in range (x+1) for j in range (y+1) for k in range (z+1) if i+j+k!=n]

print (List)

#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    List=list(arr)
    maximum=max(List)
    while maximum in List:
        List.remove(maximum)
    print(max(List))    

#Nested Lists

if __name__ == '__main__':
    List=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        List.append([name, score])
    List.sort(key=lambda x: (x[1], x[0]))  
    lowest=None
    for i in List:
        if i[1]>List[0][1]:
            lowest=i[1]
            break
    name = [i[0] for i in List if i[1]== lowest]  
    name.sort() 
    for j in name:
        print (j)     

#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    esas=student_marks[query_name]
    average=sum(esas)/len(esas)
    print("{:.2f}".format(average))

#Lists

if __name__ == '__main__':
    N = int(input())
    List=[]
    for i in range(N):
        komut=input().split()
        esas=komut[0]
        if esas == "insert":
            i, e= map (int, komut[1:])
            List.insert(i, e)
        if esas== "print":
            print(List)
        if esas== "remove":
            List.remove(int(komut[1]))
        if esas== "append":
            List.append(int(komut[1]))
        if esas== "sort":
            List.sort()
        if esas== "pop":
            List.pop()
        if esas== "reverse":
            List.reverse()
                              
#Tuples

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
string=input().split()
Tup=tuple(map(int, string))


esas=hash(Tup)   
print(esas)    
    
#sWAP cASE

def swap_case(s):
    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join

def split_and_join(line):
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#STRINGS
#What's Your Name?

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Mutations

def mutate_string(string, position, character):
    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Find a string

def count_substring(string, sub_string):
    return

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#String Validators

if __name__ == '__main__':
    s = input()
    has_alphanumeric = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False
    
    for i in s:
        if i.isalnum():
            has_alphanumeric = True
        if i.isalpha():
            has_alpha = True
        if i.isdigit():
            has_digit = True
        if i.islower():
            has_lower = True
        if i.isupper():
            has_upper = True
    
    print(has_alphanumeric)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)

#Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c +
           (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

#Text Wrap

import textwrap

def wrap(string, max_width):
    new=""
    for i in range(len(string)):
        if (i+1)%max_width==0:
            new+=string[i]+"\n"
        else:
            new+=string[i]   
    return new         
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
def func(n):
    for i in range(n//2):
        ilk='.|.' * (2 * i +1)
        print(ilk.center(n*3, "-"))
        
    print('WELCOME'.center(n * 3, '-'))
    
    for i in range(n // 2 - 1, -1, -1):
        ilk='.|.' * (2 * i + 1)
        print(ilk.center(n*3, "-"))
        
if __name__ == "__main__":
    n = input().split()
    func(int(n[0]))  

#String Formatting

def print_formatted(number):
    w=bin(number)[2:]
    l=len(w)
    text=""
    for i in range(1, number+1):
        d=str(i).rjust(l)
        o=oct(i)[2:].rjust(l)
        h=hex(i)[2:].upper().rjust(l)
        b=bin(i)[2:].rjust(l)
        text+=(f"{d} {o} {h} {b}\n")    
    
    print(text)
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Alphabet Rangoli


def print_rangoli(size):
    import string
    
    alphabet = string.ascii_lowercase
    
    rangoli_lines = []
    
    for i in range(size):
        # Create a segment of the rangoli for each letter
        segment = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        rangoli_lines.append(segment.center(size * 4 - 3, '-'))
    
    # Create the full rangoli by joining the top half and its reverse
    full_rangoli = rangoli_lines + rangoli_lines[:-1][::-1]
    
    return '\n'.join(full_rangoli)
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#Capitalize!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    k=s.split(" ")
    t=""
    for i in k:
        t+=i.capitalize()+" "
        
    return t.strip()    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#The Minion Game

def minion_game(string):
    sesli="AEIOU"
    a=0
    b=0
    l=len(string)
    
    for i in range(l):
        if string[i] in sesli:
            a+=l-i
        else:
            b+=l-i
            
    if a>b:
        print("Kevin", a) 
    elif b>a:
        print("Stuart", b)
    else:
        print("Draw")               

if __name__ == '__main__':
    s = input()
    minion_game(s)

# Merge the Tools!

def merge_the_tools(string, k):
    l=len(string)
    
    for i in range(0, l, k):
        sonuc=""
        kelime=set()
        kelimecik=string[i:i+k]
        for j in kelimecik:
            if j not in kelime:
                kelime.add(j)
                sonuc+=j    
        print(sonuc)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
     
#SETS

#Introduction to Sets

def average(array):
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#No Idea!

def calculate_happiness(arr, set_A, set_B):
    happiness = 0

    for num in arr:
        if num in set_A:
            happiness += 1
        elif num in set_B:
            happiness -= 1

    return happiness

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    set_A = set(map(int, input().split()))
    set_B = set(map(int, input().split()))
    
    result = calculate_happiness(arr, set_A, set_B)
    print(result)


#Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
a=list(map(int, input().split()))
n=int(input())
b=list(map(int, input().split()))
ortak=set()
for i in a:
    if i not in b:
        ortak.add(i)
for j in b:
    if j not in a:
        ortak.add(j)
genel=list(ortak)
genel.sort()       
for i in genel:
    print(i)                


#Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
country=set()
for i in range(N):
    country.add(input())
    
print(len(country))    

#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
c=int(input())
for i in range(c):
    command=input().split()
    if command[0]== "pop":
        s.pop()
    elif command[0]== "remove":
        e=int(command[1])
        s.remove(e)
    elif command[0]== "discard":
        e=int(command[1])
        s.discard(e)

print(sum(s))      


#Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int, input().split()))
m=int(input())
b=(map(int, input().split()))

t=a.union(b)

print(len(t))


Set .intersection() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
a=set(map(int, input().split()))
m=int(input())
b=set(map(int, input().split()))

k=a.intersection(b)

print(len(k))

#Set .difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int, input().split()))
m=int(input())
b=set(map(int, input().split()))

t=a.difference(b)

print(len(t))

#Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
a=set(map(int, input().split()))
m=int(input())
b=set(map(int, input().split()))

t=a.symmetric_difference(b)

print(len(t))

#Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())

s=set(map(int, input().split()))
opera=int(input())

for i in range(opera):
    operation=input().split()
    diger=set(map(int, input().split()))
    if operation[0]=="intersection_update":
        s.intersection_update(diger)
    elif operation[0]=="update":
        s.update(diger)  
    elif operation[0]==  "symmetric_difference_update":
        s.symmetric_difference_update(diger)
    elif operation[0]== "difference_update":
        s.difference_update(diger)
        
print(sum(s))        
    
#The Captain's Room

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
def func(sayi, liste):
    asil=Counter(liste)
    for oda, kac in asil.items():
        if kac==1:
            return oda

n=int(input())
liste=list(map(int, input().split()))
print(func(n, liste))

#Check Subset

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    n_a=int(input())
    a=set(map(int, input().split()))
    n_b=int(input())
    b=set(map(int, input().split()))
    print(a.issubset(b))


#Check Strict Superset

# Enter your code here. Read input from STDIN. Print output to STDOUT

a=set(map(int, input().split()))
n=int(input())
result=True
for i in range(n):
    k=set(map(int, input().split()))
    if a.issuperset(k) and a!=k:
        result=True
    else:
        result= False
        break    
print(result)

#COLLECTIONS
#collections.Counter()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n=int(input())
shoes=list(map(int, input().split()))
liste=Counter(shoes)
m=int(input())
total=0

for i in range(m):
    size, prize=map(int, input().split())
    
    if size in liste.keys() and liste[size]> 0:
        total+=prize
        liste[size]-=1
print(total)        
        
#DefaultDict Tutorial

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m=map(int, input().split())
d=defaultdict(list)
k=[]
for i in range(1,n+1):
    d[input()].append(i)
    
for j in range(1, m+1):
    harf=input()
    if harf in d:
        print(*d[harf])
    else:
        print(-1)    
        
    
#Collections.namedtuple()

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple
n, title=int(input()), input().split()
total=0
student=namedtuple("student", title)
for i in range(n):
    data=student(*input().split())
    total+=int(data.MARKS)
print("{:.2f}".format(total/n))    
    

#Collections.OrderedDict()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n=int(input())
meyve=OrderedDict()

for i in range(n):
    t=input().split()
    fruit=" ".join(t[:-1])
    sayi=int(t[-1])
    if fruit in meyve:
        meyve[fruit]+=sayi
    else:
        meyve[fruit]=sayi
        
for i, j in meyve.items():
    print(i,j)


#Word Order

n=int(input())
word=[]
count={}

for i in range(n):
    w=input().strip()
    if w in count:
        count[w]+=1
    else:
        count[w]=1
        word.append(w)
        
print(len(word))
print(" ".join(str(count[i]) for i in word))        
            
#Collections.deque()

from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    command = input().split()
    if command[0] == 'append':
        d.append(int(command[1]))
    elif command[0] == 'appendleft':
        d.appendleft(int(command[1]))
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()

print(" ".join(map(str, d)))

#Company Logo

#!/bin/python3
from collections import OrderedDict
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]= 1
           
    sort=sorted(d.items(), key=lambda x: (-x[1], x[0]))  
    for i in range(3):
        if i < len(sort):
            char, count = sort[i]
            print(char, count)    

#Piling Up!

# Enter your code here. Read input from STDIN. Print output to STDOUT
def func(cubes):
    left = 0
    right = len(cubes) - 1
    once = max(cubes[left], cubes[right]) + 1

    while left <= right:
        if cubes[left] >= cubes[right] and cubes[left] <= once:
            once = cubes[left]
            left += 1
        elif cubes[right] >= cubes[left] and cubes[right] <= once:
            once = cubes[right]
            right -= 1
        else:
            return "No"

    return "Yes"

t = int(input())
for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    result = func(cubes)
    print(result)

#DATE AND TIME

#Calendar Module

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

date = input().split(" ")
month = int(date[0])
day = int(date[1])
year = int(date[2])


calendar.setfirstweekday(calendar.SUNDAY)

try:
    day_of_week = calendar.weekday(year, month, day)
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    print(days[day_of_week])
except ValueError:
    print("Invalid date")


#Time Delta

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    ftm="%a %d %b %Y %H:%M:%S %z"
    
    datetime_1= datetime.strptime(t1, ftm )
    datetime_2= datetime.strptime(t2, ftm )
    
    fark=abs(datetime_2-datetime_1)
    return str(int(fark.total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#EXCEPTIONS

#Exceptions

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
for i in range(n):
    s=input().split()
    try:
        print(int(int(s[0])/int(s[1])))
    except ZeroDivisionError as e:
        print ("Error Code: integer division or modulo by zero")
    except ValueError as b:
        print("Error Code:",b)


#Built-ins!

#Zipped!

n, m = map(int, input().split())
marks = []

for i in range(m):
    marks.append(list(map(float, input().split())))

for i in range(n):
    total = 0
    for j in range(m):
        total += marks[j][i]
    average = total / m
    print("{:.1f}".format(average))


#Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=lambda x: x[k])
    for i in arr:
        print(" ".join(map(str, i)))


#ginortS

# Enter your code here. Read input from STDIN. Print output to STDOUT

def sorting(harf):
    if harf.islower():
        return (0, harf)
    elif harf.isupper():
        return (1, harf)
    elif harf.isdigit():
        if int(harf)%2==1:
            return (2, harf)
        else:
            return(3, harf)
            
s=input()
asil=sorted(s, key=sorting)
print("".join(asil))    
        
        
#PYTHON FUNCTIONALS

#Map and Lambda Function

cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    fib=[0, 1]
    while len(fib)<n:
        son=fib[-1]+fib[-2]
        fib.append(son)
    return fib [:n]

#REGEX AND PARSING

#Detect Floating Point Number

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def valid(s):
    kural=r"^[+-]?\d*\.\d+$"
    return re.match(kural, s) is not None
n=int(input())

for i in range(n):
    s=input()
    print(valid(s))

#Re.split()

regex_pattern = r"[,.]"	# Do not delete 'r'.


#Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    sorted_candles=sorted(candles, reverse=True)
    total=0
    n=len(sorted_candles)
    for i in range(n):
        if sorted_candles[i]==sorted_candles[0]:
            total+=1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    
    while (x2>x1 and v1>v2) or (x1>x2 and v2>v1):
        x2+=v2
        x1+=v1
        if x2==x1:
            return "YES"
    return "NO"        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    pay=5
    kum=0
    
    for i in range(1, n + 1):
        begen=pay//2
        kum+=begen
        pay=begen*3
    return kum    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


#Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    def calc_super_digit(num_str):
        if len(num_str) == 1:
            return int(num_str)
        digit_sum = sum(int(digit) for digit in num_str)
        return calc_super_digit(str(digit_sum))

    initial_super_digit = calc_super_digit(n)
    return calc_super_digit(str(initial_super_digit * k))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


#Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    deger = arr[n - 1]

    i = n - 2
    while i >= 0 and arr[i] > deger:
        arr[i + 1] = arr[i]
        i -= 1
        print(" ".join(map(str, arr)))

    arr[i + 1] = deger
    print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

    
    

    
    



