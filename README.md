# Neusoft2018clusterProject

该文档分两部分，第一部分是分词与权重设置，第二部分会对文档进行聚类

分词&聚类
files文件夹中存放的是论文库。
在第一部分中，首先对文档进行了分词处理（采用结巴分词）。文档中的医学术语库和停用词库都是为分词所准备的
接着，基于TF-IDF，采用了两种权重提取方式。两种方式分别为两个py文件“论文权重”和“权重提取2”
运行不同的提取文件，都会生成相应的“key”和“dataresult”（在result文件夹中）这两个文件将会在第二部分聚类中被使用。
