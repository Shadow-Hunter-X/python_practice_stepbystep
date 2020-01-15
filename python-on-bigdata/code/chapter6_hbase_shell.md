---
title : HBase Shell 命令调用
---

When you start the thrift service ,you need set protocol,like this: ./hbase-daemon.sh start thrift -c compact protocol; In your code,you need set protocol = 'compact',like thie:con = happybase.Connection(host='localhost',port=your thriftport,autoconnect=True,protocol = 'compact',timeout = xxx)


* 开启HBase 

```shell
(base) root@bin# start-hbase.sh 
starting master, logging to /usr/hbase-1.2.2/logs/hbase-root-master-ubuntu.out
Java HotSpot(TM) 64-Bit Server VM warning: ignoring option PermSize=128m; support was removed in 8.0
Java HotSpot(TM) 64-Bit Server VM warning: ignoring option MaxPermSize=128m; support was removed in 8.0
(base) root@bin# hbase shell
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/usr/hbase-1.2.2/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/usr/hadoop-2.7.6/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
HBase Shell; enter 'help<RETURN>' for list of supported commands.
Type "exit<RETURN>" to leave the HBase Shell
Version 1.2.2, r3f671c1ead70d249ea4598f1bbcc5151322b3a13, Fri Jul  1 08:28:55 CDT 2016

hbase(main):001:0> status
1 active master, 0 backup masters, 1 servers, 0 dead, 2.0000 average load

hbase(main):002:0> version
1.2.2, r3f671c1ead70d249ea4598f1bbcc5151322b3a13, Fri Jul  1 08:28:55 CDT 2016

hbase(main):004:0> whoami
root (auth:SIMPLE)
    groups: root

hbase(main):005:0> list
TABLE                                                                                                                                             
0 row(s) in 0.0890 seconds

=> []
```


* 表操作

```shell
hbase(main):005:0> list        1查看目前所有的表，由于目前还没有创建表，所以为结果为空
TABLE                                                                              
0 row(s) in 0.0890 seconds
=> []
hbase(main):006:0> create 'user', 'user name', 'address'  2创建user表两个列族use name和address
0 row(s) in 1.3400 seconds
=> Hbase::Table - user
hbase(main):009:0> describe 'user'     3 查看刚才创建的user表的信息；包含目前表是否禁用；
Table user is ENABLED                 列族名；列族的版本；数据缓存，压缩方法等                                                                                                                    
user                                                                                   
COLUMN FAMILIES DESCRIPTION                                                      
{NAME => 'address', BLOOMFILTER => 'ROW', VERSIONS => '1', IN_MEMORY => 'false', KEEP_DELETED_CELLS => 'FALSE', DATA_BLOCK_ENCODING => 'NONE', TTL
 => 'FOREVER', COMPRESSION => 'NONE', MIN_VERSIONS => '0', BLOCKCACHE => 'true', BLOCKSIZE => '65536', REPLICATION_SCOPE => '0'}                  
{NAME => 'user name', BLOOMFILTER => 'ROW', VERSIONS => '1', IN_MEMORY => 'false', KEEP_DELETED_CELLS => 'FALSE', DATA_BLOCK_ENCODING => 'NONE', T
TL => 'FOREVER', COMPRESSION => 'NONE', MIN_VERSIONS => '0', BLOCKCACHE => 'true', BLOCKSIZE => '65536', REPLICATION_SCOPE => '0'}                
2 row(s) in 0.2130 seconds
hbase(main):010:0> exists 'user'    4 查看user是否存在
Table user does exist                                                                    
0 row(s) in 0.0190 seconds
hbase(main):012:0> is_enabled 'user'   5 查看目前表是否可用
true                                                                                                                                              
0 row(s) in 0.0270 seconds
hbase(main):013:0> disable 'user'      6 禁用表
0 row(s) in 2.3360 seconds
hbase(main):014:0> drop 'user'        7 删除表，删除前先确保表被禁用
0 row(s) in 1.2920 seconds
```

* 数据操作
先修改user中的address列族，让其支持3个版本的数据，然后在进行插入数据

