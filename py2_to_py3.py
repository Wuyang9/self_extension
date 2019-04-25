# coding = utf-8 
# python 3.6.7 
# Created by wuyang at2019/4/24
"""要和2to3.py文件搭配使用，二者放在一个目录下"""

import os
import time


def py2_to_py3():
    file_location = str(input("请输入py2文件所在文件夹路径："))
    time_start = time.time()
    convert_command = "python3 2to3.py -w "
    for path, dir_list, file_list in os.walk(file_location):
        for length in range(len(file_list)):
            if file_list[length][-3:] == ".py" and file_list[length] != "__init__.py":
                py_convert_command = convert_command + path + "\\" + file_list[length]
                print(py_convert_command)
                os.system(py_convert_command)
    time_end = time.time()
    print("转换完成，耗时：", time_end-time_start, " s")


if __name__ == "__main__":
    py2_to_py3()
