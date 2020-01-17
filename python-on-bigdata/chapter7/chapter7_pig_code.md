
* 1-foreach操作 

```pig 
iris = load '/user/root/test_data/iris.data' using PigStorage(',') as (sepal_length, sepal_width, petal_length, petal_width,species);
iris_10 = LIMIT iris 10 ; 
--store processed into '/user/root/test_data' ; 
cell = foreach iris_10 generate sepal_length, sepal_width, petal_length, petal_width,species ;
dump cell;

2019-09-25 08:28:18,619 [main] INFO  org.apache.pig.tools.pigstats.ScriptState - Pig features used in the script: LIMIT
2019-09-25 08:28:18,730 [main] WARN  org.apache.pig.data.SchemaTupleBackend - SchemaTupleBackend has already been initialized
2019-09-25 08:28:18,731 [main] INFO  org.apache.pig.newplan.logical.optimizer.LogicalPlanOptimizer - {RULES_ENABLED=[AddForEach, ColumnMapKeyPrune, ConstantCalculator, GroupByConstParallelSetter, LimitOptimizer, LoadTypeCastInserter, MergeFilter, MergeForEach, PartitionFilterOptimizer, PredicatePushdownOptimizer, PushDownForEachFlatten, PushUpFilter, SplitFilter, StreamTypeCastInserter]}
2019-09-25 08:28:18,980 [main] INFO  org.apache.pig.data.SchemaTupleBackend - Key [pig.schematuple] was not set... will not generate code.
2019-09-25 08:28:19,066 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input paths to process : 1
2019-09-25 08:28:19,066 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
2019-09-25 08:28:19,243 [main] INFO  org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter - Saved output of task 'attempt__0001_m_000001_1' to hdfs://sandbox.hortonworks.com:8020/tmp/temp-1643266101/tmp768395684/_temporary/0/task__0001_m_000001
2019-09-25 08:28:19,461 [main] WARN  org.apache.pig.data.SchemaTupleBackend - SchemaTupleBackend has already been initialized
2019-09-25 08:28:19,525 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input paths to process : 1
2019-09-25 08:28:19,525 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
(5.1,3.5,1.4,0.2,Iris-setosa)
(4.9,3.0,1.4,0.2,Iris-setosa)
(4.7,3.2,1.3,0.2,Iris-setosa)
(4.6,3.1,1.5,0.2,Iris-setosa)
(5.0,3.6,1.4,0.2,Iris-setosa)
(5.4,3.9,1.7,0.4,Iris-setosa)
(4.6,3.4,1.4,0.3,Iris-setosa)
(5.0,3.4,1.5,0.2,Iris-setosa)
(4.4,2.9,1.4,0.2,Iris-setosa)
(4.9,3.1,1.5,0.1,Iris-setosa)

```


* 2-filter操作

```Pig
iris_ver = filter iris by species matches 'Iris-versicolor';
iris_ver_10 = limit iris_ver 10 ;
cell_ver = foreach iris_ver_10 generate petal_length, petal_width,species ;
dump cell_ver;

2019-09-25 08:59:06,817 [main] INFO  org.apache.pig.tools.pigstats.ScriptState - Pig features used in the script: LIMIT
2019-09-25 08:59:06,967 [main] WARN  org.apache.pig.data.SchemaTupleBackend - SchemaTupleBackend has already been initialized
2019-09-25 08:59:07,045 [main] INFO  org.apache.pig.newplan.logical.optimizer.LogicalPlanOptimizer - {RULES_ENABLED=[AddForEach, ColumnMapKeyPrune, ConstantCalculator, GroupByConstParallelSetter, LimitOptimizer, LoadTypeCastInserter, MergeFilter, MergeForEach, PartitionFilterOptimizer, PredicatePushdownOptimizer, PushDownForEachFlatten, PushUpFilter, SplitFilter, StreamTypeCastInserter]}
2019-09-25 08:59:07,061 [main] INFO  org.apache.pig.newplan.logical.rules.ColumnPruneVisitor - Columns pruned for iris: $0, $1
2019-09-25 08:59:07,155 [main] INFO  org.apache.pig.data.SchemaTupleBackend - Key [pig.schematuple] was not set... will not generate code.
2019-09-25 08:59:07,480 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input paths to process : 1
2019-09-25 08:59:07,480 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
2019-09-25 08:59:07,811 [main] INFO  org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter - Saved output of task 'attempt__0001_m_000001_1' to hdfs://sandbox.hortonworks.com:8020/tmp/temp-1643266101/tmp521198451/_temporary/0/task__0001_m_000001
2019-09-25 08:59:07,864 [main] WARN  org.apache.pig.data.SchemaTupleBackend - SchemaTupleBackend has already been initialized
2019-09-25 08:59:07,871 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input paths to process : 1
2019-09-25 08:59:07,871 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
(1.4,0.2,Iris-setosa)
(1.4,0.2,Iris-setosa)
(1.3,0.2,Iris-setosa)
(1.5,0.2,Iris-setosa)
(1.4,0.2,Iris-setosa)
(1.7,0.4,Iris-setosa)
(1.4,0.3,Iris-setosa)
(1.5,0.2,Iris-setosa)
(1.4,0.2,Iris-setosa)
(1.5,0.1,Iris-setosa)

```