```shell
hbase(main):002:0> alter 'user',{NAME=>'address',VERSIONS=>3}
Updating all regions with the new schema...
1/1 regions updated.
Done.
0 row(s) in 2.1440 seconds
构造的测试数据如下，将下列的语句在HBase Shell执行
put 'user' , '1' , 'user name:first_name' , 'mike'
put 'user' , '1' , 'user name:last_name' , 'lee'
put 'user' , '1' , 'address:city' , 'BeiJin'
put 'user' , '1' , 'address:region' , '海淀区'
put 'user' , '1' , 'address:city' , 'ShangHai'
put 'user' , '1' , 'address:region' , '闵行区'
put 'user' , '2' , 'user name:first_name' , 'lily'
put 'user' , '2' , 'user name:last_name' , 'wang'
put 'user' , '2' , 'address:city' , 'ShangHai'
put 'user' , '2' , 'address:region' , '徐汇区'
put 'user' , '2' , 'address:city' , 'GuangZhou'
put 'user' , '2' , 'address:region' , '越秀区'
put 'user' , '3' , 'user name:first_name' , 'petter'
put 'user' , '3' , 'user name:last_name' , 'lee'
put 'user' , '3' , 'address:city' , 'GuangZhou'
put 'user' , '3' , 'address:region' , '天河区'
put 'user' , '3' , 'address:city' , 'ShenZhen'
put 'user' , '3' , 'address:region' , '南山区'
put 'user' , '4' , 'user name:first_name' , 'bill'
put 'user' , '4' , 'user name:last_name' , 'lan'
put 'user' , '4' , 'address:city' , 'ShenZhen'
put 'user' , '4' , 'address:region' , '福田区'
put 'user' , '4' , 'address:city' , 'BeiJin'
put 'user' , '4' , 'address:region' , '朝阳区'

hbase(main):096:0> get 'user' , '1' , 'address'    
COLUMN                                CELL
 address:city		 timestamp=1569158776506, value=ShangHai
 address:regison    timestamp=1569158776541, value=\xE9\x97\xB5\xE8\xA1\x8C\xE5\x8C\xBA
2 row(s) in 0.0120 seconds
hbase(main):033:0> get 'user' , '1' , {COLUMNS=>['address:city','address:region'],VERSIONS=>2}
COLUMN                                CELL                                      
 address:city                         timestamp=1569163076365, value=ShangHai      
 address:city                         timestamp=1569163076242, value=BeiJin         
 address:region                       timestamp=1569163076399, value=\xE9\x97\xB5\xE8\xA1\x8C\xE5\x8C\xBA                                         
 address:region                       timestamp=1569163076301, value=\xE6\xB5\xB7\xE6\xB7\x80\xE5\x8C\xBA                                         
4 row(s) in 0.0720 seconds

hbase(main):036:0> scan 'user',{COLUMNS=>['address:city','address:region']} 获取address列簇数据
ROW   COLUMN+CELL                                                           
 1    column=address:city, timestamp=1569163076365, value=ShangHai                
 1    column=address:region, timestamp=1569163076399, value=\xE9\...                
 2    column=address:city, timestamp=1569163076655, value=GuangZhou               
 2    column=address:region, timestamp=1569163076716, value=\xE8\...                 
 3    column=address:city, timestamp=1569163076948, value=ShenZhen                
 3    column=address:region, timestamp=1569163077004, value=\xE5\...                 
 4    column=address:city, timestamp=1569163077252, value=BeiJin                    
 4    column=address:region, timestamp=1569163078434, value=\xE6\...                 
4 row(s) in 0.0380 seconds
hbase(main):035:0> get 'user' , '1'     获取第一行的数据
COLUMN                        CELL                                   
 address:city                 timestamp=1569163076365, value=ShangHai   
 address:region               timestamp=1569163076399, value=\xE9\x97\... 
 user name:first_name         timestamp=1569163075969, value=mike      
 user name:last_name         timestamp=1569163076184, value=lee 

hbase(main):002:0> deleteall 'user' , '1'     1 删除整行数据
0 row(s) in 0.1910 seconds
hbase(main):004:0> count 'user'           2 删除后查看，统计行数发现只有3行
3 row(s) in 0.0540 seconds
=> 3
hbase(main):008:0> delete  'user','2','address:region'
0 row(s) in 0.0070 seconds
hbase(main):009:0> scan 'user'          3 查看删除后的第2行数据
ROW      COLUMN+CELL                                                         
 2       column=address:city, timestamp=1569163076655, value=GuangZhou            
 2       column=user name:first_name, timestamp=1569163076467, value=lily            
 2       column=user name:last_name, timestamp=1569163076517, value=wang  
```