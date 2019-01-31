import re 

f = open('abc.txt')
l = []
pattern = r'\b[A-Z][\._0-9a-zA-Z]*|[0-9]+'

for line in f:
    l += re.findall(pattern,line)
print(l)
f.close()

# b = open('abc.txt')
# c = []
# pattern = r'[0-9]+'
# for a in b :
#     c += re.findall(pattern,a)
# print(c)

# f.close()