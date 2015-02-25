
6==6
numlist=range(1,101)
value=numlist[49]
len (numlist)
type (numlist)
float (3.0/2.0)
float (3/2)
3.0/2.0
int(3.0/2.0)
3/float(2)
from_future_import division
import math
math.sqrt(1089)
import math; math.sqrt(1089)
from math import sqrt
sqrt(1089)
math.sqrt(1089)
from math import *
newlist=[0,1,2,3,4,5,6]
newlist[2:5]
d={'a':10,'b':20,'c':30}
d['a']
d['c']=40
d['c']
fruits=['apple','banana','cherry']
for i in range(len(fruits)):
    print fruits[i].upper(),
fruits=['apple','banana','cherry']
for fruit in fruits:
    print fruit.upper()
def calc(a,b):
    return a+b
list1=[1,2]
list2=[2,4]
list1+list2
list1.append(list2)
locations = {'Sinan': ['Baltimore', 'MD'], 'Brandon': ['Arlington', 'VA']}
locations['Sinan'][1]
nums=[1,2,3,5,4,6]
sorted(nums)
nums=[1,2,3,5,4,6]
nums.reverse
f=open('drinks.csv','rU')
f.read()
f.read()
f.close()
f=open('drinks.csv','rU')
f.read(1)
f.readlines(1)
f.close()
f=open('drinks.csv','rU')
f.readline()
f.readline()
f.close()
f=open('drinks.csv','rU')
f.readlines()
f.close()
'''use list comprehension to duplicate readlines without reading the entire 
file at once'''
f=open('drinks.csv','rU')
row for row in f
f.close()
'''use a context manager to automatically close your file'''
with open('drinks.csv','rU') as f:
    [row for row in f]
#split in commas to create a list of lists
with open('drinks.csv','rU') as f:
    [row.split(',') for row in f]
# use the builtin module csv instead
import csv
with open('drinks.csv','rU') as f:
   [row for row in csv.reader(f)]
#use next() to grab the next row
import csv
with open('drinks.csv','rU') as f:
    header=csv.reader(f).next()
    data= [row for row in csv.reader(f)]
    print header
    print data
#write a string to a file
nums=range(5)
with open('nums.txt','wb') as f:
    for num in nums:
        f.write(str(num)+'\n')
#convert a list of lists into a CSV file
import csv
output=[['col1','col2','col3'],['4','5','6']]
with open('examples.csv','wb') as f:
    for row in output:
        csv.writer(f).writerow(row)
#user writerows to do this in one line
with open('example.csv','wb') as f:
    csv.writer(f).writerows(output)
    