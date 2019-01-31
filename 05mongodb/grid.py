# grid.py
from pymongo import MongoClient 
import gridfs 

conn = MongoClient('localhost',27017)
db = conn.gird 

#通过GridFS 获取集合对象
#fs即为存储大文件对象
fs = gridfs.GridFS(db)

#通过查找获取游标
cursor = fs.find()

for file in cursor:
    if file.filename =='abc.mp4':
        with open(file.filename,'wb') as f:
            while True:
                #可以通过file.read从数据库获取文件内容
                data = file.read(4096)
                if not data:
                    break 
                f.write(data)
conn.close()