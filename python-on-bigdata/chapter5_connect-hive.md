

```python
from pyhive import hive
```


```python
connection = hive.Connection(host='hadoop_env.com', port=10000)
```


```python
cursor = connection.cursor()
```


```python
cursor.execute('show databases')     
```


```python
print cursor.fetchall()
```

    [(u'default',), (u'test',)]



```python
cursor.execute("CREATE DATABASE testdb")
```


```python
cursor.execute('show databases')
```


```python
print cursor.fetchall()
```

    [(u'default',), (u'test',), (u'testdb',)]



```python
cursor.execute("USE testdb")
```


```python
cursor.execute('show tables') 
```


```python
cursor.execute("CREATE TABLE iris_data2(sepal_length DOUBLE , sepal_width DOUBLE , petal_length string , petal_width string , species string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' STORED AS TEXTFILE") 
```


```python
cursor.execute('show tables') 
```


```python
print cursor.fetchall()
```

    [(u'iris_data2',)]



```python
cursor.execute("LOAD DATA INPATH '/test_data/iris.data' OVERWRITE INTO TABLE iris_data2")
```


```python
cursor.execute("select * from iris_data2 limit 5")
```


```python
print cursor.fetchall()
```

    [(5.1, 3.5, u'1.4', u'0.2', u'Iris-setosa'), (4.9, 3.0, u'1.4', u'0.2', u'Iris-setosa'), (4.7, 3.2, u'1.3', u'0.2', u'Iris-setosa'), (4.6, 3.1, u'1.5', u'0.2', u'Iris-setosa'), (5.0, 3.6, u'1.4', u'0.2', u'Iris-setosa')]



```python

```
