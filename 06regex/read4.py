import sys 
import re

def getAddress(port):
    pattern = (r'\S+')
    f = open('1.txt','r')

    while True:
        data = ''
        for line in f :
            if line != '\n':
                data += line 
            else:
                break
        #表示文档结束
        if not data:
            break
        PORT = re.match(pattern,data).group()
        #确认对应段
        if port == PORT:
            pattern = r'address\s+is\s+(\w{4}.\w{4}.\w{4})'
            addr = re.search(pattern,data).group(1)
            return addr 
        else:
            continue

    # return addr 

if __name__ == '__main__':
    port = sys.argv[1]
    print(getAddress(port))
