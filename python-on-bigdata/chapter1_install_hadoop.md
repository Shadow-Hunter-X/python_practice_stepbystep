---
在Ubuntu上安装单机版大数据环境
---


#1 安装ubuntu虚拟机

http://mirrors.aliyun.com/ubuntu-releases/ 
在阿里云镜像网站上，选项自己需要的ubuntu版本，下载即可。

开启root账号 ，为方便起见，应用中用root账号进行安装

~~~
hadoop@ubuntu:~$ sudo passwd root
[sudo] password for hadoop: 
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
hadoop@ubuntu:~$  

安装ssh服务：
apt-get install openssh-server
开启服务
sudo service ssh start

vi /etc/ssh/sshd_config 
PermitRootLogin without-password  --> PermitRootLogin yes

~~~


#2 安装JDK

https://www.oracle.com/technetwork/cn/java/javase/downloads/jdk8-downloads-2133151-zhs.html

到oracle官网下载JDK，在成功下载后，进行安装操作，按以下步骤：

~~~
* 1 解压 jdk 压缩包： tar -zxvf 

root@ubuntu:/usr# tar -zxvf jdk-8u11-linux-x64.tar.gz -C ./

* 2 修改文件夹名 
root@ubuntu:/usr# mv jdk1.8.0_11/ jvm

* 3 配置
root@ubuntu:/usr# vi /etc/profile
  
  添加以下的配置信息
  export JAVA_HOME=/usr/jvm
  export JRE_HOME=${JAVA_HOME}/jre  
  export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib   
  export PATH=${JAVA_HOME}/bin:$PATH
  
* 4 配置完成后的生效和查看  
root@ubuntu:/usr# source /etc/profile
root@ubuntu:/usr# java -version
java version "1.8.0_11"
Java(TM) SE Runtime Environment (build 1.8.0_11-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.11-b03, mixed mode)
 
~~~


#3 安装anaconda开发环境

~~~

下载地址： https://repo.continuum.io/archive/index.html

1 可直至从浏览器下载，也可以使用下载工具wget ： wget https://repo.continuum.io/archive/Anaconda2-2019.07-Linux-x86_64.sh
下载完毕后，即可进行安装操作

2 查看文件MD5值是否完整的下载，如果没有完整下载，将无法完成安装

md5sum Anaconda2-2019.07-Linux-x86_64.sh 
如下载中出现错误，安装时会提示： ERROR: size of Anaconda3-2019.07-Linux-x86_64.sh should be    541906131 bytes

bash Anaconda2-2019.07-Linux-x86_64.sh
在安装期间，首先会提示阅读并同意相关条款，按回车键即可。


3 成功安装后,会提示是否进行初始化操作：输入 yes 
Do you wish the installer to initialize Anaconda2
by running conda init? [yes|no]
[no] >>> yes

成功安装后，会出现以下的提示信息：
If you'd prefer that conda's base environment not be activated on startup, 
   set the auto_activate_base parameter to false: 

conda config --set auto_activate_base false

Thank you for installing Anaconda2!

4 验证查看安装的anaconda

(base) root@ubuntu:/usr/Anaconda2# conda --version
conda 4.7.10

5 安装需要的pthon库
打开 anaconda-navigator​
--(base) root@ubuntu:/usr/Anaconda2# conda install -c anaconda anaconda-navigator​
--Collecting package metadata (current_repodata.json): \ 

如安装 : pyhive , pyspark 等 （如果安装太慢，可更变anaconda的镜像源）

[一张图片的引用]

6 注：在windows上安装较为简单，下载安装包后即可安装。


~~~


# 4 安装Hadoop 

官方网站下载地址 ：https://hadoop.apache.org/releases.html  
如下载速度太慢，可选择国内的镜像源：http://www.apache.org/mirrors/

下载完安装包，后进行安装操作：
	1 解压
	  	
	2 配置
	/etc/profile
	export HADOOP_HOME=/usr/hadoop-2.8.5
	export CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath):$CLASSPATH
	export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
	export PATH=$PAHT:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
	
	
	/hadoop-env.sh
	export JAVA_HOME=/usr/JVM
	
	
	/core-site.xml
	<configuration>
        <property>
             <name>hadoop.tmp.dir</name>
             <value>file:/usr/hadoop-2.8.5/tmp</value>
             <description>Abase for other temporary directories.</description>
        </property>
        <property>
             <name>fs.defaultFS</name>
             <value>hdfs://localhost:9000</value>
        </property>
	</configuration>
	
	/hdfs-site.xml
	<configuration>
        <property>
             <name>dfs.replication</name>
             <value>1</value>
        </property>
        <property>
             <name>dfs.namenode.name.dir</name>
             <value>file:/usr/hadoop-2.8.5/tmp/dfs/name</value>
        </property>
        <property>
             <name>dfs.datanode.data.dir</name>
             <value>file:/usr/hadoop-2.8.5/tmp/dfs/data</value>
        </property>
	</configuration>

	/maped-site.xml    
	(base) root@hadoop# cp mapred-site.xml.template mapred-site.xml
	
	<configuration>
	<property>
		<name>mapreduce.framework.name</name>
		<value>yarn</value>
		</property>
	</configuration>
	
	/yarn-site.xml
	 <property>
		<name>yarn.nodemanager.aux-services</name>
		<value>mapreduce_value</value>
	</property>
	

	配置完成后，执行namenode的初始化
	./usr/hadoop-2.8.5/bin/hdfs namenode -format
	
	启动namenode和datanode进程
	./usr/hadoop-2.8.5/sbin/start-dfs.sh   start-yarn.sh 或就是直接用start-all.sh
	
	3 验证
	
	 http://localhost:50070  
	 
	 hdfs 命令的使用

	 jps 查看开启的进程
	 
5 hive 使用 hive 1.2.2 解压即可运行

6 spark 安装  
	tar -zxvf spark-2.2.0-bin-hadoop2.7.tgz -C ./ 
	mv spark-2.2.0-bin-hadoop2.7 spark-2.2.0 
	
	配置文件： 
	/etc/profile 
	43 export SPAKR_HOME=/usr/spark-2.2.0
    44 export PAHT=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

	配置文件: spark-env.sh 
	
7 kafka安装

	下载版本：
	kafka_2.11-0.10.0.0.tgz 
	
	tar -zxvf kafka_2.11-0.10.0.0.tgz  -C ./ 
	
	bin/zookeeper-server-start.sh config/zookeeper.properties
	 
	验证： 
	7.1 开启zookeeper
		bin/zookeeper-server-start.sh config/zookeeper.properties     -- 开启一个终端，成功开启
	7.2 开启kafka ，重新开启一个终端
	    bin/kafka-server-start.sh config/server.properties      
		
	7.3 定义一个新的topic 
	    bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
		bin/kafka-topics.sh --list --zookeeper localhost:2181  用命令查看topic是否成功开启
		
	7.4 生产数据-开启消费者
		bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
		输入一些用于测试的字符串
	
	7.5 开启消费者，用于接收消息
		bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning 
	
		
---------------------------

HDP 2.2 

包括 hadoop的界面
		http://192.168.223.128:8088/cluster
     spark
		
	 hbase
		
	 Ambari
		端口是 8080
		
	 Oozie
		http://192.168.223.128:11000/oozie/
	 
	 






