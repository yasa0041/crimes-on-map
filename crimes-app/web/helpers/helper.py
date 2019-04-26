import os
from datetime import datetime
from flask import current_app as app


def remove_file(filename):
    os.remove(filename)
    print("Deleted file {}", filename)

def reportCrime(record):
    # city = record['city']
    # crime_type = record['type']
    # latlong = record['latlong']
    # location_desc = record['loc_desc']
    # crime_desc = record['crime_desc']
    #'Case_ID', 'Crime_Description', 'Date', 'Geolocation', 'Location_Description', 'Neighborhood_Score', 'Predicted_Neighborhood_Score', 'Predicted_Rental_Price', 'Rental_Price', 'Zipcode'
    print(record)
    record['Date'] = datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')
    record['Case_ID'] = str(record['City'])+str(record['Date'])
    return uploaSingleRecord(record)

def uploadCrimeRecord(filename):
    df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    fields = app.config['DATA_COLS']
    if sorted(fields) == sorted(list(df.columns)):
        print('Uploading to Kafka topic:', app.config['KAFKA_TOPIC'])
        df.apply(lambda x: app.config['KAFKA_PRODUCER'].send(app.config['KAFKA_TOPIC'] , value = x.to_dict()), axis=1)
    else:
        remove_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Incorrect Columns in the uploaded csv. The data fields of {} must match: {}'.format(filename, fields), 401
    
    return 'File uploaded successfully!'

def uploaSingleRecord(record):
    app.config['KAFKA_PRODUCER'].send(app.config['KAFKA_TOPIC'] , value = record)
    return "reported a crime", 200