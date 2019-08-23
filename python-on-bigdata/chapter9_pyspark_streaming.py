import time 
import datetime
import sys 
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def net_streaming(stream_sc,host,port):
	"""
	"""
	print '---------------net streaming------------------\n'
	socketTexts = stream_sc.socketTextStream(host, int(port))
	counts = socketTexts.flatMap(lambda line: line.split(" "))\
	                       .map(lambda word: (word, 1))\
						   .reduceByKey(lambda a, b: a+b)
	
	counts.pprint()
	stream_sc.start()
	stream_sc.awaitTerminationOrTimeout(timeout=100)
	stream_sc.stop(stopSparkContext=False,stopGraceFully=True)
	
	
def file_streaming(stream_sc):
	"""
	"""
	print '\n---------------file streaming------------------'
	file_stream = stream_sc.textFileStream("D:\Developing\data")
	file_stream.pprint()
	
	stream_sc.start()
	stream_sc.awaitTerminationOrTimeout(timeout=3)
	stream_sc.stop(stopSparkContext=False,stopGraceFully=True)
	
def kafka_streaming(stream_sc):
	"""
	"""
	pass 
		
def flume_streaing(stream_sc):
	"""
	"""
	pass
	
def save_streaming(stream_sc):
	"""
	"""
	pass
	
if __name__ == '__main__':
	
	if len(sys.argv) != 3:
		print "usage: chapter9_pyspark_streaming.py <host> <port>" 
		exit(-1)
		
	sc=SparkContext(appName="pyspark_streaming")
	stream_sc = StreamingContext(sc, 1)
	
	net_streaming(stream_sc,sys.argv[1],sys.argv[2])
	#file_streaming(stream_sc)
	#kafka_streaming(stream_sc)
	#save_streaming(stream_sc)
	