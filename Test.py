'''
import dataType


price = 0
price1 = 00
tmp = dataType.PriceData()
print(dataType.PriceData.dataCompare(tmp, price, price1) )

'''
from Utils.IOUtils import FileReader

account = "12341231234567"

fr = FileReader()
userData = FileReader.read_one_users(account)
print(userData['name'])