* 3-group操作
 
```Pig
group_num = group iris by species ;
cnt = foreach group_num generate group, COUNT(iris);
dump cnt 
2019-09-25 09:48:28,520 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-25 09:48:28,521 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-25 09:48:28,527 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-25 09:48:29,102 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-25 09:48:29,103 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-25 09:48:29,108 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-25 09:48:30,163 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-25 09:48:30,163 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-25 09:48:30,201 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-25 09:48:31,228 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Success!
2019-09-25 09:48:31,230 [main] INFO  org.apache.pig.data.SchemaTupleBackend - Key [pig.schematuple] was not set... will not generate code.
2019-09-25 09:48:31,282 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input paths to process : 1
2019-09-25 09:48:31,282 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
(Iris-setosa,50)
(Iris-virginica,50)
(Iris-versicolor,50)
(,0)
```

* 4-order by操作

```Pig
order_by = order iris by petal_length ;
order_by_cell = foreach order_by generate petal_length ,species ;
dump order_by_cell ;
HadoopVersion   PigVersion      UserId  StartedAt       FinishedAt      Features
2.6.0.2.2.4.2-2 0.14.0.2.2.4.2-2        root    2019-09-25 09:59:57     2019-09-25 10:07:24     ORDER_BY

Success!

Job Stats (time in seconds):
JobId   Maps    Reduces MaxMapTime      MinMapTime      AvgMapTime      MedianMapTime   MaxReduceTime   MinReduceTime   AvgReduceTime   MedianReducetime     Alias    Feature Outputs
job_1569388191536_0004  1       1       196     196     196     196     44      44      44      44      order_by        SAMPLER
job_1569388191536_0005  1       1       65      65      65      65      16      16      16      16      order_by,order_by_cell  ORDER_BY        hdfs://sandbox.hortonworks.com:8020/tmp/temp-823389658/tmp-38180957,

Input(s):
Successfully sampled 100 records (4943 bytes) from: "/user/root/test_data/iris.data"
Successfully read 151 records (4943 bytes) from: "/user/root/test_data/iris.data"

Output(s):
Successfully stored 151 records (3656 bytes) in: "hdfs://sandbox.hortonworks.com:8020/tmp/temp-823389658/tmp-38180957"

Counters:
Total records written : 151
Total bytes written : 3656
Spillable Memory Manager spill count : 0
Total bags proactively spilled: 0
Total records proactively spilled: 0

Job DAG:
job_1569388191536_0004  ->      job_1569388191536_0005,
job_1569388191536_0005


2019-09-25 10:07:24,760 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-25 10:07:24,760 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-25 10:07:24,766 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-25 10:07:25,929 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-25 10:07:25,929 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-25 10:07:25,941 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-25 10:07:26,421 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-25 10:07:26,421 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-25 10:07:26,426 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-25 10:07:27,200 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-25 10:07:27,200 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-25 10:07:27,206 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-25 10:07:27,942 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-25 10:07:27,942 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-25 10:07:28,064 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-25 10:07:29,045 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-25 10:07:29,046 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-25 10:07:29,050 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-25 10:07:29,812 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Success!
2019-09-25 10:07:29,814 [main] INFO  org.apache.pig.data.SchemaTupleBackend - Key [pig.schematuple] was not set... will not generate code.
2019-09-25 10:07:29,822 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input paths to process : 1
2019-09-25 10:07:29,822 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
(,)
(1.0,Iris-setosa)
(1.1,Iris-setosa)
(1.2,Iris-setosa)
(1.2,Iris-setosa)
(1.3,Iris-setosa)
(1.3,Iris-setosa)
(1.3,Iris-setosa)
(1.3,Iris-setosa)
(1.3,Iris-setosa)
(1.3,Iris-setosa)
(1.3,Iris-setosa)
(1.4,Iris-setosa)
(1.4,Iris-setosa)
(1.4,Iris-setosa)
(1.4,Iris-setosa)
(1.4,Iris-setosa)
(1.4,Iris-setosa)
(1.4,Iris-setosa)
(1.4,Iris-setosa)
(1.4,Iris-setosa)
(1.4,Iris-setosa)
(1.4,Iris-setosa)
......
```


* distinct

```Pig
uniq =  distinct iris ;
```


* join操作

