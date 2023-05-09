# 定义相关csv位置
import csv
import os
SchedulePath=input("请输入要填充的班表csv地址：")
RoutePath=input("请输入航路表csv地址：")
# 遍历班表的起降机场 
with open(os.path.join(SchedulePath), encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print(headers)
    for row in reader:
        print(row)
# → 遍历一号航路的起降机场
with open(os.path.join(RoutePath), encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print(headers)
    for row in reader:
        print(row)
#  → if班表的起降机场=航路起降机场，则填充 → else 留空
