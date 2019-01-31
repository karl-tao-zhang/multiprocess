# mongo1.py
from pymongo import MongoClient 
#创建数据库连接
conn  = MongoClient("localhost",27017)
#创建数据库对象
db = conn.stu 
# db = conn['stu']
#创建集合对象
myset = db.class6
#创建索引
# index = myset.ensure_index('name')
# print(index) #索引名称
# #复合索引
# index = myset.ensure_index\
#         ([('name',1),('age',-1)])
# print(index)
#创建其他类型索引
# index = myset.ensure_index('name',unique = True,sparse = True)
# print(index)
#查看当前索引
# for i in myset.list_indexes():
#     print(i)
#删除索引
# myset.drop_index('name_1')    
#myset.drop_indexes()
l = [
    {'$group':{'_id':'$King','num':{'$sum':1}}},
    {'$match':{'num':{'$gt':1}}}
]
cursor = myset.aggregate(l)
for i in cursor:
    print(i)

conn.close()