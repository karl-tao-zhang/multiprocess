import re 
obj = re.compile(r'(?P<dog>de)fg(?P<pig>hi)')
match_obj = obj.search('abcdefghijklmn')

print('flags:',obj.flags) #标志位常亮
print('pattern:',obj.pattern) #正则表达式
print('groupindex:',obj.groupindex) #捕获组字典
print('groups:',obj.groups) #子组个数

#pos   目标字符串起始位置
print(match_obj.pos)
#endpos　目标字符串结束位置
print(match_obj.endpos)

#re
print(match_obj.re)

#string
print(match_obj.string)

#lastgroup
print(match_obj.lastgroup)
#lastindex
print(match_obj.lastindex)
print('***********')

print(match_obj.start())
print(match_obj.end())

print(match_obj.span())
print(match_obj.group()) #匹配正则表达式整体内容
print(match_obj.group(1)) #匹配某个子组内容

print(match_obj.groups())
print(match_obj.groupdict())
