# crimes-on-map Public API: 
Hosted url: http://theta-anchor-215617.appspot.com/map/chicago

To deploy the app:

cd crimes-app/web/
FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run

Google Cloud App Engine:

cd crimes-app/web/
gcloud app deploy

# Kibana Dashboard:

Hosted url: http://34.73.60.209:5601/goto/8686eb5d7c8ed31f4e0252b9c29972df

# Elasticsearch "combined-crimes" Index:

Hosted url: http://34.73.60.209:5601/goto/c88a4b9daa79677d6bbb902677e42080

# Descriptions of Python Notebooks:

1) API_Stress_Test.ipynb: Uploads a .csv of 1M records to the API bulk upload endpoint with the goal of stressing the system

2) ChicagoRentalPrices.ipynb: Currently assigns ZIP codes to all Chicago crime records based on geolocation and then uses these ZIP codes to assign rental prices 

3) LARentalPrices.ipynb: Same as ChicagoRentalPrices.ipynb, but for Los Angeles crime records

4) Crime_Type_Dict.ipynb: Manual mapping for crime types between Chicago and Los Angeles

5) csv-to-elasticsearch.ipynb: Uploads a .csv directly to Elasticsearch index

6) kafka-producer.ipynb: Uploads a .csv to Kafka after checking to make sure data fields match Elasticsearch index. These functions are deployed in the Spark code. 

7) Prediction_Tasks.ipynb: Builds machine learning models from rental price and neighborhood crime schools. Predicts future data points 

8) sample_upload_bad.csv: Sample .csv to test the data field matching when uploading to Kafka topic

9) sample_upload_good.csv:  Sample .csv to test the data field matching when uploading to Kafka topic

10) addCrimeScoreAsTimeSeries.ipynb: 

11) calculateCrimeScore.ipynb: 

12) linear_regression_spark.ipynb
