from prettytable import PrettyTable
from ganzhiwuxin import *
from shipan import *

所有天盘=[]
for i in range(1, 13):
    a = 天盘(支(i), 支(1))
    所有天盘.append(a)

所有甲子 = []
for i in range(1, 11):
    for j in range(1, 13):
        if 阴阳相同(干(i), 支(j)):
            所有甲子.append(干支(干(i), 支(j)))

所有栻盘 = []
for i in 所有天盘:
    for j in 所有甲子:
        所有栻盘.append(栻盘(i, j))

result = []
for i in 所有栻盘:
    sike = i['四课']
    gan = sike['干']
    ganyanshen = sike['干阳神']
    zhi = sike['支']
    zhiyanshen = sike['支阳神']

    if 六合(寄宫(gan), zhi) and 六合(ganyanshen, zhiyanshen):
        result.append(i)

print("上下皆合格式共{0}格".format(len(result)))
x = PrettyTable()

x.header = False
x.padding_width = 2
x.border = 0

x.add_row(result[0:5])
x.add_row(['', '', '', '', ''])
x.add_row(['', '', '', '', ''])
x.add_row(result[5:10])
print(x)
