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

* 示例
~~~python
>>> seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
>>> combOp = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
>>> aggre_data=sc.parallelize([1, 2, 3, 4]).aggregate((0, 0), seqOp, combOp)
>>> type(aggre_data)
<type 'tuple'>
>>> aggre_data
(10, 4)

>>> data = sc.parallelize([(1,3),(1,2),(1,4),(2,3)]) 
>>> def seq(a,b):
...     return max(a,b)
…
>>def combine(a,b):
...     return a+b
...
>>data.aggregateByKey(3,seq,combine,4).collect()
[(1, 10), (2, 3)]

>>> data.cache()      # 调用cache
ParallelCollectionRDD[15] at parallelize at PythonRDD.scala:195

>>> sc.parallelize([1, 2, 3, 4, 5], 3).glom().collect()
[[1], [2, 3], [4, 5]]
>>> sc.parallelize([1, 2, 3, 4, 5], 3).coalesce(1).glom().collect()    # 减少为只有1个
[[1, 2, 3, 4, 5]]

>>> x = sc.parallelize([("a", 1), ("b", 4)])
>>> y = sc.parallelize([("a", 2)])
>>> [(x, tuple(map(list, y))) for x, y in sorted(list(x.cogroup(y).collect()))]
[('a', ([1], [2])), ('b', ([4], []))]

>>> sc.parallelize([(1,3),(1,2),(1,4),(2,3)]).collect()
[(1, 3), (1, 2), (1, 4), (2, 3)]

>>> m = sc.parallelize([(1, 2), (3, 4)]).collectAsMap()
>>> m[1] , m[3]
(2, 4)

>>> data.count()
4

>>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
>>> rdd.countByKey()
defaultdict(<type 'int'>, {'a': 2, 'b': 1})

>>> sc.parallelize([1, 1, 2, 3]).distinct().collect()
[2, 1, 3]

>>> rdd = sc.parallelize([1, 2, 3, 4, 5])
>>> data1=rdd.filter(lambda x: x % 2 == 0)
>>> type(data1)
<class 'pyspark.rdd.PipelinedRDD'>

>>> data2=rdd.flatMap(lambda x: range(1, x))
>>> type(data2)
<class 'pyspark.rdd.PipelinedRDD'>
>>> data2.collect()
[1, 1, 2, 1, 2, 3]
>>> data2=sc.parallelize([(1,2),(3,4),(5,6),(7,8)]).flatMap(lambda x: x)
>>> type(data2)
<class 'pyspark.rdd.PipelinedRDD'>
>>> data2.collect()
[1, 2, 3, 4, 5, 6, 7, 8]

>>> x = sc.parallelize([("a", ["x", "y", "z"]), ("b", ["p", "r"])])
>>> def f(x): return x
…
>>> data3=x.flatMapValues(f)
>>> type(data3)
<class 'pyspark.rdd.PipelinedRDD'>
>>> data3.collect()
[('a', 'x'), ('a', 'y'), ('a', 'z'), ('b', 'p'), ('b', 'r')]


~~~


* 

~~~python

~~~