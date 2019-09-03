---
title ： 构建分析用数据
---


# 导入测试用数据

	为了能够良好的开展

## 1 关于 MovieLens电影数据
	用户电影评分MovieLens, MovieLens多被用于推荐系统的学习数据。它由美国 Minnesota 大学计算机科学与工程学院的 GroupLens 项目组创办，是一个非商业性质的、以研究为目的的实验性站点。
	完整数据下载  ：  http://files.grouplens.org/datasets/movielens/ml-latest.zip
	数据样例下载  ：  http://files.grouplens.org/datasets/movielens/ml-latest-small.zip
	
	下载的数据包中包含了4个数据文件，分别如以下：
	（1）ratings.csv - 电影评分数据集 ；userId,movieId,rating,timestamp 为其数据列：表示每个用户对每部电影在什么时候的评分。
	（2）movies.csv - 对电影的分类数据集 ；movieId,title,genres 为其数据列：表示了每部电影的名字和分类。
	（3）tags.csv - 标签文件 ； userId,movieId,tag,timestamp 为其数据列：表示每个用户对电影的分类。
	（4）links.csv - 链接信息 ； movieId,imdbId,tmdbId 为其数据列： 每个电影的 imdb(网路电影资料库),tmdb(电影数据库)的关联编号。
	

## 2 关于iris_dataset鸢尾属植物数据
	Iris数据集是常用的分类实验数据集，Iris也称鸢尾花卉数据集，是一类多重变量分析的数据集。数据集包含150个数据样本，分为3类，每类50个数据，每个数据包含4个属性。
	可通过花萼长度，花萼宽度，花瓣长度，花瓣宽度4个属性预测鸢尾花卉属于哪一类。
    
   
     
## 3 下载并导入

### 3.1 导入到HDP中 
	
### 3.2 导入到自行安装的大数据环境中 

### 3.3 Windows上的Spark的使用

# 查看数据使用数据

  使用HDFS命令查看数据
  
  使用Hive查看数据
  
  使用Spark查看数据


# 总结


