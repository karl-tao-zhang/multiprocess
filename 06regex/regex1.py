# regex1.py
import re 
#匹配内容返回迭代对象
# it = re.finditer\
# (r'\d+','2008年是个多事之秋,512地震08奥运等')
# for i in it:
    # print(dir(i))
    # print(i.group())

# obj = re.fullmatch(r'\w+','abcde#f123')
# print(obj)

#匹配字符串开始位置
# obj = re.match('foo','foo,food on the table')
# print(obj.group())

#匹配第一处位置
obj = re.search('foo','Foo,food on the table')
print(obj.group())