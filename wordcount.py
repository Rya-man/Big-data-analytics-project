from pyspark import SparkConf, SparkContext

def main():
    conf = SparkConf().setAppName("WordCount")
    sc = SparkContext(conf=conf)

    # Sample data
    data = ["Hello world", "Hello Spark", "Hello Docker", "Hello Windows"]

    # Parallelize the data
    rdd = sc.parallelize(data)

    # Perform word count
    counts = rdd.flatMap(lambda line: line.split(" ")) \
                .map(lambda word: (word, 1)) \
                .reduceByKey(lambda a, b: a + b)

    # Collect and print the results
    results = counts.collect()
    for word, count in results:
        print(f"{word}: {count}")

    sc.stop()

if __name__ == "__main__":
    main()
