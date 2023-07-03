# VAScheduleMaker
用以自动填充虚航班表航路的工具
## 工作原理
遍历班表文件以及做好的航路文件，如遇起降机场四码相同，即可进行填充。
## 使用方法
1.准备好班表文件（就是从phpvms导出的班表csv文件）

2.准备好航路文件，格式如下
| Dep | Arr | Route |
| --- | --- | --- |
| ZSAM | ZGGG | NUSPA W597 IKATA A470 SWA X63 SHL |

3.检查无误后，运行脚本
## Feature
添加过滤NAIP航路功能
