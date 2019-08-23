from pyspark import SparkContext

def test_parallelize(sc):
	"""
	对parallelize使用
	"""
	print('{}{}'.format('parallelize:',sc.parallelize([0, 2, 3, 4, 6], 5).collect()))

def test_textFile(sc):
	"""
	对textFile使用
	"""
	lines=sc.textFile('2019-06-11-15-23-10.txt')
	print('{}{}'.format('textFile -> num of doc lines:',lines.count()))
	print('{}{}'.format('textFile -> doc first line:',lines.first()))
	resoult={}
	str = ''.join(lines.collect())
	for i in str:
		resoult[i]=str.count(i)
	print(resoult)

def test_wholeTextFiles(sc):
	"""
	对wholeTextFiles使用
	"""
	lines=sc.wholeTextFiles('2019-06-11-15-23-10.txt')
	print('{}{}'.format('wholeTextFiles -> num of doc lines:',lines.count()) )
	print('{}{}'.format('wholeTextFiles -> doc first line:',lines.first()) )
	
if __name__=='__main__': 
	sc = SparkContext()
	test_parallelize(sc)
	test_textFile(sc)
	test_wholeTextFiles(sc)