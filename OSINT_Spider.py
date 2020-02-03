# -*- coding:utf-8 -*-

import os
import re
import pypinyin

pyname = os.path.basename(__file__) #获取脚本名
filedir = os.path.abspath('.') # 获取当前目录
filenames=os.listdir(filedir)
all_in_one = []

out_put = open(filedir + '\\output.txt' , 'a+')
for filename in filenames:
    if filename != pyname:
        filepath = filedir + '\\' + filename
        username = []
        for line in open(filepath, encoding='utf-8', errors='ignore'):
            if '"fn"' in line:
                line = re.sub("[A-Za-z0-9\,\"\:\ \(\)\.\\n]", "", line)
                #print(line)
                str = ''
                # 不带声调的(style=pypinyin.NORMAL)
                for i in pypinyin.pinyin(line, style=pypinyin.NORMAL):
                    str += ''.join(i)
                    out_put.write(str + '\n')
out_put.close()

