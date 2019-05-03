# crimes-on-map
Michael Chifala, Yash Sapra, Kamal Chaturverdi

University of Colorado, Boulder



CSCI 7000-003; Dr. Lv.;  Spring 2019

# Public API: 
Hosted url: http://theta-anchor-215617.appspot.com/map/chicago

To deploy the app:

cd crimes-app/web/
FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run

Google Cloud App Engine:

cd crimes-app/web/
gcloud app deploy

# Kibana Dashboard:

Hosted url: http://34.73.60.209:5601/goto/897fbd197445f03d50419fc10287168a

# Elasticsearch "combined-crimes" Index:

Hosted url: http://34.73.60.209:5601/goto/4494939ca907d24022495df14e5088ab

# Descriptions of Python Notebooks and .CSV files:

1) API_Stress_Test.ipynb: Uploads a .csv of 1M records to the API bulk upload endpoint with the goal of stressing the system

2) ChicagoRentalPrices.ipynb: Currently assigns ZIP codes to all Chicago crime records based on geolocation and then uses these ZIP codes to assign rental prices 

3) LARentalPrices.ipynb: Same as ChicagoRentalPrices.ipynb, but for Los Angeles crime records

4) Crime_Type_Dict.ipynb: Manual mapping for crime types between Chicago and Los Angeles

5) csv-to-elasticsearch.ipynb: Uploads a .csv directly to Elasticsearch index

6) kafka-producer.ipynb: Uploads a .csv to Kafka after checking to make sure data fields match Elasticsearch index. These functions are deployed in the Spark code. 

7) Prediction_Tasks.ipynb: Builds machine learning models from rental price and neighborhood crime schools. Predicts future data points 

8) sample_upload_bad.csv: Sample .csv to test the data field matching when uploading to Kafka topic

9) sample_upload_good.csv:  Sample .csv to test the data field matching when uploading to Kafka topic

10) addCrimeScoreAsTimeSeries.ipynb: Read the input file (all collected data), group & filter it, & save back as a .csv

11) calculateCrimeScore.ipynb: From the .csv outputted by addCrimeScoreAsTimeSeries.ipynb, calculate crime score, and save it to all records in the input file. Output is the file with crime score appended to it. 

12) linear_regression_spark.ipynb: Attempted implementation of linear regression on the input crime/rental data

13) Spark_DataFrame.csv: Output of the rental price and neighborhood crime score predictions for April 2019. For use in Spark
