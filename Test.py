

from dataType import NameData
from dataType import PriceData
from dataType import TimeData
from dataType import DateData
from dataType import PasswordData
from dataType import BankAccountData
from random import random
'''
A = input()
B = input()
td = TimeData()
pd = PriceData()
'''
#NameData
#print(NameData.dataConfirm(A))
#print(PriceData.dataConfirm(A))
'''
print(TimeData.dataConfirm(A))
print(TimeData.dataToBasicType(A))
print(len(A))
print(TimeData.dataConfirm(B))
print(TimeData.dataToBasicType(B))
print(len(B))
print(TimeData.dataCompare(td, A, B))
'''
'''
print(PriceData.dataConfirm(A))
print(PriceData.dataConfirm(B))
print(PriceData.dataCompare(td, A, B))

x = "2020-01-01"
print(x[:4])
'''
'''
data = "20201231"
year = data[:4]
month = data[4:6]
day = data[6:]
print(year)
print(month)
print(day)

data = "200102"
year = int(data[:2])
month = data[2:4]
day = data[4:]

print(year)
print(month)
print(day)
'''

'''
A = input()
print(DateData.dataConfirm(A))
print(DateData.dataToBasicType(A))
'''

'''
A = input()
print(PasswordData.dataConfirm(A))
print(PasswordData.dataToBasicType(A))
'''
'''
data = "1234.123.1234567"
print(data[:4] + data[5:8] + data[9:])
'''
'''
#A = input()
A = "1234.123.1234567"
print(len(A))
print(BankAccountData.dataConfirm(A))
print(BankAccountData.dataToBasicType(A))
'''



result = ""
for i in range(14) :
    num = random()
    num = int(num * 10)
    num = str(num)
    
    result = result + num
    num = int(num) % 5
    print(num)

print(result)

num = random()
num = int(num * 10)
num = num % 5
print(num)