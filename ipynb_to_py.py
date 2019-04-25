# coding = utf-8 
# python 3.6.7 
# Created by wuyang at2019/2/22

"""
    版本0.0：将格式为.ipynb文件批量转换为.py文件
    版本0.1：当转换为.txt文件时，再修改其扩展名为.py文件
    命令行指令：jupyter nbconvert --to script *.ipynb
"""

import os
import time

file_location = str(input("请输入ipynb文件所在文件夹路径："))
time_start = time.time()
convert_command = "jupyter nbconvert --to script "
for path, dir_list, file_list in os.walk(file_location):
    for length in range(len(file_list)):
        if file_list[length][-5:] == "ipynb":
            py_convert_command = convert_command + path + "\\" + file_list[length]
            print(file_list[length])
            os.system(py_convert_command)

            # 若转换后的文件扩展名为txt，则直接转换修改
            if file_list[length][:-6]+".txt" in os.listdir(path):
                try:
                    if not os.path.exists(path + "\\" + file_list[length][:-6] + ".py"):
                        os.rename(path+"\\"+file_list[length][:-6]+".txt", path+"\\"+file_list[length][:-6]+".py")
                except:
                    pass

time_end = time.time()
print("转换完成，耗时：", time_end-time_start, " s")

# F:\Windows10\Desktop\ab