```Pig
-- 加载movie数据
movies = load '/user/root/test_data/movies.csv' using PigStorage(',') as (movieId, title, genres);
-- 加载links数据
links = load '/user/root/test_data/links.csv' using PigStorage(',') as (movieId, imdbId, tmdbId);
-- 将movies和links进行关联，通过movieId
movie_links = join movies by movieId , links by movieId ;
-- 限制10条数据
movie_links_10 = limit movie_links 10 ;
-- 注意对于movieId在两个数据集中都有，所以需要区分，使用movies::moveId
movie_links_10_cell = foreach movie_links_10 generate movies::movieId ,title ,imdbId , tmdbId;
-- 查看数据
dump movie_links_10_cell

HadoopVersion   PigVersion      UserId  StartedAt       FinishedAt      Features
2.6.0.2.2.4.2-2 0.14.0.2.2.4.2-2        root    2019-09-26 02:28:23     2019-09-26 02:57:35     HASH_JOIN,LIMIT

Success!

Job Stats (time in seconds):
JobId   Maps    Reduces MaxMapTime      MinMapTime      AvgMapTime      MedianMapTime   MaxReduceTime   MinReduceTime   AvgReduceTime   MedianReducetime     Alias    Feature Outputs
job_1569388191536_0007  2       1       662     662     662     662     75      75      75      75      links,movie_links,movie_links_10,movies HASH_JOIN
job_1569388191536_0008  1       1       n/a     n/a     n/a     n/a     n/a     n/a     n/a     n/a     movie_links,movie_links_10_cell         hdfs://sandbox.hortonworks.com:8020/tmp/temp32236273/tmp-1365536984,

Input(s):
Successfully read 9743 records from: "/user/root/test_data/links.csv"
Successfully read 9743 records from: "/user/root/test_data/movies.csv"

Output(s):
Successfully stored 0 records in: "hdfs://sandbox.hortonworks.com:8020/tmp/temp32236273/tmp-1365536984"

Counters:
Total records written : 0
Total bytes written : 0
Spillable Memory Manager spill count : 0
Total bags proactively spilled: 0
Total records proactively spilled: 0

Job DAG:
job_1569388191536_0007  ->      job_1569388191536_0008,
job_1569388191536_0008


2019-09-26 02:57:35,451 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-26 02:57:35,452 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-26 02:57:35,458 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:36,479 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-26 02:57:36,479 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-26 02:57:36,526 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:37,532 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-26 02:57:37,532 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-26 02:57:37,691 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:38,434 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-26 02:57:38,434 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-26 02:57:38,562 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:39,495 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:40,588 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:41,088 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:41,968 [main] WARN  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Unable to get job related diagnostics
2019-09-26 02:57:42,139 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-26 02:57:42,139 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-26 02:57:42,189 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:42,676 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:43,546 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:44,899 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 02:57:45,358 [main] WARN  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Unable to retrieve job to compute warning aggregation.
2019-09-26 02:57:45,359 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Success!
2019-09-26 02:57:45,421 [main] INFO  org.apache.pig.data.SchemaTupleBackend - Key [pig.schematuple] was not set... will not generate code.
2019-09-26 02:57:45,434 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input paths to process : 1
2019-09-26 02:57:45,434 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 1
(1,Toy Story (1995),0114709,862)
(2,Jumanji (1995),0113497,8844)
(3,Grumpier Old Men (1995),0113228,15602)
(4,Waiting to Exhale (1995),0114885,31357)
(5,Father of the Bride Part II (1995),0113041,11862)
(6,Heat (1995),0113277,949)
(7,Sabrina (1995),0114319,11860)
(8,Tom and Huck (1995),0112302,45325)
(9,Sudden Death (1995),0114576,9091)
(10,GoldenEye (1995),0113189,710)

```

* left join 操作

```Pig
join movies by moviedId left outer , links by movieId ;
```

* Parallel

```Pig
iris = load '/user/root/test_data/iris.data' using PigStorage(',') as (sepal_length, sepal_width, petal_length, petal_width,species);
group_num = group iris by species parallel 10;
cnt = foreach group_num generate group, COUNT(iris) ;
dump cnt ;

2019-09-26 04:15:12,359 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-26 04:15:12,359 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-26 04:15:12,428 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 04:15:13,732 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-26 04:15:13,732 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-26 04:15:13,891 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 04:15:17,333 [main] INFO  org.apache.hadoop.yarn.client.api.impl.TimelineClientImpl - Timeline service address: http://sandbox.hortonworks.com:8188/ws/v1/timeline/
2019-09-26 04:15:17,335 [main] INFO  org.apache.hadoop.yarn.client.RMProxy - Connecting to ResourceManager at sandbox.hortonworks.com/192.168.223.128:8050
2019-09-26 04:15:17,413 [main] INFO  org.apache.hadoop.mapred.ClientServiceDelegate - Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
2019-09-26 04:15:26,202 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Success!
2019-09-26 04:15:26,205 [main] INFO  org.apache.pig.data.SchemaTupleBackend - Key [pig.schematuple] was not set... will not generate code.
2019-09-26 04:15:26,307 [main] INFO  org.apache.hadoop.mapreduce.lib.input.FileInputFormat - Total input paths to process : 10
2019-09-26 04:15:26,307 [main] INFO  org.apache.pig.backend.hadoop.executionengine.util.MapRedUtil - Total input paths to process : 10
(Iris-versicolor,50)
(,0)
(Iris-setosa,50)
(Iris-virginica,50)

```


