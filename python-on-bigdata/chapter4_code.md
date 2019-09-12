
from snakebite.client import Client     # 


```python
client = Client("hadoop_env.com", 9000, use_trash=False)  #
```


```python
ls_files=client.ls(['/test_data'])  #
```


```python
for x in ls_files:
    print x
```

    {'group': u'supergroup', 'permission': 420, 'file_type': 'f', 'access_time': 1568194427743L, 'block_replication': 1, 'modification_time': 1568194428062L, 'length': 4551L, 'blocksize': 134217728L, 'owner': u'root', 'path': '/test_data/iris.data'}
    {'group': u'supergroup', 'permission': 420, 'file_type': 'f', 'access_time': 1568194133530L, 'block_replication': 1, 'modification_time': 1568194134713L, 'length': 197979L, 'blocksize': 134217728L, 'owner': u'root', 'path': '/test_data/links.csv'}
    {'group': u'supergroup', 'permission': 420, 'file_type': 'f', 'access_time': 1568194134753L, 'block_replication': 1, 'modification_time': 1568194134812L, 'length': 494431L, 'blocksize': 134217728L, 'owner': u'root', 'path': '/test_data/movies.csv'}
    {'group': u'supergroup', 'permission': 420, 'file_type': 'f', 'access_time': 1568194134825L, 'block_replication': 1, 'modification_time': 1568194134927L, 'length': 2483723L, 'blocksize': 134217728L, 'owner': u'root', 'path': '/test_data/ratings.csv'}
    {'group': u'supergroup', 'permission': 420, 'file_type': 'f', 'access_time': 1568194134936L, 'block_replication': 1, 'modification_time': 1568194134965L, 'length': 118660L, 'blocksize': 134217728L, 'owner': u'root', 'path': '/test_data/tags.csv'}
    {'group': u'supergroup', 'permission': 420, 'file_type': 'f', 'access_time': 1567143893408L, 'block_replication': 1, 'modification_time': 1567143893602L, 'length': 3715L, 'blocksize': 134217728L, 'owner': u'root', 'path': '/test_data/test.csv'}



```python
list(client.count(['/']))    #
```




    [{'directoryCount': 12L,
      'fileCount': 7L,
      'length': 3306717L,
      'path': '/',
      'quota': 9223372036854775807L,
      'spaceConsumed': 3306717L,
      'spaceQuota': 18446744073709551615L}]




```python
mkdirs=client.mkdir(['/temp_data','/201909'],create_parent=True)
```


```python
list(mkdirs)
```




    [{'path': '/temp_data', 'result': True}, {'path': '/201909', 'result': True}]




```python
rmdir_res=client.rmdir(['/temp_data'])
```


```python
list(rmdir_res)
```




    [{'path': '/temp_data', 'result': True}]




```python
delete_files=client.delete(['/test_data/temp.py'])
```


```python
list(delete_files)
```




    [{'path': '/test_data/temp.py', 'result': True}]




```python
client.df()
```




    {'capacity': 41083600896L,
     'corrupt_blocks': 0L,
     'filesystem': 'hdfs://hadoop_env.com:9000',
     'missing_blocks': 0L,
     'remaining': 26666823680L,
     'under_replicated': 0L,
     'used': 3439893L}




```python
client.stat(['/test_data'])
```




    {'access_time': 0L,
     'block_replication': 0,
     'blocksize': 0L,
     'file_type': 'd',
     'group': u'supergroup',
     'length': 0L,
     'modification_time': 1568197308654L,
     'owner': u'root',
     'path': '/test_data',
     'permission': 493}




```python
client.test('/201909')
```




    True




```python
du_info=client.du(['/test_data'])
```


```python
list(du_info)
```




    [{'length': 4365L, 'path': '/test_data/func.py'},
     {'length': 4551L, 'path': '/test_data/iris.data'},
     {'length': 197979L, 'path': '/test_data/links.csv'},
     {'length': 494431L, 'path': '/test_data/movies.csv'},
     {'length': 2483723L, 'path': '/test_data/ratings.csv'},
     {'length': 12099L, 'path': '/test_data/result.txt'},
     {'length': 118660L, 'path': '/test_data/tags.csv'},
     {'length': 3715L, 'path': '/test_data/test.csv'}]




```python
copy_res=client.copyToLocal(['/test_data/func.py'],'/home/hadoop/func_copy.py',check_crc=True)
```


```python
list(copy_res)
```




    [{'error': '',
      'path': '/home/hadoop/func_copy.py',
      'result': True,
      'source_path': '/test_data/func.py'}]




```python

```
