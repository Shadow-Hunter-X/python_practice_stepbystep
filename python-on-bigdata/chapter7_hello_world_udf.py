from pig_util import outputSchema

@outputSchema('str:chararray')
def hello_world():
    return "hello world"
		
'''
REGISTER '/home/hadoop/test_data/hello_world.py' using streaming_python as hello_udf ;
movies_data = load '/home/hadoop/test_data/movies.csv' using PigStorage(',') as (movieId:chararray, title:chararray, genres:chararray) ;
movies_10 = LIMIT movies_data 10 ; 
movies_10_hello = FOREACH movies_10 GENERATE hello_udf.hello_world() ;
dump movies_10_hello ;
'''

#-------------------------------------------------------------------


from pig_util import outputSchema
from datetime import datetime
import re

@outputSchema('title:chararray')
def parse_title(title):
"""
	取得电影名,去掉年份
"""
	movie_name = re.sub(r'\s*\(\d{4}\)','', title)
	groups=re.search(r'\s*\(\d{4}\)',title,re.M|re.I)
	if groups:
		issue_year=int(title[groups.span()[0]:groups.span()[1]].strip()[1:5])
		year_diff=datetime.now().year - issue_year
		return movie_name ,  issue_year , year_diff
	return movie_name , -1 , -1 
	
@outputSchema('days_since_release:int')
def days_since_release(date):
"""
	计算电影至今，推出了多少年
"""
	if date is None:
		return None
	today = datetime.today()
	release_date = datetime.strptime(date, '%d-%b-%Y')
	delta = today - release_date
	return delta.days

'''
```
REGISTER '/home/hadoop/test_data/date_diff.py' USING streaming_python AS date_diff;

-- 加载Python脚本
records = LOAD '/home/hadoop/test_data/movies.csv' USING PigStorage(',') AS (movieId:int, title:chararray, release_date:chararray);

-- 解析电影名和计算出版时间
titles = FOREACH records GENERATE date_diff.parse_title(title) ;

data = limit titles 10 ;

dump data
'''


