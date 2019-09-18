import sys
import string
import hashlib

while True:
    line = sys.stdin.readline()
    if not line:
        break

    line = string.strip(line, "\n ")
    sepal_length  , sepal_width  , petal_length  , petal_width  , species  = string.split(line, "\t")
    connect_value = sepal_length + ' ' + sepal_width + ' ' + petal_length + ' ' + petal_width
    print "\t".join([hashlib.md5(connect_value).hexdigest(),species])
	
"""	
add file /root/chapter5.py;
SELECT TRANSFORM (sepal_length  , sepal_width  , petal_length  , petal_width  , species)
    USING 'python chapter5.py' AS
    (connect_value string , species string)
FROM iris_data LIMIT 5;


CREATE TABLE iris_data(sepal_length string , sepal_width string , petal_length string , petal_width string , species string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;


LOAD DATA LOCAL INPATH '/root/iris.data' OVERWRITE INTO TABLE iris_data


hive (default)> use testdb;
OK
Time taken: 2.184 seconds
hive (testdb)> CREATE TABLE iris_data(sepal_length string , sepal_width string , petal_length string , petal_width string , species string)
             > ROW FORMAT DELIMITED
             > FIELDS TERMINATED BY ','
             > LINES TERMINATED BY '\n'
             > STORED AS TEXTFILE;
OK
Time taken: 1.0 seconds
hive (testdb)> LOAD DATA LOCAL INPATH '/root/iris.data' OVERWRITE INTO TABLE iris_data;
Loading data to table testdb.iris_data
Table testdb.iris_data stats: [numFiles=1, numRows=0, totalSize=4702, rawDataSize=0]
OK
Time taken: 1.249 seconds
hive (testdb)> select * from iris_data limit 2;
OK
5.1     3.5     1.4     0.2     Iris-setosa
4.9     3.0     1.4     0.2     Iris-setosa
Time taken: 0.543 seconds, Fetched: 2 row(s)
hive (testdb)>

---

hive (testdb)> add file /root/chapter5.py;
Added resources: [/root/chapter5.py]
hive (testdb)> SELECT TRANSFORM (sepal_length  , sepal_width  , petal_length  , petal_width  , species)
             >     USING 'python chapter5.py' AS
             >     (connect_value string , species string)
             > FROM iris_data LIMIT 5;
Query ID = root_20190917222727_c067f91c-c1a1-4a8c-b9f6-eb4d4d25fdc0
Total jobs = 1
Launching Job 1 out of 1


Status: Running (Executing on YARN cluster with App id application_1568758057499_0003)

--------------------------------------------------------------------------------
        VERTICES      STATUS  TOTAL  COMPLETED  RUNNING  PENDING  FAILED  KILLED
--------------------------------------------------------------------------------
Map 1 ..........   SUCCEEDED      1          1        0        0       0       0
--------------------------------------------------------------------------------
VERTICES: 01/01  [==========================>>] 100%  ELAPSED TIME: 6.56 s
--------------------------------------------------------------------------------
OK
05a888532c570229af2b539e18030dc4        Iris-setosa
7db4a6dcd27fd81316b7987dad40936c        Iris-setosa
6d69a940d56f671953aabcf4030352a1        Iris-setosa
1f78515b5f35c5fb0d2ea5c369cd406d        Iris-setosa
fa000ea6942640e64aa3b19e5320d953        Iris-setosa
Time taken: 10.708 seconds, Fetched: 5 row(s)

"""

