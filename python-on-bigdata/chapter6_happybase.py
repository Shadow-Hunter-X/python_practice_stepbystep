import happybase
connection = happybase.Connection(host='hadoop_env.com',port=9090,timeout=1000000)
#conn = happybase.Connection(host=host,port=port,protocol='compact',transport='framed')
connection.open()
print connection.tables()
user = connection.table('user')
user_families=user.families()

regions=user.regions()

row_1=user.row('1')      # 获取第一行的数据 

rows_1=user.rows(['2','3','4'])    # 获取好多列

cells=user.cells('1','address:city')     # 

sanner=user.scan()
for key , data in sanner:
	print key , data 
	
user.put('5',{'user name:first_name':'kate','user name:last_name':'jane','address:city':'chengdu','address:region':'tianfu'})

user.delete('5')	
	
batch=user.batch()
batch.put('5',{'user name:first_name':'kate','user name:last_name':'jane',
               'address:city':'chengdu','address:region':'tianfu'})
batch.delete('5')
batch.send()


#---------------------------------------------------------------------#

由于在使用HappyBase和HBase进行通信时，使用的是thrift进行通信的，所以需要保持二者协议参数一致，
在代码中连接HBase时的协议配置参数要和hbase-daemon.sh命令中的参数一致否则就会出现TTransportException(type=4, message='TSocket read 0 bytes')这样的错误，默认情况下
由于Connection构造函数中大多数参数使用默认值，但是如果使用其他的配置参数，需要注意。数据使用在第3章说明的movie数据进行插入。


import happybase      				# 导入HappyBase库  

connection = happybase.Connection(host='hadoop_env.com',port=9090 ,timeout=100000 , protocol='compact')  	#连接Hbase
# connection.open()   由于在Connection中的 autoconnect=True 默认是直连的，所以可以不使用open函数

tables_list = connection.tables()   # 获取所有的表

families = {
'movieId':dict(),
'title':dict(max_versions=3),
'genres':dict()
}

connection.create_table('movie' , families )   # 创建movie表，包含3个列族

movie = connection.table('movie')   # 获取movie表对象

# 完表中插入数据
movie.put('1',{'movieId:Id':'1','title:name':'Toy Story (1995)','genres:name':'Adventure|Animation|Children|Comedy|Fantasy'})
movie.put('2',{'movieId:Id':'2','title:name':'Jumanji (1995)','genres:name':'Adventure|Children|Fantasy'})
movie.put('3',{'movieId:Id':'3','title:name':'Grumpier Old Men (1995)','genres:name':'Comedy|Romance'})
movie.put('4',{'movieId:Id':'4','title:name':'Waiting to Exhale (1995)','genres:name':'Comedy|Drama|Romance'})
movie.put('5',{'movieId:Id':'5','title:name':'Father of the Bride Part II (1995)','genres:name':'Comedy'})
movie.put('6',{'movieId:Id':'6','title:name':'Heat (1995)','genres:name':'Action|Crime|Thriller'})
movie.put('7',{'movieId:Id':'7','title:name':'Sabrina (1995)','genres:name':'Comedy|Romance'})
movie.put('8',{'movieId:Id':'8','title:name':'Tom and Huck (1995)','genres:name':'Adventure|Children'})

scaner=movie.scan()

for key, data in scaner:
    print key, data

# -------------------------------------------------------------------#

import happybase

connection = happybase.Connection(host='hadoop_env.com',port=9090 ,timeout=100000 , autoconnect=False , protocol='compact')
connection.open()
movie=connection.table('movie')
batch=movie.batch()

batch.put('9',{'movieId:Id':'9','title:name':'xx','genres:name':'xx'})
batch.put('10',{'movieId:Id':'10','title:name':'xx','genres:name':'xx'})
batch.put('11',{'movieId:Id':'11','title:name':'xx','genres:name':'xx'})
batch.put('12',{'movieId:Id':'12','title:name':'xx','genres:name':'xx'})
new_rows=movie.rows(['9','10','11','12'])
batch.delete('9',{'title:name','genres:name'})
batch.delete('10',{'title:name','genres:name'})
batch.delete('11',{'title:name','genres:name'})
batch.delete('12',{'title:name','genres:name'})
batch.send

scaner=movie.scan()

for key, data in scaner:
    print key, data
	
connection.disable_table('movie')
connection.close()


# -----------------------------------------------------------------#
# 使用连接池

import happybase
import thread
import time


def user_table():
	with pool.connection() as connection:
		user=connection.table('user')
		scaner=user.scan()
		for key, data in scaner:
			print key, data
	
def user_table():
	with pool.connection() as connection:
		connection.enable_table('movie')
		movie=connection.table('movie')
		scaner=movie.scan()
		for key, data in scaner:
			print key, data

pool = happybase.ConnectionPool(size=3, host='hadoop_env.com', table_prefix='pool_test')

try:
   thread.start_new_thread( user_table )
   thread.start_new_thread( movie_table )
except:
   print "Error: 无法开启线程"












