# mongo.py
from pymongo import MongoClient 
#创建数据库连接
conn  = MongoClient("localhost",27017)
#创建数据库对象
db = conn.stu 
# db = conn['stu']
#创建集合对象
myset = db.class6
# myset = db.['class']

# print(dir(myset))
#插入操作
# myset.insert({'name':'张铁林','King':'乾隆'})
# myset.insert([{'name':'张国立','King':'康熙'},\
#                 {'name':'陈道明','King':'乾隆'}])
# myset.insert_many([{'name':'唐国强','King':'雍正'},\
#                     {'name':'陈建斌','King':'雍正'}])
# myset.insert_one({'name':'郑少秋','King':'乾隆'})
# myset.save({'_id':1,'name':'吴奇隆','King':'雍正'})
# cursor = myset.find({'age':{'$gt':20}},{'_id':0})
# for i in cursor:
#     print(i)
# print(cursor.next())
# print(cursor.count())
# print(cursor.limit(2))
# print(cursor.skip(2))
# for i in cursor.sort([('age',1),('name',-1)]):
#     print(i)
# dic = {'$or':[{'age':{'$gt':16}},{'sex':'w'}]}
# data = myset.find_one(dic,{'_id':0})
# print(data)
# myset.update({'name':'张国立'},{'$set':{'name':'国立'}})
# myset.update({'name':'冰冰'},{'$set':{'King':'武则天'}},upsert = True)
# myset.update({'King':'乾隆'},{'$set':{'King_name':'弘历'}},multi = True)
# myset.remove({'name':''})
# print(myset.find_one_and_delete({'name':'吴奇隆'}))




conn.close()