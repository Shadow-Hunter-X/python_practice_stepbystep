PS E:\spark-2.4.2-bin-hadoop2.7\bin> .\spark-shell2.cmd
19/10/09 10:48:18 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://Yct201811021847:4040
Spark context available as 'sc' (master = local[*], app id = local-1570589309789).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.4.2
      /_/

Using Scala version 2.12.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_191)
Type in expressions to have them evaluated.
Type :help for more information.

scala> val num = Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
num: Array[Int] = Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

scala> val data=sc.textFile("D:/spark.txt")
data: org.apache.spark.rdd.RDD[String] = D:/spark.txt MapPartitionsRDD[1] at textFile at <console>:24

scala> val newRDD = no.map(num => (num * 2))
newRDD: Array[Int] = Array(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

scala> data.count()
res0: Long = 1627

scala> val contextdata = data.filter(line => line.contains("sparkcontext"))
contextdata: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[2] at filter at <console>:25

scala> data.filter(line => line.contains("TaskContext")).count()
res5: Long = 12

scala> data.first()
res7: String = nextprevious |PySpark 2.4.4 documentation ?

scala> data.take(5)
res8: Array[String] = Array(nextprevious |PySpark 2.4.4 documentation ?, pyspark package, Subpackages, pyspark.sql module, pyspark.streaming module)

scala>  data.partitions.length    
res9: Int = 2

scala>  data.cache()
res10: data.type = D:/spark.txt MapPartitionsRDD[1] at textFile at <console>:24

-----------------------------------------------------------------------------------------------------------------------------------------

(base) root@hadoop# pyspark
Python 2.7.16 |Anaconda, Inc.| (default, Mar 14 2019, 21:00:58) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
19/10/09 01:21:07 WARN Utils: Your hostname, ubuntu resolves to a loopback address: 127.0.1.1; using 192.168.223.130 instead (on interface eth0)
19/10/09 01:21:07 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
19/10/09 01:21:08 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.3
      /_/

Using Python version 2.7.16 (default, Mar 14 2019 21:00:58)
SparkSession available as 'spark'.
>>> sc.parallelize([0, 2, 3, 4, 6], 5).glom().collect()
[[0], [2], [3], [4], [6]] 

>>> sc.parallelize(xrange(0, 6, 2), 5).glom().collect()
[[], [0], [], [2], [4]]

>>> path = os.path.join("/home/hadoop/test_data", "iris.data")  
>>> textFile = sc.textFile(path)  # 读取文件内容
>>> textFile.collect()
[u'5.1,3.5,1.4,0.2,Iris-setosa', u'4.9,3.0,1.4,0.2,Iris-setosa', ……..]

>>> dirPath = os.path.join("/home/hadoop/", "files")
>>> os.mkdir(dirPath)                # 创建文件夹
>>> with open(os.path.join(dirPath, "1.txt"), "w") as file1:
...     _ = file1.write("1")         # 创建文件，写入数据
... 
>>> with open(os.path.join(dirPath, "2.txt"), "w") as file2:
...     _ = file2.write("2")         # 创建文件，写入数据
... 
>>> textFiles = sc.wholeTextFiles(dirPath)    # 读取刚才穿件的文件夹中的文件内容
>>> sorted(textFiles.collect())
[(u'file:/home/hadoop/files/1.txt', u'1'), (u'file:/home/hadoop/files/2.txt', u'2')]

>>> df=spark.read.csv('/home/hadoop/test_data/movies.csv',header=True, inferSchema=True)
>>> df.show(10)
+-------+--------------------+--------------------+
|movieId|               title|              genres|
+-------+--------------------+--------------------+
|      1|    Toy Story (1995)|Adventure|Animati...|
|      2|      Jumanji (1995)|Adventure|Childre...|
|      3|Grumpier Old Men ...|      Comedy|Romance|
|      4|Waiting to Exhale...|Comedy|Drama|Romance|
|      5|Father of the Bri...|              Comedy|
|      6|         Heat (1995)|Action|Crime|Thri...|
|      7|      Sabrina (1995)|      Comedy|Romance|
|      8| Tom and Huck (1995)|  Adventure|Children|
|      9| Sudden Death (1995)|              Action|
|     10|    GoldenEye (1995)|Action|Adventure|...|
+-------+--------------------+--------------------+
only showing top 10 rows


