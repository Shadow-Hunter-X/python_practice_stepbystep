# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:48:10 2020

@author: JSKJ
"""

from pyspark import SparkContext
from pyspark.sql import SparkSession
sc=SparkContext(appName="spark sql mathplotlib")          
spark=SparkSession.builder.appName('spark sql mathplotlib').master("Yct201811021847").getOrCreate()

movies_df=spark.read.csv('movies.csv',header=True, inferSchema=True).dropna()
ratings_df=spark.read.csv('ratings.csv',header=True,inferSchema=True).dropna()
movies_df.createOrReplaceTempView('movies')      
ratings_df.createOrReplaceTempView('ratings')

data=spark.sql(" SELECT title , rating , userID, genres ,avg_movie_rating , DENSE_RANK() OVER( ORDER BY avg_movie_rating desc) rank FROM \
    (SELECT m.title , rating , userID, m.genres, \
    AVG(rating) OVER(partition by m.movieId) avg_movie_rating \
    FROM  movies m LEFT JOIN ratings r ON r.movieId = m.movieId \
    WHERE rating is not null ) A ")

data.createOrReplaceTempView('data')


users=spark.sql(" select userID , count(*) cnt from data where rank='1' group by userID").filter('cnt > 4')
user_pd=users.toPandas()
userID=user_pd.userID.to_list()
user_cnt = user_pd.cnt.to_list()
len(user_cnt)



import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_figheight(7)
fig.set_figwidth(7)

ax1 = fig.add_subplot(211)
ax1.scatter(np.arange(9),user_cnt)
ax1.set_xticklabels(user_cnt,rotation=45)

ax2 = fig.add_subplot(212)
ax2.bar(np.arange(9),user_cnt)
ax2.set_xticklabels(user_cnt,rotation=45)

#ax3 = fig.add_subplot(313)
#ax3.bar(len(user_cnt),user_cnt)
#ax3.set_xticklabels(userID,rotation=45)




