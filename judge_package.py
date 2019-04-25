# coding = utf-8 
# python 3.6.7 
# Created by wuyang at2019/2/26

"""
判断某个包是否已安装
"""
import os
cmd = str(input("输入命令行指令："))
package_text = os.popen(cmd).read()
print(package_text)
package_text = package_text.lower()


def judgePackage(package_text, package_name=str):
    if package_name in package_text:
        print("exist !")
    else:
        print("not exist !")


while 1:
    package_name = str(input("输入完整包名："))
    judgePackage(package_text, package_name)



