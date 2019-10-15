---
title: pyspark rdd
---

* spark rdd创建方法

~~~python
# 从Python List结构创建RDD
>>> list_data = ['a','b','c','d','e']
>>> list_data
['a', 'b', 'c', 'd', 'e']
>>> rdd_list = sc.parallelize(list_data,2)
>>> type(rdd_list)
<class 'pyspark.rdd.RDD'>

# 从已有的RDD创建，即上面创建的rdd_list基础上进行创建
>>> rdd_map=rdd_list.flatMap(lambda x: x + 'x')
>>> type(rdd_map)
<class 'pyspark.rdd.PipelinedRDD'>        # PipelinedRDD是RDD的子类，所以它包含所有的api
>>> list_map=rdd_map.glom().collect()
>>> list_map
[['a', 'x', 'b', 'x'], ['c', 'x', 'd', 'x', 'e', 'x']]

# 从外部数据源创建RDD
>>> rdd_file=sc.textFile('/home/hadoop/test_data/iris.data')
>>> type(rdd_file)
<class 'pyspark.rdd.RDD'>

~~~

* transformation函数

~~~python

~~~