# 作者 Mr.Peng
# 更新日期：2022年4月30日
# 将"@"替换成相应的值

import requests
import time

print('自动登录校园网工具')
# 变量
admin = "@"  # 账号（学号）
upass = "@"  # 密码
R3 = "@"  # 0校园网 1电信 2联通 3移动
# 合成变量前标签
dd = '&DDDDD=' + admin
passa = '&upass=' + upass
r3 = '&R3=' + R3
# 常量
key = '&0MKKey=123456'
r1 = '&R1=0'
r6 = '&R6=0'
para = '&para=00'
v6 = '&v6ip=%20_:%201651145882541'
url = '@' # 根据各个学校校园网的不同来更换url，详情看文档
print("等待4秒，以免缓存出错")
time.sleep(4)  # 休眠四秒，以免Buffer Error
print("正在登录...")
# 执行登录操作
uurl = url + dd + passa + key + r1 + r3 + r6 + para + v6
durl = dd + r1 + r3 + r6 + para + v6
print('完成请求，获得链接数据（数据仅供BUG调试）：\n' + durl)  # 输出变量+常量
print("\n")
do = requests.get(url=uurl)
print("当前状态" + do.text)  # 输出认证服务器的Refer信息
print("\n")
print("完成！10秒后窗口关闭!")
time.sleep(10)
