if __name__ == '__name__':
    sc = sparkContext()
    result = sc.textFile('book.txt') \
    .flatMap(lambda x: x.split()) \
    .map(lambda x: (x,1)) \
    .reduceByKey(lambda x,y: x+y) \
    .saveAsTextFile('output')
