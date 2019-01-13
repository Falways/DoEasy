#!/usr/bin/python3

# python声明变量不需要指定类型
import codecs
file = open('test.txt')
list = []
while 1:
    line = file.readline()
    if not line:
        break
    else:
        list.append(line)

for i in list:
    print("序号：%s,的值为：%s"%(list.index(i)+1,i))

# 写文件
dict = {'username':'falways','age':'22','sex':'男'}
f = codecs.open('./writefile.txt','w',"utf-8-sig")
f.write(str(dict))
f.close()