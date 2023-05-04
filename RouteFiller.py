# 定义相关csv位置
import csv
import os
SchedulePath=input("请输入班表csv地址：")
RoutePath=input("请输入航路表csv地址：")
# 遍历班表的起降机场 
with open(os.path.join(SchedulePath)) as csvfile:
    ARPT = csv.reader(csvfile, delimiter=' ', )


# → 遍历一号航路的起降机场 → if班表的起降机场=航路起降机场，则填充 → else 留空
