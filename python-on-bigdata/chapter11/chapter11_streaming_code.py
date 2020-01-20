#coding:utf-8
import time 
import datetime
import sys 

from pyspark import SparkContext
from pyspark.streaming import StreamingContext                   

def net_streaming():
	'''
	功能     ：连接到TCP服务器，接收处理Socket数据流
	参数host ： TCP服务器IP
	参数port ： TCP服务器端口
	'''

	if len(sys.argv) != 3:
		print "usage: chapter9_streaming.py <tcp host> <tcp port>"
		return -1

	host,port = sys.argv[1],sys.argv[2]

	sc=SparkContext(appName="pyspark_net_streaming")              
	stream_sc = StreamingContext(sc, 1)							
	socketTexts = stream_sc.socketTextStream(host, int(port))	  
	
	counts = socketTexts.flatMap(lambda line: line.split(" "))\
	                       .map(lambda word: (word, 1))\
			       .reduceByKey(lambda a, b: a+b)
						   
	counts.pprint(24)	
	stream_sc.start()  		
	stream_sc.awaitTerminationOrTimeout(timeout=30)				
	stream_sc.stop(stopSparkContext=False,stopGraceFully=True)	

# 对于进行Spark Streaming处理中需要的库
# 创建SparkContext对象，对于每一个Spark应用都需要一个 Spark上下文对象来Spark API
# 在现有的SparkContext的基础上创建StreamingContext，第二个参数表示流出数据频率为1秒
# 通过socketTextStream 连接到对应的TCP服务器
#数据的转换操作：3个Transformations操作,flatMap函数将文本数据按空格划分，及生成了由单词构成的DStream；map函数函数将每个单词构成键值对的形式RDD；reduceByKey函数将有map函数生成的DStream数据，进行按单词统计
# 查看计算结果，这一步相当于Action操作，会触发上面Transformations操作的执行
# 开始执行数据流
# 等待停止执行；可以设置等待超时设置
# 关闭流处理,stopSparkContext连同底层的SparkContext一起关闭，stopGraceFully 是否已优雅的方式,等待所以数据接收处理完毕。
	

from pyspark.sql import SparkSession

def file_save(rdd):
	'''
	   功能  :	将数据追加保存到json文件
	'''
	if not rdd.isEmpty():
		rdd.toDF(["sepal_length","sepal_width","petal_length","petal_width ","species"]).write.save("data_json",format="json",mode="append")

def file_streaming_static():
	"""
	   功能  :  监控在HDFS上的json文件，读取数据将处理的结果保存会HDFS
	"""
	sc=SparkContext.getOrCreate()								  
	spark=SparkSession(sc)

	stream_sc = StreamingContext(sc, 1)  
	file_data = stream_sc.textFileStream("hdfs://127.0.0.1:9000/test_data").map( lambda x: x.split(","))	
	
	file_data.pprint(24)
	file_data.foreachRDD(file_save)		
	
	stream_sc.start()					
	stream_sc.awaitTerminationOrTimeout(timeout=30)				
	stream_sc.stop(stopSparkContext=True,stopGraceFully=True)	


#创建SparkContext对象，对于每一个Spark应用都需要一个 Spark上下文对象来Spark API ,使用getOrCreate从检查点数据重新创建一个StreamingContext，没有的话创建一个新的StreamingContext
#在现有的SparkContext的基础上创建StreamingContext，第二个参数表示流出数据频率为1秒
#对指定的HDFS目录进行监控，对其中的csv文件，处理


import numpy as np
import time
import datetime

def data_file():
	'''
	每隔3秒生成一个csv文件，最多生成10个文件
	'''
	i = 0 
	while(i<10):
		x = np.random.rand(4, 4)			# x 变量 ，矩阵 4*4 	
		y = np.random.randint(-10, 10, 4)		# y 结果 ，数组 4 

		t = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())		# 以当前时间作为文件名
		f = open('/home/hadoop/stream/'+t ,'w')						# 创建打开文件

		for i in range(len(y)):										# 写入数据操作
			output = " %0.4f, %0.4f, %0.4f, %0.4f , %d\n" % (x[i,0], x[i,1], x[i,2], x[i,3],y[i])
			f.write(output)
		
		f.close()													# 关闭文件
		print t
		time.sleep(3)
		i+=1
		
def file_streaming_dynamic():
	'''
   	功能：处理在linux文件系统上动态生成的文件csv文件，并将处理的文件转存到其他的目录下
	'''
	sc=SparkContext.getOrCreate()
	stream_sc = StreamingContext(sc, 1)
	file_stream = stream_sc.textFileStream("file:///home/hadoop/stream/").map( lambda x: x.split(","))

	file_stream.pprint(24)
	file_stream.saveAsTextFiles("/home/hadoop/output/")	

	stream_sc.start()
	stream_sc.awaitTerminationOrTimeout(timeout=100)
	stream_sc.stop(stopSparkContext=True,stopGraceFully=True)

	
from pyspark.streaming.kafka import KafkaUtils

def kafka_streaming():
	'''
    功能：接收处理kafka消息	
	'''

	if len(sys.argv) != 3:
		print "Usage: chapter9_streaming.py <zookeepr host> <topic name>"
		return -1

	sc=SparkContext(appName="kafka_streaming")
	ssc=StreamingContext(sc, 1)

	zkQuorum,topic = sys.argv[1:]
	kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
	lines=kvs.map(lambda x: x[1])
	counts = lines.flatMap(lambda line: line.split(" ")) \
			      .map(lambda word: (word, 1)) \
			      .reduceByKey(lambda a, b: a+b)

	counts.pprint(24)

	ssc.start()
	ssc.awaitTerminationOrTimeout(timeout=30)
	ssc.stop(stopSparkContext=True,stopGraceFully=True)
	
if __name__ == '__main__':
	#net_streaming()
	#file_streaming_static()
	#data_file()
	#file_streaming_dynamic()
	kafka_streaming()
	
