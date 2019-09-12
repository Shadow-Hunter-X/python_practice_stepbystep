

```python
from pyspark import SparkContext     # 
```


```python
from pyspark.sql import SparkSession  #
```


```python
spark=SparkSession.builder.appName('my_app_name').getOrCreate()
```


```python
df=spark.read.csv('movies.csv',header=True, inferSchema=True)
```


```python
df.createOrReplaceTempView("movie")  
```


```python
spark.sql("SELECT * FROM movie limit 5").show() 
```

    +-------+--------------------+--------------------+
    |movieId|               title|              genres|
    +-------+--------------------+--------------------+
    |      1|    Toy Story (1995)|Adventure|Animati...|
    |      2|      Jumanji (1995)|Adventure|Childre...|
    |      3|Grumpier Old Men ...|      Comedy|Romance|
    |      4|Waiting to Exhale...|Comedy|Drama|Romance|
    |      5|Father of the Bri...|              Comedy|
    +-------+--------------------+--------------------+
    



```python

```
