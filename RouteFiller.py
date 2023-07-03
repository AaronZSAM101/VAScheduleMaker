# 定义相关csv位置
import os
import pandas as pd
SchedulePath=input("请输入要填充的班表csv地址:")
RoutePath=input("请输入航路表csv地址:")
# 读取Schedules.csv文件、Route.csv文件
schedules_df = pd.read_csv(SchedulePath)
route_df = pd.read_csv(RoutePath)
# 遍历班表的每一行
for index, row in schedules_df.iterrows():
    depicao = row['depicao']
    arricao = row['arricao']
    ## 在Route.csv文件中查找匹配的dep和arr
    route_match = route_df[(route_df['Dep'] == depicao) & (route_df['Arr'] == arricao)]['Route'].values
    ## 如果找到匹配项，则将对应的Route填充到Schedules.csv的相应行的route列中
    if len(route_match) > 0:
        schedules_df.at[index, 'route'] = route_match[0]
exportPath=input('班表填充完成，请输入保存路径:')
# 将更新后的Schedules.csv文件保存
schedules_df.to_csv(os.path.join(exportPath, 'Schedules_updated.csv'), index=False)
input('班表航路填充完成！')