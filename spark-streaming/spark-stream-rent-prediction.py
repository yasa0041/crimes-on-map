from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
import sys
#import nltk
#from nltk.sentiment.vader import SentimentIntensityAnalyzer

appName = "Spark-Kafka-Crime-Stream"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

def getSparkSessionInstance(sparkConf):
    if ('sparkSessionSingletonInstance' not in globals()):
        globals()['sparkSessionSingletonInstance'] = SparkSession\
            .builder\
            .config(conf=sparkConf)\
            .getOrCreate()
    return globals()['sparkSessionSingletonInstance']

ssc = StreamingContext(sc, 1)

es_write_conf = {
        "es.nodes" : "elastic-2",
        "es.port" : "9200",
        "es.resource" : 'combined_crimes_test/type',
        "es.input.json": "yes",
        "es.input.id":"Case_Id"
    }

def predict_rent(x):
    try:
        df
    except NameError:
        spark = getSparkSessionInstance(conf)
        df = spark.read.csv('/home/sapra_yash93/crimes-on-map/spark-streaming/rent-predictions.csv', header='true')
    
    price = df.select('Rental_Price').where(df['Zipcode']==x['Zipcode']).collect()
    if (len(price)):
        x['Rental_Price'] = 100
        #price[0]['Rental_Price']
        x['Predicted'] = "True"
        print("Predicted price {} for Zipcode {}".format(x['Rental_Price'], x['Zipcode']))
    else:
        print("No data to predict price for Zipcode: {}".format(x['Zipcode']))
    return x

lines = KafkaUtils.createDirectStream(ssc, ['crimes'], {"metadata.broker.list": "35.232.117.118:9092"})
lines.pprint()
sentiments = lines.map(lambda j: predict_rent(json.loads(j[1])))

final_rdd = sentiments.map(json.dumps).map(lambda x: ('key', x))
final_rdd.pprint()
final_rdd.foreachRDD(lambda j: j.saveAsNewAPIHadoopFile(
    path='-',
    outputFormatClass="org.elasticsearch.hadoop.mr.EsOutputFormat",
    keyClass="org.apache.hadoop.io.NullWritable",
    valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
    conf=es_write_conf
))

ssc.start()
ssc.awaitTermination()
